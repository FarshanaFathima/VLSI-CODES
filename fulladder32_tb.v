`include "fulladder32.v"

module top;
reg [31:0] A,B;
reg C;
wire [31:0] res;
wire carry;
adder32 m0 (A,B,C,res,carry);
initial begin
	if($value$plusargs("a=%d",A));
	if($value$plusargs("b=%d",B));
	if($value$plusargs("c=%d",C));
	#5;
	$display("res=%d",res);
end
endmodule