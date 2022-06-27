`include "fulladder4.v"
module adder8(A, B, C, sum, carry);
	input[7:0] A, 
B;	
	input C;
	output[7:0] sum;
	output carry;
	wire W0;
	adder4 FBA_0(A[3:0], B[3:0], C, sum[3:0], W0);
	adder4 FBA_1(A[7:4], B[7:4], W0, sum[7:4], carry);
endmodule

