`include "fulladder16.v"
module adder32(A, B, C, sum, carry);
	input[31:0] A, B;	
	input C;
	output[31:0] sum;
	output carry;
	wire W0;
	adder16 EBA_0(A[15:0], B[15:0], C, sum[15:0], W0);
	adder16 EBA_1(A[31:16], B[31:16], W0, sum[31:16], carry);
endmodule

