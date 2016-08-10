import gotox
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


basecode=([[0,0,0,0,0,0]],2)

def testcode(codedata):#this scores the code on its aptitude to mash two output
    score=0
    f=gotox.agoto()
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
    return score
#print(testcode(basecode)) 


aihopper=[basecode,basecode,basecode,basecode,basecode]
scores=[0,0,0,0,0]
#print(getgreatestpos(scores))
#print(getlowestpos(scores))
c2=0
c=0
while(c<200):
    #while(c2<5):
    scores[c2]=testcode(aihopper[c2])
    print("AI"+str(c)+": "+str(aihopper[c2])+" score: "+str(scores[c2]))
    newai=gotox_mutator.mutate(aihopper[getgreatestpos(scores)],4)
    c2=getlowestpos(scores)
    aihopper[getlowestpos(scores)]=newai
        #c2=c2+1
    c=c+1

        
