import array as arr
def main():
   
	filename=input('Enter name of file\n')
	f1=open('new2.v','w')  
	f2=open('new2.py','a')
	f=open(filename,'r')
	f1.write('`include '+'"'+filename+'"'+'\n'+'module top;\n')
	count=0
	index=0
	for line in f:
		#print(line)
		flag=0
		inp=''
		if line.startswith('input'):
			
			#print(line)
			for x in line:
					if x!=';':
						inp=inp+x
					else:
						flag=1
						break
			if flag!=1:			
				for line in f:
					for x in line:
						if x!=';':
							inp=inp+x
						
						else:
							flag=1
					if flag==1:
						break
				
			j=inp.split(',')
			print(j)
			countin=len(j)
			print(len(j))
	bitsize=[]
	for i in range(0,len(j)):
		bitsize.append(1)
	print(bitsize)
	
	listinput=[]
	flag2=0
	for i in range(0,countin):
		m=str(j[i])
		tr=(m.split())
		if len(tr)>=1:
			flag2=1
	
		if tr[0]=='input':
			if flag2==0:
				listinput.append(tr[1])
			else:
				listinput.append(tr[2])
		else:
			listinput.append(tr[0])
	print(listinput)
	f.seek(0,0)
	flag3=0
	c=0
	for line in f:
		if line.startswith('input'):
			sr=line.split()
			k=str(sr[1])
			if k[0]=='[':
				flag3=1
				num1=int(k[1])
				print(num1)
				num2=int(k[3])
				print(num2)
				diff=num1-num2
			for x in line:
				
				
				
						
					
				
			
			
	
			
			
	'''f.seek(0,0)
	for line in f:	
		flag1=0
		out=''
		if line.startswith('output'):
			for x in line:
					if x!=';':
						out=out+x
					else:
						flag1=1
						break
			if flag1!=1:
						
				for line in f:
					for x in line:
						if x!=';':
							out=out+x
						
						else:
							flag1=1
						if flag1==1:
							break
					if flag1==1:
						break
				
			r=out.split(',')
			print(r)
			countout=len(r)
			print(len(r))
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			

	f.seek(0,0)
	for line in f:
		#print(line)
		flag=0
		inp=''
		if line.startswith('input'):
				f1.write(line.replace("input"," reg "))
				for x in line:
					if x==';':
						flag=1
						break
				if flag!=1:			
					for line in f:
						for x in line:
							if x!=';':
								f1.write(x)
						
							else:
								f1.write(';')
								flag=1
						if flag==1:
							break
	
	f.seek(0,0)
	for line in f:
		#print(line)
		flag=0
		inp=''
		if line.startswith('output'):
				f1.write(line.replace("output","wire"))
				for x in line:
					if x==';':
						flag=1
						break
				if flag!=1:			
					for line in f:
						for x in line:
							if x!=';':
								f1.write(x)
						
							else:
								f1.write(';')
								flag=1
						if flag==1:
							break
	f.seek(0,0)
	for line in f:
		flag=0
		
		if line.startswith('module'):
			line=line.replace('module','')
		
			f1.write(line.replace("("," m0(")+'\n')
			for line in f:
				if line.startswith('input'):
					break
				else:
				
					for x in line:
						if x!=';':
							f1.write(x)
						
						else:
							f1.write(';')
							flag=1
						if flag==1:
							break
	x=0
	f1.write('integer ')
	for x in range(0,countin):
		f1.write('i')
		f1.write(str(x))
		if x!=countin-1:
			f1.write(',')
	f1.write(';'+'\n')
	f1.write('initial'+'\n')
	f1.write('begin'+'\n')
	
	f.seek(0,0)
	listinput=[]
	for i in range(0,countin):
		m=str(j[i])
		tr=(m.split())
	
		if tr[0]=='input':
			listinput.append(tr[1])
		else:
			listinput.append(tr[0])
	i=0
	
	listoutput=[]
	for i in range(0,countout):
		m1=str(r[i])
		tr1=(m1.split())
	
		if tr1[0]=='output':
			listoutput.append(tr1[1])
		else:
			listoutput.append(tr1[0])
	
	
	#f1.write(";\n")
	x=0
	for x in range(0,len(listinput)):
		f1.write('for(i')
		f1.write(str(x))
		f1.write('=0;i')
		f1.write(str(x))
		f1.write('<=')
		f1.write('1')
		f1.write(';i')
		f1.write(str(x))
		f1.write('='+"i"+str(x)+"+ 1) begin \n")
		#f1.write('=+1) begin \n')
	f1.write('#5 ')
	x=0
	for x in range(len(listinput)):
		f1.write(listinput[x]+'='+'i'+str(x)+';  ');
	
	f1.write('\n')	
	x=0
	for x in range(0,len(listinput)):
		f1.write("end\n")	
	#f1.write("endgenerate\n\n")	
	f1.write("end\n")
	f1.write("initial\n")
	f1.write("begin\n")
	f1.write("$monitor ($time,"+"\" ")
	for x in range(0,len(listinput)):
		f1.write(listinput[x]+"=%d")
		#if x!=len(listinput)-1:
		f1.write(",")
	x=0
	for x in range(0,len(listoutput)):
		f1.write(listoutput[x]+"=%d")
		if x!=len(listoutput)-1:
			f1.write(",")
	
	
	f1.write("\""+",")
	for x in range(0,len(listinput)):
		f1.write(listinput[x])
		#if x!=len(listinput)-1:
		f1.write(",")
	f1.write("		")
	for x in range(0,len(listoutput)):
		f1.write(listoutput[x])
		if x!=len(listoutput)-1:
			f1.write(",")
	
			
	f1.write(")")
	f1.write(";")
	f1.write("\n end")
	
		
	
	
	
		
	
	f1.write("\nendmodule\n")'''
		
		
	
	
			
	
	
				
				
			
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
			
			
	
	
		
	f.close()
	f1.close()
	
	
if __name__== "__main__":
  main()
