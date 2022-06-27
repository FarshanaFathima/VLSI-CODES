`include "wallace16b.v"

module wallace32b(A, B, prod);
input [31:0] A,B;
output [63:0] prod;
wire [63:0] p0, p1, p2, p3, sum0, sum1;
wire carry0, carry1, c;

wallace16b m0(A[15:0], B[15:0], p0[31:0]);
wallace16b m1(A[31:16], B[15:0], p1[47:16]);
wallace16b m2(A[15:0], B[31:16], p2[47:16]);
wallace16b m3(A[31:16], B[31:16], p3[63:32]);

assign p1[15:0] = 16'd0;
assign p2[15:0] = 16'd0;
assign p3[31:0] = 32'd0;

assign p1[63:48] = 16'd0;
assign p2[63:48] = 16'd0;
assign p0[63:32] = 32'd0;

adder64 t1(p0, p1, 1'b0, sum0, carry0);
adder64 t2(sum0, p2, carry0, sum1, carry1);
adder64 t3(sum1, p3, carry1, prod, c);

endmodule

