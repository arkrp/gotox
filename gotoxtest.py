import gotox
f=gotox.agoto()
#|varw|varr|varcond|c1|c2|out|
f.setcode([[2,0,0,1,1,9],[0,0,3,0,0,1]])
f.call(0)
f.act(2)#ALWAYS REMEMBER TO ACT()
#print(f.getsomeoutputs())
print(f.getoutput())
print(f.getoutput())
print(f.memory)
f.makmem(6)
print(f.memory)
