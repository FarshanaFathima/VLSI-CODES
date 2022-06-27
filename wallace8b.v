module wallace(a, b, q);

input [8:1] a, b;					//input and output
wire [15:1] p1, p2, p3, p4, p5, p6, p7, p8;						//intermediate wires-partial products
wire [15:1] s1, s2, s3, s4, s5, s6, c1, c2, c3, c4, c5;				//s-sum, c-carry
wire [16:1] c6;
wire car, car1, car2, car3, car4, car5, car6, car7, car8;
output [16:1] q;
wire carry;

		
assign p1[8:1]=b & {8{a[1]}};		//finding partial products
assign p1[15:9]=7'b0;

assign p2[1]=1'b0;							
assign p2[9:2]=b & {8{a[2]}};
assign p2[15:10]=6'b0;

assign p3[2:1]=2'b0;							
assign p3[10:3]=b & {8{a[3]}};
assign p3[15:11]=5'b0;

assign p4[3:1]=3'b0;			
assign p4[11:4]=b & {8{a[4]}};
assign p4[15:12]=4'b0;
						
assign p5[4:1]=4'b0;
assign p5[12:5]=b & {8{a[5]}};
assign p5[15:13]=3'b0;
					
assign p6[5:1]=5'b0;
assign p6[13:6]=b & {8{a[6]}};
assign p6[15:14]=2'b0;
						
assign p7[6:1]=6'b0;
assign p7[14:7]=b & {8{a[7]}};
assign p7[15]=1'b0;
					
assign p8[7:1]=7'b0;
assign p8[15:8]=b & {8{a[8]}};

/*
always begin
	$display("p1: %b", p1);
	$display("p2: %b", p2);
	$display("p3: %b", p3);
	$display("p4: %b", p4);
	$display("p5: %b", p5);
	$display("p6: %b", p6);
	$display("p7: %b", p7);
	$display("p8: %b", p8);
	end
*/

assign c1[1]=0;
assign c1[2]=0;														//sum1, carry1
	
assign s1[1]=p1[1];
	
assign s1[2]=p1[2]^p2[2];
assign c1[3]=p1[2]&p2[2];

assign s1[3]=(p1[3]^p2[3])^p3[3];
assign c1[4]=(p1[3]&p2[3]) || (p2[3]&p3[3]) || (p3[3]&p1[3]);

assign s1[4]=(p1[4]^p2[4])^p3[4];
assign c1[5]=(p1[4]&p2[4]) || (p2[4]&p3[4]) || (p3[4]&p1[4]);

assign s1[5]=(p1[5]^p2[5])^p3[5];
assign c1[6]=(p1[5]&p2[5]) || (p2[5]&p3[5]) || (p3[5]&p1[5]);

assign s1[6]=(p1[6]^p2[6])^p3[6];
assign c1[7]=(p1[6]&p2[6]) || (p2[6]&p3[6]) || (p3[6]&p1[6]);

assign s1[7]=(p1[7]^p2[7])^p3[7];
assign c1[8]=(p1[7]&p2[7]) || (p2[7]&p3[7]) || (p3[7]&p1[7]);

assign s1[8]=(p1[8]^p2[8])^p3[8];
assign c1[9]=(p1[8]&p2[8]) || (p2[8]&p3[8]) || (p3[8]&p1[8]);

assign s1[9]=(p1[9]^p2[9])^p3[9];
assign c1[10]=(p1[9]&p2[9]) || (p2[9]&p3[9]) || (p3[9]&p1[9]);

assign s1[10]=(p1[10]^p2[10])^p3[10];
assign c1[11]=(p1[10]&p2[10]) || (p2[10]&p3[10]) || (p3[10]&p1[10]);

assign s1[15:11]=5'b0;
assign c1[15:12]=4'b0;


assign s2[1]=0;														//sum2, carry2
assign s2[2]=0;
assign s2[3]=0;
assign c2[1]=0;
assign c2[2]=0;
assign c2[3]=0;
assign c2[4]=0;
assign c2[5]=0;

assign s2[4]=p4[4];

assign s2[5]=p4[5]^p5[5];
assign c2[6]=p4[5]&p5[5];

assign s2[6]=(p4[6]^p5[6])^p6[6];
assign c2[7]=(p4[6]&p5[6]) || (p5[6]&p6[6]) || (p6[6]&p4[6]);

assign s2[7]=(p4[7]^p5[7])^p6[7];
assign c2[8]=(p4[7]&p5[7]) || (p5[7]&p6[7]) || (p6[7]&p4[7]);

assign s2[8]=(p4[8]^p5[8])^p6[8];
assign c2[9]=(p4[8]&p5[8]) || (p5[8]&p6[8]) || (p6[8]&p4[8]);

assign s2[9]=(p4[9]^p5[9])^p6[9];
assign c2[10]=(p4[9]&p5[9]) || (p5[9]&p6[9]) || (p6[9]&p4[9]);

assign s2[10]=(p4[10]^p5[10])^p6[10];
assign c2[11]=(p4[10]&p5[10]) || (p5[10]&p6[10]) || (p6[10]&p4[10]);

assign s2[11]=(p4[11]^p5[11])^p6[11];
assign c2[12]=(p4[11]&p5[11]) || (p5[11]&p6[11]) || (p6[11]&p4[11]);

assign s2[12]=(p4[12]^p5[12])^p6[12];
assign c2[13]=(p4[12]&p5[12]) || (p5[12]&p6[12]) || (p6[12]&p4[12]);

assign s2[13]=(p4[13]^p5[13])^p6[13];
assign c2[14]=(p4[13]&p5[13]) || (p5[13]&p6[13]) || (p6[13]&p4[13]);

assign s2[15:14]=2'b0;
assign c2[15]=0;


assign s3[1]=s1[1];														//sum3, carry3
assign s3[2]=s1[2];
assign c3[1]=0;
assign c3[2]=0;
assign c3[3]=0;

assign s3[3]=s1[3]^c1[3];
assign c3[4]=s1[3]&c1[3];

assign s3[4]=(s1[4]^c1[4])^s2[4];
assign c3[5]=(s1[4]&c1[4]) || (c1[4]&s2[4]) || (s2[4]&s1[4]);

assign s3[5]=(s1[5]^c1[5])^s2[5];
assign c3[6]=(s1[5]&c1[5]) || (c1[5]&s2[5]) || (s2[5]&s1[5]);

assign s3[6]=(s1[6]^c1[6])^s2[6];
assign c3[7]=(s1[6]&c1[6]) || (c1[6]&s2[6]) || (s2[6]&s1[6]);

assign s3[7]=(s1[7]^c1[7])^s2[7];
assign c3[8]=(s1[7]&c1[7]) || (c1[7]&s2[7]) || (s2[7]&s1[7]);

assign s3[8]=(s1[8]^c1[8])^s2[8];
assign c3[9]=(s1[8]&c1[8]) || (c1[8]&s2[8]) || (s2[8]&s1[8]);

assign s3[9]=(s1[9]^c1[9])^s2[9];
assign c3[10]=(s1[9]&c1[9]) || (c1[9]&s2[9]) || (s2[9]&s1[9]);

assign s3[10]=(s1[10]^c1[10])^s2[10];
assign c3[11]=(s1[10]&c1[10]) || (c1[10]&s2[10]) || (s2[10]&s1[10]);

assign s3[11]=(s1[11]^c1[11])^s2[11];
assign c3[12]=(s1[11]&c1[11]) || (c1[11]&s2[11]) || (s2[11]&s1[11]);

assign s3[12]=(s1[12]^c1[12])^s2[12];
assign c3[13]=(s1[12]&c1[12]) || (c1[12]&s2[12]) || (s2[12]&s1[12]);

assign s3[13]=(s1[13]^c1[13])^s2[13];
assign c3[14]=(s1[13]&c1[13]) || (c1[13]&s2[13]) || (s2[13]&s1[13]);

assign s3[15:14]=2'b0;
assign c3[15]=0;


assign s4[1]=0;														//sum4, carry4
assign s4[2]=0;
assign s4[3]=0;
assign s4[4]=0;
assign s4[5]=0;
assign c4[1]=0;
assign c4[2]=0;
assign c4[3]=0;
assign c4[4]=0;
assign c4[5]=0;
assign c4[6]=0;
assign c4[7]=0;

assign s4[6]=c2[6];
assign s4[7]=c2[7]^p7[7];
assign c4[8]=c2[7]&p7[7];

assign s4[8]=c2[8]^p7[8]^p8[8];
assign c4[9]=(c2[8]&p7[8]) || (p7[8]&p8[8]) || (p8[8]&c2[8]);

assign s4[9]=(c2[9]^p7[9])^p8[9];
assign c4[10]=(c2[9]&p7[9]) || (p7[9]&p8[9]) || (p8[9]&c2[9]);

assign s4[10]=(c2[10]^p7[10])^p8[10];
assign c4[11]=(c2[10]&p7[10]) || (p7[10]&p8[10]) || (p8[10]&c2[10]);

assign s4[11]=(c2[11]^p7[11])^p8[11];
assign c4[12]=(c2[11]&p7[11]) || (p7[11]&p8[11]) || (p8[11]&c2[11]);

assign s4[12]=(c2[12]^p7[12])^p8[12];
assign c4[13]=(c2[12]&p7[12]) || (p7[12]&p8[12]) || (p8[12]&c2[12]);

assign s4[13]=(c2[13]^p7[13])^p8[13];
assign c4[14]=(c2[13]&p7[13]) || (p7[13]&p8[13]) || (p8[13]&c2[13]);

assign s4[14]=(c2[14]^p7[14])^p8[14];
assign c4[15]=(c2[14]&p7[14]) || (p7[14]&p8[14]) || (p8[14]&c2[14]);

assign s4[15]=(c2[15]^p7[15])^p8[15];


assign c5[1]=0;											//sum5, carry5
assign c5[2]=0;
assign c5[3]=0;
assign c5[4]=0;												
	
assign s5[1]=s3[1];
assign s5[2]=s3[2];
assign s5[3]=s3[3];
	
assign s5[4]=s3[4]^c3[4];
assign c5[5]=s3[4]&c3[4];

assign s5[5]=(s3[5]^c3[5])^s4[5];
assign c5[6]=(s3[5]&c3[5]) || (c3[5]&s4[5]) || (s4[5]&s3[5]);

assign s5[5]=(s3[5]^c3[5])^s4[5];
assign c5[6]=(s3[5]&c3[5]) || (c3[5]&s4[5]) || (s4[5]&s3[5]);

assign s5[6]=(s3[6]^c3[6])^s4[6];
assign c5[7]=(s3[6]&c3[6]) || (c3[6]&s4[6]) || (s4[6]&s3[6]);

assign s5[7]=(s3[7]^c3[7])^s4[7];
assign c5[8]=(s3[7]&c3[7]) || (c3[7]&s4[7]) || (s4[7]&s3[7]);

assign s5[8]=(s3[8]^c3[8])^s4[8];
assign c5[9]=(s3[8]&c3[8]) || (c3[8]&s4[8]) || (s4[8]&s3[8]);

assign s5[9]=(s3[9]^c3[9])^s4[9];
assign c5[10]=(s3[9]&c3[9]) || (c3[9]&s4[9]) || (s4[9]&s3[9]);

assign s5[10]=(s3[10]^c3[10])^s4[10];
assign c5[11]=(s3[10]&c3[10]) || (c3[10]&s4[10]) || (s4[10]&s3[10]);

assign s5[11]=(s3[11]^c3[11])^s4[11];
assign c5[12]=(s3[11]&c3[11]) || (c3[11]&s4[11]) || (s4[11]&s3[11]);

assign s5[12]=(s3[12]^c3[12])^s4[12];
assign c5[13]=(s3[12]&c3[12]) || (c3[12]&s4[12]) || (s4[12]&s3[12]);

assign s5[13]=(s3[13]^c3[13])^s4[13];
assign c5[14]=(s3[13]&c3[13]) || (c3[13]&s4[13]) || (s4[13]&s3[13]);

assign s5[14]=(s3[14]^c3[14])^s4[14];
assign c5[15]=(s3[14]&c3[14]) || (c3[14]&s4[14]) || (s4[14]&s3[14]);

assign s5[15]=s4[15];


assign c6[1]=0;											//sum6, carry6
assign c6[2]=0;
assign c6[3]=0;
assign c6[4]=0;	
assign c6[5]=0;												
	
assign s6[1]=s5[1];
assign s6[2]=s5[2];
assign s6[3]=s5[3];
assign s6[4]=s5[4];
	
assign s6[5]=s5[5]^c5[5];
assign c6[6]=s5[5]&c5[5];

assign s6[6]=(s5[6]^c5[6])^c4[6];
assign c6[7]=(s5[6]&c5[6]) || (c5[6]&c4[6]) || (c4[6]&s5[6]);

assign s6[7]=(s5[7]^c5[7])^c4[7];
assign c6[8]=(s5[7]&c5[7]) || (c5[7]&c4[7]) || (c4[7]&s5[7]);

assign s6[8]=(s5[8]^c5[8])^c4[8];
assign c6[9]=(s5[8]&c5[8]) || (c5[8]&c4[8]) || (c4[8]&s5[8]);

assign s6[9]=(s5[9]^c5[9])^c4[9];
assign c6[10]=(s5[9]&c5[9]) || (c5[9]&c4[9]) || (c4[9]&s5[9]);

assign s6[10]=(s5[10]^c5[10])^c4[10];
assign c6[11]=(s5[10]&c5[10]) || (c5[10]&c4[10]) || (c4[10]&s5[10]);

assign s6[11]=(s5[11]^c5[11])^c4[11];
assign c6[12]=(s5[11]&c5[11]) || (c5[11]&c4[11]) || (c4[11]&s5[11]);

assign s6[12]=(s5[12]^c5[12])^c4[12];
assign c6[13]=(s5[12]&c5[12]) || (c5[12]&c4[12]) || (c4[12]&s5[12]);

assign s6[13]=(s5[13]^c5[13])^c4[13];
assign c6[14]=(s5[13]&c5[13]) || (c5[13]&c4[13]) || (c4[13]&s5[13]);

assign s6[14]=(s5[14]^c5[14])^c4[14];
assign c6[15]=(s5[14]&c5[14]) || (c5[14]&c4[14]) || (c4[14]&s5[14]);

assign s6[15]=s5[15]^c4[15];
assign c6[16]=s5[15]&c4[15];


assign q[1]=s6[1];											//sum6, carry6
assign q[2]=s6[2];
assign q[3]=s6[3];
assign q[4]=s6[4];												
assign q[5]=s6[5];	
	
assign q[6]=s6[6]^c6[6];
assign car=s6[6]&c6[6];

assign q[7]=s6[7]^c6[7]^car;
assign car1=(s6[7]&c6[7]) || (c6[7]&car) || (car&s6[7]);

assign q[8]=s6[8]^c6[8]^car1;
assign car2=(s6[8]&c6[8]) || (c6[8]&car1) || (car1&s6[8]);

assign q[9]=s6[9]^c6[9]^car2;
assign car3=(s6[9]&c6[9]) || (c6[9]&car2) || (car2&s6[9]);

assign q[10]=s6[10]^c6[10]^car3;
assign car4=(s6[10]&c6[10]) || (c6[10]&car3) || (car3&s6[10]);

assign q[11]=s6[11]^c6[11]^car4;
assign car5=(s6[11]&c6[11]) || (c6[11]&car4) || (car4&s6[11]);

assign q[12]=s6[12]^c6[12]^car5;
assign car6=(s6[12]&c6[12]) || (c6[12]&car5) || (car5&s6[12]);

assign q[13]=s6[13]^c6[13]^car6;
assign car7=(s6[13]&c6[13]) || (c6[13]&car6) || (car6&s6[13]);

assign q[14]=s6[14]^c6[14]^car7;
assign car8=(s6[14]&c6[14]) || (c6[14]&car7) || (car7&s6[14]);

assign q[15]=s6[15]^c6[15]^car8;
assign q[16]=c6[16];


endmodule
