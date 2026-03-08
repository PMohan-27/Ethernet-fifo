# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_fifo_sync(dut):
    """Sample test that always passes - no verification"""
    dut._log.info("Start FIFO Sync Test")

    # Set the clock period to 8 ns (125 MHz)
    clock = Clock(dut.i_clk, 8, units="ns")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Applying Reset")
    dut.i_rstn.value = 0
    dut.i_write.value = 0
    dut.i_read.value = 0
    dut.iw_data.value = 0
    await ClockCycles(dut.i_clk, 10)
    dut.i_rstn.value = 1

    dut._log.info("Reset Complete")

    # Sample test operations
    dut._log.info("Performing sample write operation")
    dut.i_write.value = 1
    dut.iw_data.value = 0xAB
    await ClockCycles(dut.i_clk, 1)
    
    dut._log.info("Performing sample read operation")
    dut.i_write.value = 0
    dut.i_read.value = 1
    await ClockCycles(dut.i_clk, 1)
    
    dut._log.info("Test Complete - PASSED")

