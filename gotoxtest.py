import gotox
import gotox_mutator
"""
f=gotox.agoto()
#|varw|varr|varcond|c1|c2|out|

codedata = gotox_mutator.mutate(([[0,0,0,1,1,0],[0,0,1,0,0,1]],4),4)
print(codedata)
f.setcode(codedata)
f.call(0)
f.act(20)#ALWAYS REMEMBER TO ACT()
#print(f.getsomeoutputs())
#print(f.getoutput())
print(f.getsomeoutputs())
#print(f.getoutput())
print(f.memory)
#f.makmem(6)
#print(f.memory)
"""
f=gotox.agoto()
f.actionq.append(0)
g=gotox.agoto()

print(g.actionq)
print(f.actionq)