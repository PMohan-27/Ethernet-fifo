`default_nettype none

module memory (

    input wire i_clk,
    input wire i_rstn,             //active low reset
    input wire i_write,            //signal to write data into the FIFO
    input wire [7:0] iw_data,      //data to be written into the FIFO  
    input wire i_read,             //signal to read data from the FIFO

    output reg [7:0] ow_data,      //data read from the FIFO
    output reg ow_empty,           //signal to indicate FIFO is empty
    output reg ow_full             //signal to indicate FIFO is full
);

    reg [7:0] mem [0:63];
    reg [6:0] w_ptr, r_ptr;

    assign ow_empty = (w_ptr == r_ptr);
    assign ow_full = (w_ptr[5:0] == r_ptr[5:0]) && (w_ptr[6] != r_ptr[6]);
    always @(posedge i_clk) begin
        if(!i_rstn) begin
            ow_data <= '0;
            // ow_empty <= 1'b1;
            // ow_full <= '0;

            w_ptr <= '0;
            r_ptr <= '0;
        end else begin
            if(i_write && !ow_full) begin
                mem[w_ptr[5:0]] <= iw_data;
                w_ptr <= w_ptr + 7'd1;
            end

            if(i_read && !ow_empty) begin
                ow_data <= mem[r_ptr[5:0]];
                r_ptr <= r_ptr + 7'd1;
            end
        end
    end
endmodule

