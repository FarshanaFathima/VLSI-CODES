`include "fulladder32.v"
module adder64(A, B, C, sum, carry);
	input[63:0] A, B;	
	input C;
	output[63:0] sum;
	output carry;
	wire W0;
	adder32 EBA_0(A[31:0], B[31:0], C, sum[31:0], W0);
	adder32 EBA_1(A[63:32], B[63:32], W0, sum[63:32], carry);
endmodule

