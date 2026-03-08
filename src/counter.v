`default_nettype 

module counter(

    input wire i_clk,
    input wire i_rstn,             //active low reset
    input wire i_read,             //signal to read data from the FIFO
    input wire i_empty,            //signal to indicate FIFO is empty

    output reg [3:0] or_timetag    //timetag for the read data, can be used to track the order of data
  
);
endmodule
