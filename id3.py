###############################################################################
################----------ID3 ALGORITHM-----------#############################
###############################################################################

import subprocess
import math
import xlrd 
from itertools import groupby
from xlwt import Workbook 
from anytree import Node, RenderTree

###############################################################################
###############-----------VERILOG CODE------------#############################
###############################################################################

############################################################################################################################
#definition of adder
############################################################################################################################
def adder(a,b):
	k=convert(a)
	l=convert(b)
	aq="a="+str(k)
	bq=" +b="+str(l)
	x="./fulladder32_tb +"+aq+" +"+bq+" +c=0"
	s=subprocess.check_output(x,shell=True)
	y=str(s).strip("b\'res=    ")
	y=y.strip("\\n")
	y=reconverta(y)
	return float(y)
############################################################################################################################
#definition of multiplier
############################################################################################################################
def multi(a,b):
	k=convert(a)
	l=convert(b)
	aq="a="+str(k)
	bq=" +b="+str(l)
	x="./wallace32b_tb +"+aq+" +"+bq
	s=subprocess.check_output(x,shell=True)
	y=str(s).strip("b\'res=    ")
	y=y.strip("\\n")
	y=reconvertm(y)
	return float(y)
############################################################################################################################
#CONVERTION OF INTEGER TO FLOATING POINT-ADDER
############################################################################################################################
def reconverta(a):
	ch=''
	k=str(a)
	for i in range(0,len(k)-8):
		ch=ch+k[i]
	ch=ch+'.'
	for i in range(len(k)-8,len(k)):
		ch=ch+k[i]
	return str(ch)

############################################################################################################################
#CONVERTION OF INTEGER TO FLOATING POINT-MULTIPLIER
############################################################################################################################
def reconvertm(a):
	ch=''
	k=str(a)
	for i in range(0,len(k)-16):
		ch=ch+k[i]
	ch=ch+'.'
	for i in range(len(k)-16,len(k)):
		ch=ch+k[i]
	return str(ch)

############################################################################################################################
#CONVERTION OF FLOATING POINT TO INTEGER
############################################################################################################################
def convert(a):
	a=round(a,8)
	j=0
	y=str(a)
	number=''
	k=0;
	for j in range(len(y)):
		k=k+1
		if(y[j]!='.'):
			number=number+y[j]
		else:
			k=0
	if(k<8):
		for i in range(k,8):
			number=number+'0'
	return str(number)

###############################################################################
###############-------------MAIN CODE------------##############################
###############################################################################

global Maxi
global nodes_dic
nodes_dic={}
Maxi=0
selected_attr=[]
selected_index=[]

############################################################################################################################
###Counting the no of labels of the Final Attribute Value to be predicted
############################################################################################################################
def countfinal(l):
	labels=["bus","car","train"]
	counter=[]
	for j in labels:
		count1=l.count(j)
		counter.append(count1)
	return counter

############################################################################################################################
##FUNCTION TO FIND ENTROPY
############################################################################################################################
def entropy(attr_countresult):
	s=float(0)
	div=0
	for i in attr_countresult:
		k1=0
		div=i/float(sum(attr_countresult))
		if div!=0:
			lg=float(math.log(div,2))
			k1=abs(lg)
		if(div!=0 and k1!=0): 
			y1=float(multi(div,k1))
			s=adder(s,y1) #############################ADDER IMPLEMENTATION 1
		else:
			y1=float(0)
			s=s
	return s

########################################################################################
###########3--------FUNCTION TO FIND INFORMATION GAIN(ROOT NODE)-------#################
########################################################################################
def IG(attr,attr_count,path,i):
	loc=(path)
	wb1 = xlrd.open_workbook(loc) 
	sheet = wb.sheet_by_index(i) 
	print("------------------------------------------------------------")
	attr_entropy=0
	attr_column=[]
	
########################################################################################
#GETTING THE column OF PARTICULAR ATTRIBUTE
########################################################################################
	for i in range(1,sheet.nrows): 
		if attr_count==1:
			attr_column.append(int(sheet.cell_value(i,attr_count)))
		else:
			attr_column.append(str(sheet.cell_value(i,attr_count)))
	r=list(set(attr_column))
	r.sort()
	for i in r:
		print (i)
########################################################################################
#BUSCOUNT CARCOUNT TRAINCOUNT
########################################################################################
		attr_countresult=[0,0,0] 
		for j in range(1,sheet.nrows):
			if attr_count==1:
				cell= int(sheet.cell_value(j,attr_count))
			else:
				cell= str(sheet.cell_value(j,attr_count))
			if i==cell:
				if str(sheet.cell_value(j,sheet.ncols-1))=="bus":
					attr_countresult[0]=attr_countresult[0]+1
				elif str(sheet.cell_value(j,sheet.ncols-1))=="car":
					attr_countresult[1]=attr_countresult[1]+1
				elif str(sheet.cell_value(j,sheet.ncols-1))=="train":
					attr_countresult[2]=attr_countresult[2]+1
					
########################################################################################
######INFORMATION GAIN FOR attr_entropy  CALCULATION STARTS HERE
######CALLING ENTROPY FUNCTION TO CALCULATE ENTROPY OF EACH SUBSET OF THE ATTRIBUTE	
########################################################################################
		en=entropy(attr_countresult)
		Prob=sum(attr_countresult)/float(sheet.nrows-1)
		print("Entropy:",en,"\n")
########################################################################################
#attr_entropy-ATTRIBUTE TOTAL ENTROPY----ADDER IMPLEMENTATION_2 MULTI_IMPLEMENTATION 1##
########################################################################################
		if(Prob!=0.0 and en!=0.0):
			attr_entropy=adder(attr_entropy,float(multi(Prob,en)))
########################################################################################
	InfoGain=MainEntropy-attr_entropy
	print("Information gain of ",attr,InfoGain)
	return InfoGain
########################################################################################
#############---------------INFO GAIN IS OBTAINED HERE-------------------###############
########################################################################################			


########################################################################################
##########----------------------FINDING INFO GAIN OF ALL NODES----------------##########
########################################################################################
#LOCATION OF FILE
########################################################################################

loc = ("Dataset1.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
#STORE THE ATTRIBUTES
attribute=[]    
#APPEND ATTRIBUTES INTO THE LIST
for i in range(sheet.ncols-1): 
	val=sheet.cell_value(0, i)
	attribute.append(str(val))

#LAST column GETS APPENDED TO final
final=[]		
for i in range(1,sheet.nrows): 
	val=str(sheet.cell_value(i,sheet.ncols-1))
	final.append(val)

########################################################################################
######FINDING THE ENTROPY OF THE FULL DATASET
########################################################################################
counter=[]
MainEntropy=0
#FINDING THE COUNT OF EACH RESULT(BUS,CAR,TRAIN) FOR FULL DATASET USING COUNTER FINAL FUNCTION
counter=countfinal(final)
########################################################################################
######FINDING MAIN_ENTROPY BY CALLING entropy FUNCTION
########################################################################################
MainEntropy=entropy(counter)
print("Main Entropy:",MainEntropy)
level=[]
#FOR LOOP WHICH SENDS ATTRIBUTE TO INFORMATION GAIN FUNCTION ONE BY ONE
index=0
for i in attribute:
	gain=IG(i,index,"Dataset1.xlsx",0)
########################################################################################
#FIND THE MAXIMUM IMFORMATION GAIN ATTRIBUTE
########################################################################################
	if gain>Maxi:
		Maxi=gain
		Maxattr=i
		Maxindex=index
	index=index+1
selected_attr.append(Maxattr)
selected_index=Maxindex
print("attribute "+Maxattr+" with maximum Information gain "+str(Maxi)+" "+str(Maxindex))
Dict={}
Dict[Maxattr] = 2, 3, 4

storefile=open("nodes.txt","w")
storefile.write("Parent Child\n")
for i in range(1,sheet.nrows): 
	level.append(sheet.cell_value(i, Maxindex))

num=0
Dict[Maxattr]=set(level)
attr_list=list(set(level))
Maxattr1=Maxattr
attr_list1=attr_list
attr_list.sort()
nodes_dic["root"]=Maxattr
for i in attr_list:
	nodes_dic[i]=Maxattr
	storefile.write(str(Maxattr)+" "+str(i)+"\n")


########################################################################################
########!!!!!!!!FINDING ALL THE OTHER NODES!!!!!!!!!!!!!!!!!!!!!!!!!!
########################################################################################
list_of_sel_index=[]
label1=[]
nameincre=0
sheet_select=0 
whileind=len(set(attribute))-len(set(selected_attr))

while whileind>0:
	wb = xlrd.open_workbook(loc) 
	sheet = wb.sheet_by_index(sheet_select) 
	wb = Workbook() 
	items=[]
	for i in range(1,sheet.nrows):
		items.append(str(sheet.cell_value(i,Maxindex)))
	column_values=list(set(items))
	column_values.sort()
	index1=0
	namelist=[]
########################################################################################
###########PRINTING THE BRANCHING DATA INTO INDIVIDUAL EXCELSHEETS
########################################################################################	
	for j in column_values:
		index1+=1
		cont=0
		sheetname="sheet"+str(index1)
		sheetname= wb.add_sheet(sheetname) 
		for i in range(1,sheet.nrows):
			if j==(str(sheet.cell_value(i,Maxindex))):
				for k in range(0,sheet.ncols):
					if k==1:
						value=int(sheet.cell_value(i,k))
					else:
						value=str(sheet.cell_value(i,k))
					
					sheetname.write(cont+1,k,value)	
				cont+=1
	namestring="excel"+str(nameincre)+".xlsx"
	wb.save(namestring)
	loc = (namestring)
	wb = xlrd.open_workbook(loc) 
	Maxi=0
	sheetname1=[]
########################################################################################
######--------Using above obtained values and calculating for all attributes iteratively
########################################################################################
	for i in range(index1):
		counter1=[]
		sheetn = wb.sheet_by_index(i)
		lastcolumn=[]
		for j in range(1,sheetn.nrows): 
			val=str(sheetn.cell_value(j,sheetn.ncols-1))
			lastcolumn.append(val)
		counter1=countfinal(lastcolumn)
		entropy_result=entropy(counter1)
		if entropy_result!=0 :
			if selected_index!=1:
				parent1=str(sheetn.cell_value(1,selected_index))
			else:
				parent1=int(sheetn.cell_value(1,selected_index))
			sheet_select=i
			ind=0
			for f in attribute:
				if f not in selected_attr:
					info=IG(f,ind,namestring,i)
					if info>Maxi:
						Maxi=info
						Maxattr=f
						Maxindex=ind
				ind=ind+1
			attr_column1=[]
			for i in range(1,sheetn.nrows): 
				if Maxindex==1:
					attr_column1.append(int(sheetn.cell_value(i,Maxindex)))
				else:
					attr_column1.append(str(sheetn.cell_value(i,Maxindex)))
			attr_set=list(set(attr_column1))
			attr_set.sort()
			for i in attr_set:
				nodes_dic.__setitem__(i,parent1)
				if isinstance(i,float):
					i=int(i)
				storefile.write(str(parent1)+" "+str(i)+"\n")
		elif	 entropy_result ==0:
			if selected_index!=1:
				value=str(sheetn.cell_value(1,selected_index))
			else:
				value=int(sheetn.cell_value(1,selected_index))
			label1.append(value)
			value1=str(sheetn.cell_value(1,sheetn.ncols-1))
			Dict[value]=value1
			storefile.write(str(value)+" "+value1+"\n")
		attr_column1=[]
		for i in range(1,sheetn.nrows): 
			if Maxindex==1:
				attr_column1.append(int(sheetn.cell_value(i,Maxindex)))
			else:
				attr_column1.append(str(sheetn.cell_value(i,Maxindex)))
	attr_set=list(set(attr_column1))
	attr_set.sort()
	for i in attr_set:
		nodes_dic.__setitem__(i,parent1)
		if isinstance(i,float):
			i=int(i)
	selected_attr.append(Maxattr)
	selected_index=Maxindex
	list_of_sel_index.append(selected_index)
	nameincre=nameincre+1
	whileind+=-1
	if whileind==0:
		break
storefile.close()	

fv=len(attribute)
sv=len(selected_attr)
root_node=Node(Maxattr1)
nodes={}
nodes[root_node.name]=root_node

########################################################################################
##########TREE BUILDING
########################################################################################
for i in attr_list1:
	k=str(i)
	k = Node(str(i), parent=nodes[root_node.name])
with open('nodes.txt','r') as f:
	lines=f.readlines()[1:]
	root=Node(lines[0].split(" ")[0])
	nodes={}
	nodes[root.name]=root

	for line in lines:
		line=line.split(" ")
		name="".join(line[1:]).strip()
		nodes[name]=Node(name,parent=nodes[line[0]])

########################################################################################
#####---------TREE PRINTING
########################################################################################
	for pre,_,node in RenderTree(root):
		print("%s%s" %(pre,node.name))


########################################################################################
##########----------FOR USER GIVEN INPUT FINDING FINAL_VALUE---------------#############
########################################################################################

userinput =input(str('Enter your row in the order of\ngender(female/male)\ncarownership(0,1,2)\ntravelcost(cheap,standard,expensive)\nincomelevel(low,medium,high):\nage(22,32,44)\n'))
user_attr=userinput.split(' ')
print(user_attr)
file1=open('nodes.txt','r')

f=['bus','car','train']
flag=0
i=''
for line in file1:
	if line.startswith(Maxattr1):
		#print(Maxattr1)
		for i in user_attr:
			if i in line:
				user_attr.remove(i)
				flag=1
				break
	if flag==1:
		break

#print(str(i))


if str(i) in f:
	print('Your mode of transport is: '+str(i))
else:
	while(True):
		flag=0
		flag2=0
		file1.seek(0,0)
		for line in file1:
			if line.startswith(i):
				for j in user_attr:
					if str(j) in line:
						#print(str(j))
						user_attr.remove(j)
						flag=1
						break
				for m in f:
					if m in line:
						flag2=1
						break
				if flag==1:
					i=str(j)
					break
		if flag2==1:
			break
print("Your mode of Transport is "+str(m))

########################################################################################
#####################-----------------THE END-------------------########################
########################################################################################


########################################################################################
########################################################################################
#########  DIVISION IS NOT IMPLEMENTED DUE TO PRECISION PROBLEMS #######################
########################################################################################
	
