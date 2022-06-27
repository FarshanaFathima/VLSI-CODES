`include "wallace8b.v"
`include "fulladder64.v"

module wallace16b(A, B, prod);
input [15:0] A,B;
output [31:0] prod;
wire [31:0] p0, p1, p2, p3, sum0, sum1;
wire carry0, carry1, c;

wallace m0(A[7:0], B[7:0], p0[15:0]);
wallace m1(A[15:8], B[7:0], p1[23:8]);
wallace m2(A[7:0], B[15:8], p2[23:8]);
wallace m3(A[15:8], B[15:8], p3[31:16]);

assign p1[7:0] = 8'd0;
assign p2[7:0] = 8'd0;
assign p3[15:0] = 16'd0;

assign p1[31:24] = 8'd0;
assign p2[31:24] = 8'd0;
assign p0[31:16] = 16'd0;

adder32 t1(p0, p1, 1'b0, sum0, carry0);
adder32 t2(sum0, p2, carry0, sum1, carry1);
adder32 t3(sum1, p3, carry1, prod, c);

endmodule
