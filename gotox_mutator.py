import random
#this file serves as help for the evolutionary ai thing
#this allows random mutation of gotox code while avoiding gotox syntax errors
# this mutates one single value in the slot into another valid value
# it also has a 4% chance fore each of two things to occur
# 1. memsize incrasing by 1
# 2. a random cell being added
#this is missing many features that will be added after a working prototype is made
def mutate(celldata,outputs):# takes code amount of outputs there are and size of memory array
	celldata = codedesync(celldata)
        code,memsize=celldata
	code = code[:]
	#seperates it from reference
	if(random.randint(0,25)==0):
		memsize=memsize+1
	#if(random.randint(0,25)==0):
	#	memsize=memsize-1#WARNING THIS WILL DEFINITLY CAUSE KEYERRORS FIX IT LATER
	if(random.randint(0,25)==0):
		code.append(newRcell(len(code)+1,outputs,memsize))#makesarandom cell
	x=randstf(len(code))
	y=random.randint(0,5)
	if((y==3)or(y==4)):
		code[x][y]=randstf(len(code))
	if((y==0)or((y==1)or(y==2))):
		code[x][y]=randstf(memsize)#gets random memory space
	if(y==5):
		code[x][y]=randstf(outputs)#gets random one of the outpurs
	c=0
	return code,memsize
def newRcell(cod,outp,mem):#takes code lenght as well as mem and outp length
	return([randstf(mem),randstf(mem),randstf(mem),randstf(cod),randstf(cod),randstf(outp)])
def randstf(inp):#gets random memory/output space given amount of spaces
	return(random.randint(0,inp-1))
#def randcell(code):#gets random cell from a code cell length
#	return(random.randint(0,(code-1)))
#randcell was depreciated for being functionaly identical to randstf
#print(newRcell(len(acode),outp,memsz))
#print(newRcell(len(acode),outp,memsz))
#print(newRcell(len(acode),outp,memsz))
#print(newRcell(len(acode),outp,memsz))
#print(newRcell(len(acode),outp,memsz))
#print(newRcell(len(acode),outp,memsz))
def codedesync(celldata):#desynchroniseds the arrays required because of the python problems with multidimensional arrays required for any coppying or manipulation of gotoxs
	code,memsize=celldata
	code=code[:]
	c=0
	while(c<len(code)):
		code[c]=code[c][:]
		c=c+1
	return code,memsize

#test of this library

#acode=[[0,0,0,0,0,0],[0,0,0,0,0,0]]
#outp=6
#memsize=7

#while(True):
#	raw_input()
#	acode,memsize=mutate(acode,outp,memsize)
#	print(str(acode)+" "+str(memsize))
		
	
