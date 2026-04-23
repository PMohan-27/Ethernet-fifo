`default_nettype none

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
    memory memory_inst(

        .i_clk(i_clk),
        .i_rstn(i_rstn),             //active low reset
        .i_write(i_write),            //signal to write data into the FIFO
        .iw_data(iw_data),      //data to be written into the FIFO  
        .i_read(i_read),             //signal to read data from the FIFO

        .ow_data(ow_data),      //data read from the FIFO
        .ow_empty(ow_empty),           //signal to indicate FIFO is empty
        .ow_full(ow_full)             //signal to indicate FIFO is full
    );

    counter counter_inst(

        .i_clk(i_clk),
        .i_rstn(i_rstn),             //active low reset
        .i_read(i_read),             //signal to read data from the FIFO
        .i_empty(ow_empty),            //signal to indicate FIFO is empty

        .or_timetag(or_timetag)    //timetag for the read data, can be used to track the order of data
    
    );
endmodule

