`include "wallace16b.v"

module top;
reg [15:0] A,B;
wire [31:0] res;
wallace16b m0(A,B,res);
initial begin
	if($value$plusargs("a=%d",A));
	if($value$plusargs("b=%d",B));
	#5;
	$display("res=%d",res);
end
endmodule

