`include "fulladder.v"
module adder4(A, B, C, sum, carry);
	input [3:0] A, B;	
	input C;
	output [3:0] sum;
	output carry;
	wire W0, W1, W2;
	fulladder FA_0(A[0], B[0], C, sum[0], W0);
	fulladder FA_1(A[1], B[1], W0, sum[1], W1);
	fulladder FA_2(A[2], B[2], W1, sum[2], W2);
	fulladder FA_3(A[3], B[3], W2, sum[3], carry);
endmodule

