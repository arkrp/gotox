import gotox
import copy
import gotox_mutator
# this is meant to ba a basic test of the gotox api and its effectiveness in use
def getlowestpos(scores):
    c=0
    lowestp = 0
    lowest = scores[0]
    while(c<len(scores)):
        if(scores[c]<lowest):
            lowest = scores[c]
            lowestp = c
        c=c+1
    return lowestp
def getgreatestpos(scores):
    c=0
    greatp=0
    great=scores[0]
    while(c<len(scores)):
        if(scores[c]>great):
            great = scores[c]
            greatp = c
        c=c+1
    return greatp


#basecode=([[0,0,0,1,1,1],[0,0,0,1,1,2]],2)
#basecode = ([[0,0,0,0,0,0]],2)
def basecode():# this is a dirty hack to remove the reference problem with nested arrays
    return(([[0,0,0,0,0,0]],2))
print(basecode())
def testcode(codedata):#this scores the code on its aptitude to mash two output
    print("testing"+str(codedata))
    score=0
    f=gotox.agoto()
    #print("ACRIONQ "+str(f.actionq))
    f.setcode(codedata)
    f.call(0)#ALWAYS REMEMBER TO INSERT INITIAL CALL
    f.act(20)
    #print(f.output)
    running=True
    while(running):
        x=f.getoutput()
        if(x==1):
            score=score+1
        if(x==2):
            score=score*2
        if(x=="END"):
            running=False
    print(score)
    #print("ENDAQ"+str(f.actionq))
    return score
    #del f
#print(testcode(basecode)) 


aihopper=[basecode(),basecode(),basecode(),basecode(),basecode()]
scores=[0,0,0,0,0]
#print(getgreatestpos(scores))
#print(getlowestpos(scores))
#aihopper[0]=gotox_mutator.mutate(aihopper[4],4)
#while(True):
#    raw_input("|")
#    aihopper[4]=gotox_mutator.mutate(aihopper[4],4)
#    print(aihopper)
c2=0
c=0
while(c<2000):
    #while(c2<5):
    scores[c2]=testcode(aihopper[c2])
    #print("AI"+str(c)+": "+str(aihopper[c2])+" score: "+str(scores[c2]))
    print(scores)

    newai=gotox_mutator.mutate(aihopper[getgreatestpos(scores)],4)
    print("mutated "+str(aihopper[getgreatestpos(scores)])+str(getgreatestpos(scores))+"\n got:"+str(newai))
    c2=getlowestpos(scores)
    aihopper[c2]=newai
        #c2=c2+1
    c=c+1

        
