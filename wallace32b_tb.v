`include "wallace32b.v"

module top;
reg [31:0] A,B;
wire [63:0] res;
wallace32b m0(A,B,res);
initial begin
	if($value$plusargs("a=%d",A));
	if($value$plusargs("b=%d",B));
	#20;
	$display("res=%d",res);
end
endmodule

