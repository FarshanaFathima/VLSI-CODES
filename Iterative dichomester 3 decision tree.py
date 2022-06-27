import subprocess
import math
import xlrd 
from itertools import groupby
from xlwt import Workbook 
from anytree import Node, RenderTree

global Maxi
global nodes_dic
nodes_dic={}
Maxi=0
selected_attr=[]
selected_index=[]

def countfinal(l):
	labels=["bus","car","train"]
	counter=[]
	for j in labels:
		count1=l.count(j)
		counter.append(count1)
	return counter






#FUNCTION TO FIND ENTROPY
def entropy(attr_countresult):
	s=0
	div=0
	for i in attr_countresult:
		k=0
		div=i/float(sum(attr_countresult))
		if div!=0:
			lg=float(math.log(div,2))
			k=abs(lg)
		s=s+div*k
	return s



#FUNCTION TO FIND InfoRMATION GAIN(ROOT NODE)
def IG(attr,attr_count,path,i):
	loc=(path)
	wb1 = xlrd.open_workbook(loc) 
	sheet = wb.sheet_by_index(i) 
	print("------------------------------------------------------------")
	attr_entropy=0
	attr_column=[]
	
#GETTING THE column OF PARTICULAR ATTRIBUTE
	for i in range(1,sheet.nrows): 
#attr_count=1 IS FOR CAROWNERSHIP(WE ARE DOING THIS BCUZ WE DONT WANT FLOAT)
		if attr_count==1:
			attr_column.append(int(sheet.cell_value(i,attr_count)))
		else:
			attr_column.append(str(sheet.cell_value(i,attr_count)))

	
	r=list(set(attr_column))
	r.sort()
	
	for i in r:
		print (i)
#BUSCOUNT CARCOUNT TRAINCOUNT
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
					
#INFORMATION GAIN FOR attr_entropy  CALCULATION STARTS HERE
#CALLING ENTROPY FUNCTION TO CALCULATE ENTROPY OF EACH SUBSET OF THE ATTRIBUTE	
		en=entropy(attr_countresult)
		#print("entropy",en)
		
		Prob=sum(attr_countresult)/float(sheet.nrows-1)
#attr_entropy-ATTRIBUTE TOTAL ENTROPY
		attr_entropy=attr_entropy+float(Prob*en)
#VERILOG NEEDED-MAC(preferable)
	#print("attr_entropy",attr_entropy)
	InfoGain=MainEntropy-attr_entropy
	print("Information gain of ",attr,InfoGain)
#INFORMATION GAIN IS RETURNED
	return InfoGain
	
			





#!!!!!!!!!!!!FINDING ROOT NODE!!!!!!!!!!!!!!!!!!!!!!!






#LOCATION OF FILE
loc = ("Dataset.xlsx") 
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
	val=str(sheet.cell_value(i,4))
	final.append(val)
#FINDING THE ENTROPY OF THE FULL DATASET
counter=[]
MainEntropy=0
#FINDING THE COUNT OF EACH RESULT(BUS,CAR,TRAIN) FOR FULL DATASET USING COUNTER FINAL FUNCTION
counter=countfinal(final)
#FINDING ENTROPY BY CALLING entropy FUNCTION
MainEntropy=entropy(counter)
print("Main Entropy",MainEntropy)

level=[]
#FOR LOOP WHICH SENDS ATTRIBUTE TO INFORMATION GAIN FUNCTION ONE BY ONE
index=0
for i in attribute:
	gain=IG(i,index,"Dataset.xlsx",0)
#FIND THE MAXIMUM IMFORMATION GAIN ATTRIBUTE
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
#first = Node(Maxattr)
for i in range(1,sheet.nrows): 
	print(sheet.cell_value(i, Maxindex))
	level.append(sheet.cell_value(i, Maxindex))

num=0
Dict[Maxattr]=set(level)
attr_list=list(set(level))
'''for i in set(level):
	k=str(i)
	
	print(k)
	k = Node(str(i), parent=first)
	num=num+1'''
Maxattr1=Maxattr
attr_list1=attr_list
attr_list.sort()
'''root_node=Node(Maxattr1)
for i in attr_list1:
	k=str(i)
	k = Node(str(i), parent=root_node)'''
nodes_dic["root"]=Maxattr
for i in attr_list:
	nodes_dic[i]=Maxattr
	storefile.write(Maxattr+"_"+i+"\n")
print(nodes_dic)







#!!!!!!!!FINDING ALL THE OTHER NODES!!!!!!!!!!!!!!!!!!!!!!!!!!


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
	#print(column_values)


	index1=0
	namelist=[]
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
	for i in range(index1):
		counter1=[]
		sheetn = wb.sheet_by_index(i)
		lastcolumn=[]
		for j in range(1,sheetn.nrows): 
			val=str(sheetn.cell_value(j,4))
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
				#if selected_index not in list_of_sel_index:

				if f not in selected_attr:
					info=IG(f,ind,namestring,i)
					#print(info)
					if info>Maxi:
						Maxi=info
						Maxattr=f
						Maxindex=ind
				ind=ind+1
			attr_column1=[]
			for i in range(1,sheetn.nrows): 
#attr_count=1 IS FOR CAROWNERSHIP(WE ARE DOING THIS BCUZ WE DONT WANT FLOAT)
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
				storefile.write(str(parent1)+"_"+str(i)+"\n")
		elif	 entropy_result ==0:
			if selected_index!=1:
				value=str(sheetn.cell_value(1,selected_index))
			else:
				value=int(sheetn.cell_value(1,selected_index))
			#print("sup"+str(value))
			label1.append(value)
			value1=str(sheetn.cell_value(1,4))
			#print("sup's value",value1)
			Dict[value]=value1
			storefile.write(str(value)+"_"+value1+"\n")
			#value12= Node(str(value1), parent=value)
		attr_column1=[]
		for i in range(1,sheetn.nrows): 
#attr_count=1 IS FOR CAROWNERSHIP(WE ARE DOING THIS BCUZ WE DONT WANT FLOAT)
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
		#storefile.write(parent1+"_"+str(i)+"\n")

	selected_attr.append(Maxattr)
	selected_index=Maxindex
	
	#print("attribute "+Maxattr+" with maximum Information gain "+str(Maxi)+" in column number "+str(Maxindex))
	list_of_sel_index.append(selected_index)
	#print(selected_attr)
	nameincre=nameincre+1
	whileind+=-1
	if whileind==0:
		break
storefile.close()	

fv=len(attribute)
sv=len(selected_attr)
#if fv-sv==1:
	#print("Last attribute to split with",set(attribute)-set(selected_attr))

#print(nodes_dic)
#print(RenderTree(first))

root_node=Node(Maxattr1)
nodes={}
nodes[root_node.name]=root_node

for i in attr_list1:
	k=str(i)
	k = Node(str(i), parent=nodes[root_node.name])
#for pre,fill,node in RenderTree(root_node):
#	print("%s%s" %(pre,node.name))
'''for i in nodes_dic:
	parent_node=Node(nodes_dic[i])

	nodes[parent_node]=Node(i, parent=parent_node)
for pre,_,node in RenderTree(root_node):
		print("%s%s" %(pre,node.name))'''

with open('nodes.txt','r') as f:
	lines=f.readlines()[1:]
	root=Node(lines[0].split("_")[0])
	nodes={}
	nodes[root.name]=root

	for line in lines:
		line=line.split("_")
		name="".join(line[1:]).strip()
		nodes[name]=Node(name,parent=nodes[line[0]])

	for pre,_,node in RenderTree(root):
		print("%s%s" %(pre,node.name))