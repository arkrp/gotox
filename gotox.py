#changelog
"""
71116:
	started project
	made basic action quene
	event() call() and shift()
	began memory section
71216
	worked on memory
	started execell function
	defined cell parts
	made cell 1 run at the begigining of the program
	made main loop
	started on end of program handling
	found strange error
71416
	made it so conditional values start at zero
	cleaned up random print statements
	condition cde was moved from first position in the code to the third
	got bored and wrote a comment blob
	generalised call() and event()
71716
	made getaction() statement
	started getsomeactions()
	had trouble with empty() ist dosnt work
	changed call() to incall()
	made user friendly call()
	the empty() thing may be due to a reserved word or something
73116
	cleaned up some stuff
	worked on documentation
	added act() function
80216
	modifiesd default memory
	made setcode()
80316
	made it standard for ouputs to be numbers
	this will make it mutch more usefull  with evolutionary ai stuff
"""
#user function list:
#call(), getaction()
#gotox standard
#this is an interprter for gotox an programing language deigned to have a large tendency twards complex
#logical structures
#
#sutch a programing language was made to attemt to improve efectiveness of, and make a standard for,
#evolving neural networks for nonproffesional use
#
#it should be noted this language is not meant to be written mannualy as is it is designed to be
#randomly generated then proceduarly changed by process of selection
#
#this is made by a 15 year old in his free time so dont take it too seriosly 
#print("starting")
class agoto:
	actionq=[]#list of actions to occur
	output=[]
	#def help:#nothign yet
	def incall(se,a,input):#make event in the input quene this is a library function
		input.append(a)
#print actionq
	def act(se,x=1):#makes the nueral network go for an ammount of actions
		c=0
		while(c<x):
			t=se.event(se.actionq)
			#print("T"+str(t))
			if(t=="END"):
				return(1) #returns 1 if finished
			se.execell(t)
			c=c+1
		return(0)#returns 0 if unfinished
	def event(se,input):#gets the next event in the quene supplied as input
		x=0
		if len(input)<>0:
			x=input[0]
			se.shift(input)
		else:                           #   #  ###  #   #  ###   ###
			x="END"                 ##  #  #     # #   #    #   #
			#print("returning end") # # #  ###    #    ###  #     was bored
		return(x)                       #  ##  #     # #   #    #   #     so he wrote this
                                                #   #  ###  #   #  ###   ###
	def setcode(se,aray):
		se.cells=aray
	def shift(se,input):
		c=1
		while(c<len(input)):
			input[c-1]=input[c]
			#del actionq[-1]
			c=c+1
		del input[-1]
	#output=[]#                    	make a way to access outpt and send input to make this a library
	def getoutput(se):#library function gets output
		return(se.event(se.output))
	def getsomeoutputs(se):
		xd=se.output[:]
		#output=[]
		#empty()#for some reason putting output =[] dosnt work here with this interpreter
		#return(xd)
		se.output=[]
		return xd

		#empty(output)
	def help(self,sub="help"):
		if sub=="help":
			return """
			welcome to gotox a programing language designed specificaly for artificial intelligence applications
			is should be noted that even the person who made this cant think of another use for it so it would be ill advised to use it for anythin gelse

                        there are several basic functions in this library including:
			getoutput()
			getsomeoutputs()
			act()
			call()
			setcode()
			"""

	#def empty(XD):#emptys output
		#XD=[]
	def call(se,a):
		#print(a)
		se.incall(a,se.actionq)
	memory=[0,1,2,3]*4
	#memsize=8
	#memory[0]=3
	#print(memory)
	
	#parts of cells
	#this is the code to be interpreted there will be a better entry system later
	#varw=   [5,1,3]#variable to wright to
	#varr=   [1,1,3]#variable to read from
	#varcond=[0,5,3]#variable condition
	#this is the memory slot thet the condition is drawn from
	#drawing a 0 results in cellT being executed : 1 results in cellF
	#2 results in both : 3 results in neither
	#cellT=  [1,1,3]#first call cel
	#cellF=  [0,2,3]#second call cell
	#cellOUT=["cell 0 trigered","cell 1 triggered","hey look cell 2"]#cell output 0 if none
	
	#converting it to a more readable format
	#it goes like this 0.varw, 1.varr, 2.varcond, 3.cellT, 4.cellF, 5.cellOUT
	cells=[[5, 1, 0, 1, 0,-10],[1,1,5,1,2,-11],[3,3,3,3,3,-12]]
	def execell(se,cell):#execute the cell with this number
	#order of operations is as follows
	#output is given if any
	#any variable assignment is done
	#logic comparison is made
	#cells are called baed on this logic
		if se.cells[cell][5]<>0:
			#print(se.cellOUT[cell])
			se.output.append(se.cells[cell][5])
		se.memory[se.cells[cell][0]]=se.memory[se.cells[cell][1]]
		a=0
		b=0
		if se.memory[se.cells[cell][2]]==0:
			a=1
		if se.memory[se.cells[cell][2]]==1:
			b=1
		if se.memory[se.cells[cell][2]]==2:
			a=1
			b=1
		if a:
			se.incall(se.cells[cell][3],se.actionq)
			#print("called"+str(se.cellT[cell])+"from"+str(cell))
		if b:
			se.incall(se.cells[cell][4],se.actionq)
			#print("called"+str(se.cellF[cell])+"from"+str(cell))
	#every thing below this point is a test not part of the api

#f= agoto()
#f.call(0)  #initial call
#counter=0
#looping=1
#while (counter<10 and (looping)):
#	x=f.event(f.actionq)
	
	#print("running "+str(x))
#	if x=="END":
#		looping=0
#		print(f.memory)
#		print("ending")
#	else:
#		f.execell(x)
	#execell(event())
#	counter=counter+1
#print memory
#while(not f.act()):
#	pass
#f.act(20)
#call(1)
#call(2)
#call(3)
#call(4)
#print(event())
#print(event())
#print(event())
#print(f.output)
#print(f.getoutput())

#print(f.getsomeoutputs())
#print(f.getoutput())
#print(f.getoutput())
#print(f.getoutput())
#print(f.getaction())
#print(f.getaction())
#print(f.getaction())
#empty()

#print(f.output)
