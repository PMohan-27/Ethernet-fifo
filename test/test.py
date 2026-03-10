# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

async def reset_dut(dut):
    dut.i_rstn.value = 0
    dut.i_write.value = 0
    dut.i_read.value = 0
    dut.iw_data.value = 0
    await ClockCycles(dut.i_clk, 10)
    dut.i_rstn.value = 1
    await ClockCycles(dut.i_clk, 1)


@cocotb.test()
async def test_fifo_sync_write_read(dut):
    cocotb.start_soon(Clock(dut.i_clk, 8, units="ns").start())
    await reset_dut(dut)

    dut.i_write.value = 1
    dut.iw_data.value = 0xAA
    await ClockCycles(dut.i_clk, 1)
    dut.i_write.value = 0

    dut.i_read.value = 1
    await ClockCycles(dut.i_clk, 1)
    dut.i_read.value = 0
    await ClockCycles(dut.i_clk, 5)

    assert dut.ow_data.value == 0xAA, f"expected 0xAA, got {dut.ow_data.value}"

@cocotb.test()
async def test_fifo_sync_empty_full_flags(dut):
    cocotb.start_soon(Clock(dut.i_clk, 8, units="ns").start())
    await reset_dut(dut)

    assert dut.ow_empty.value == 1, "should be empty after reset"
    assert dut.ow_full.value == 0,  "should not be full after reset"

    dut.i_write.value = 1
    for i in range(64): # fifo depth is 64
        dut.iw_data.value = i
        await ClockCycles(dut.i_clk, 1)
    dut.i_write.value = 0

    assert dut.ow_full.value == 1,  "should be full"
    assert dut.ow_empty.value == 0, "should not be empty when full"

@cocotb.test()
async def test_fifo_sync_data_order(dut):
    cocotb.start_soon(Clock(dut.i_clk, 8, units="ns").start())
    await reset_dut(dut)

    data = [0x0A, 0x0B, 0x0C, 0x0D]

    dut.i_write.value = 1
    for value in data:
        dut.iw_data.value = value
        await ClockCycles(dut.i_clk, 1)
    
    dut.i_write.value = 0
    dut.i_read.value = 1
    
    for expected_value in data:
        await ClockCycles(dut.i_clk, 1)
        assert dut.ow_data.value == expected_value, f"expected {expected_value}, got {dut.ow_data.value}"
    dut.i_read.value = 0

@cocotb.test()
async def test_fifo_sync_read_counter_increment(dut):
    cocotb.start_soon(Clock(dut.i_clk, 8, units="ns").start())
    await reset_dut(dut)

    
    dut.i_write.value = 1
    dut.iw_data.value = 0x0A
    await ClockCycles(dut.i_clk, 1)
    dut.iw_data.value = 0x0B
    await ClockCycles(dut.i_clk, 1)
    dut.i_write.value = 0

    dut.i_read.value = 1
    await ClockCycles(dut.i_clk, 1)
    assert dut.ow_data.value == 0x0A, f"expected 0x0A got {dut.ow_data.value}"
    timetag_1 = int(dut.or_timetag.value)

    await ClockCycles(dut.i_clk, 1)
    assert dut.ow_data.value == 0x0B, f"expected 0x0B got {dut.ow_data.value}"
    assert int(dut.or_timetag.value) > timetag_1, "expected recent timetag to be greater"
    dut.i_read.value = 0

@cocotb.test()
async def test_fifo_sync_reset(dut):
    cocotb.start_soon(Clock(dut.i_clk, 8, units="ns").start())
    await reset_dut(dut)

    dut.i_write.value = 1
    dut.iw_data.value = 0x0A
    await ClockCycles(dut.i_clk, 3)
    dut.i_write.value = 0

    dut.i_rstn.value = 0
    await ClockCycles(dut.i_clk, 5)
    dut.i_rstn.value = 1
    await ClockCycles(dut.i_clk, 1)

    assert dut.ow_empty.value == 1, "should be empty after reset"
    assert dut.ow_full.value == 0, "should not be full after reset"
    assert int(dut.or_timetag.value) == 0, "timetag should be zero after reset"