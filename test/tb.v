`default_nettype none
`timescale 1ns / 1ps

/* This testbench instantiates the fifo_sync module and provides signals
   that can be driven / tested by the cocotb test.py.
*/
module tb ();

  // Dump the signals to a VCD file. You can view it with gtkwave or surfer.
  initial begin
    $dumpfile("tb.vcd");
    $dumpvars(0, tb);
    #1;
  end

  // Wire up the inputs and outputs:
  reg i_clk;
  reg i_rstn;
  reg i_write;
  reg [7:0] iw_data;
  reg i_read;
  wire [7:0] ow_data;
  wire [3:0] or_timetag;
  wire ow_empty;
  wire ow_full;

  // Instantiate the fifo_sync DUT:
  fifo_sync dut (
      .i_clk(i_clk),
      .i_rstn(i_rstn),
      .i_write(i_write),
      .iw_data(iw_data),
      .i_read(i_read),
      .ow_data(ow_data),
      .or_timetag(or_timetag),
      .ow_empty(ow_empty),
      .ow_full(ow_full)
  );

endmodule
