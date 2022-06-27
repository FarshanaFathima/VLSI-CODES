`include "fulladder8.v"
module adder16(A, B, C, sum, carry);
	input[15:0] A, B;	
	input C;
	output[15:0] sum;
	output carry;
	wire W0;
	adder8 EBA_0(A[7:0], B[7:0], C, sum[7:0], W0);
	adder8 EBA_1(A[15:8], B[15:8], W0, sum[15:8], carry);
endmodule

