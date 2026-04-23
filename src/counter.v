`default_nettype none

module counter (

    input wire i_clk,
    input wire i_rstn,             //active low reset
    input wire i_read,             //signal to read data from the FIFO
    input wire i_empty,            //signal to indicate FIFO is empty

    output reg [3:0] or_timetag    //timetag for the read data, can be used to track the order of data
  
);

    always @(posedge i_clk) begin
        if(!i_rstn) begin
            or_timetag <= '0;
        end else begin

            if(i_read && !i_empty) begin
                or_timetag[2:0] <= or_timetag[2:0] + 1'b1;
            end

            or_timetag[3] <= 1'b0;
        end
    end
endmodule
