`include "fulladder16.v"

module top;
reg [15:0] A,B;
reg C;
wire [15:0] res;
wire carry;
adder16 m0 (A,B,C,res,carry);
initial begin
	if($value$plusargs("a=%d",A));
	if($value$plusargs("b=%d",B));
	if($value$plusargs("c=%d",C));
	#5;
	$display("res=%d",res);
end
endmodule