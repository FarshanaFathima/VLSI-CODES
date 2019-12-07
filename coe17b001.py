

from collections import OrderedDict 
  

def main():
	output_variables=[]
	output=''
	flag=0
	filename=input('Enter name of file\n')
	verilogfile=open(filename,'r')
	if flag!=1:
		for line in verilogfile:
			flag=0
			inp=''
			if line.startswith('output'):
				for character in line:
					#print(character)
					if character==';':
						flag=1
						break
					else:
						if character!=' ':
							output=output+character
				output=output.strip('output')
				output=output.strip('\n')
				output=output.strip(' ')
				if flag!=1:
					for line in verilogfile:
						for character in line:
							if character!=';':
								output=output+character
							else:
								flag=1
								break
						if flag==1:
							break
	output_variables=output.split(',')
	output_var=[]
	for i in output_variables:
		i=str(i)
		i=i.replace(' ','')
		i=i.replace('\n','')
		output_var.append(i)
	print('OUTPUT')
	print(output_var)
	wire=''
	wire_variables=[]
	verilogfile.seek(0,0)
	flag=0
	if flag!=1:
		for line in verilogfile:
			if line.startswith('wire') or line.startswith(' wire') :
				for character in line:
					if character==';':
						flag=1
						break
					else:
						if character!=' ':
							wire=wire+character
				wire=wire.strip('wire')
				wire=wire.strip('\n')
				wire=wire.strip(' ')

				if flag!=1:
					for line in verilogfile:
						for character in line:
							if character!=';':
								if character!='\n':
									wire=wire+character
							else:
								flag=1
								break
						if flag==1:
							break
	wire_variables=wire.split(',')
	wires=[]
	wiredictionary=OrderedDict()
	for i in wire_variables:
		i=str(i)
		i=i.replace(' ','')
		i=i.replace('\n','')
		wiredictionary[i]=0
		wires.append(i)
	print('WIRES')
	print(wires)



	in1=''
	in1_variables=[]
	verilogfile.seek(0,0)
	flag=0
	if flag!=1:
		for line in verilogfile:
			if line.startswith('input') or line.startswith(' input') :
				for character in line:
					if character==';':
						flag=1
						break
					else:
						if character!=' ':
							in1=in1+character
				in1=in1.strip('input')
				in1=in1.strip('\n')
				in1=in1.strip(' ')

				if flag!=1:
					for line in verilogfile:
						for character in line:
							if character!=';':
								if character!='\n':
									in1=in1+character
							else:
								flag=1
								break
						if flag==1:
							break

	value=OrderedDict()
	in1_variables=in1.split(',')
	input_init=[]
	print('INPUT')
	for i in in1_variables:
		i=str(i)
		i=i.replace(' ','')
		i=i.replace('\n','')
		value[i]=0.5
		print(i,value[i])
		input_init.append(i)
	
	

	for i in wires:
		value[i]=1

	mainlist=wires
	for i in output_var:
		mainlist.append(i)

	print(mainlist)
	sublist=wires
	for i in input_init:
		mainlist.append(i)

	value1=OrderedDict()
	value2=OrderedDict()
	print(value)
	verilogfile.seek(0,0)
	for line in verilogfile:
		m=[]
		if line.startswith('nand') or line.startswith('	nand')	:
			start=line.find('(',0,len(line)-1)
			end=line.find(')',0,len(line)-1)
			sub=line[start+1:end]
			sub=sub.replace(" ","")
			m=sub.split(',')
			j=m[0]
			m.remove(j)
			value1[str(j)]=m
			mul=1
			for r in m:
				mul=mul * value[r]
			value[str(j)]=1-mul
			value2[str(j)]=1-mul
	#verilogfile.seek(0,0)
	#for line in verilogfile:
		elif  line.startswith('and') or line.startswith(' and') :
			start=line.find('(',0,len(line)-1)
			end=line.find(')',0,len(line)-1)
			sub=line[start+1:end]
			sub=sub.replace(" ","")
			m=sub.split(',')
			j=m[0]
			m.remove(j)
			value1[str(j)]=m
			mul=1
			for r in m:
				mul=mul * value[r]
			value[str(j)]=mul
			value2[str(j)]=mul
	#verilogfile.seek(0,0)
	#for line in verilogfile:
		elif line.startswith('or') or line.startswith(' or'):
			start=line.find('(',0,len(line)-1)
			end=line.find(')',0,len(line)-1)
			sub=line[start+1:end]
			sub=sub.replace(" ","")
			m=sub.split(',')
			j=m[0]
			m.remove(j)
			value1[str(j)]=m
			mul=1
			for r in m:
				mul=mul *(1- value[r])
			value[str(j)]=1-mul
			value2[str(j)]=1-mul
	#verilogfile.seek(0,0)
	#for line in verilogfile:
		elif line.startswith('nor') or line.startswith(' nor'):
			start=line.find('(',0,len(line)-1)
			end=line.find(')',0,len(line)-1)
			sub=line[start+1:end]
			sub=sub.replace(" ","")
			m=sub.split(',')
			j=m[0]
			m.remove(j)
			value1[str(j)]=m
			mul=1
			for r in m:
				mul=mul *(1- value[r])
			value[str(j)]=mul
			value2[str(j)]=mul
	#verilogfile.seek(0,0)
	#for line in verilogfile:
		elif line.startswith('xor') or line.startswith(' xor'):
			print('m')
			start=line.find('(',0,len(line)-1)
			end=line.find(')',0,len(line)-1)
			sub=line[start+1:end]
			sub=sub.replace(" ","")
			print(sub)
			m=sub.split(',')

			j=m[0]
			print(j)
			m.remove(j)
			value1[str(j)]=m
			mul=1
			sum1=0
			for r in m:
				mul=mul *(value[r])
				sum1+=value[r]

			value[str(j)]=sum1+(mul*2*-1)
			value2[str(j)]=sum1+(mul*2*-1)
	#verilogfile.seek(0,0)
	#for line in verilogfile:
		elif line.startswith('not') or line.startswith(' not'):
			start=line.find('(',0,len(line)-1)
			end=line.find(')',0,len(line)-1)
			sub=line[start+1:end]
			sub=sub.replace(" ","")
			m=sub.split(',')
			j=m[0]
			m.remove(j)
			value1[str(j)]=m
			mul=1
			sum1=0
			for r in m:
				value[str(j)]=1-value[r]
				value2[str(j)]=1-value[r]
			



	'''verilogfile.seek(0,0)
	for line in verilogfile:
		if 'or' in line:
			start=line.find('(',0,len(line)-1)
			end=line.find(')',0,len(line)-1)
			sub=line[start+1:end]
			m=sub.split(',')
			j=m[0]
			m.remove(j)
			value1[str(j)]=m
			mul=1
			for r in m:
				mul=mul * (1-value[r])
			value[str(j)]=1-mul
			value2[str(j)]=1-mul'''

		

			#print(m)     #now chec
	'''
	for i in value1.keys():
		list1=value1[i]
		print(list1)
		mul=1
		for j in list1:
			#print(j,value[j])
			mul=mul * value[j]
		print(1-mul)
		value[i]=1-mul
		value2[i]=1-mul'''

	'''value3=OrderedDict()
	verilogfile.seek(0,0)
	for line in verilogfile:
		m=[]
		if 'and' in line:
			start=line.find('(',0,len(line)-1)
			end=line.find(')',0,len(line)-1)
			sub=line[start+1:end]
			m=sub.split(',')
			j=m[0]
			m.remove(j)
			value3[str(j)]=m
			#print(m)     #now chec
	
	for i in value3.keys():
		list1=value3[i]
		print(list1)
		mul=1
		for j in list1:
			#print(j,value[j])
			mul=mul * value[j]
		value[i]=mul
		value2[i]=mul'''











	for i in value2.keys():
		#print(i,value2[i])
		print("Activity factor of "+str(i)+" is "+ str(value2[i]*(1-value2[i])))









		




main()
