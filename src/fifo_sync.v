`default_nettype 

module fifo_sync(

    input wire i_clk,
    input wire i_rstn,             //active low reset
    input wire i_write,            //signal to write data into the FIFO
    input wire [7:0] iw_data,      //data to be written into the FIFO  
    input wire i_read,             //signal to read data from the FIFO

    output reg [7:0] ow_data,      //data read from the FIFO
    output reg [3:0] or_timetag,   //timetag for the read data, can be used to track the order of data
    output reg ow_empty,           //signal to indicate FIFO is empty
    output reg ow_full             //signal to indicate FIFO is full
);
endmodule

