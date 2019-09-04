import copy
from os import path
PROJECT_DIR = path.dirname(path.dirname(__file__))

l = [line.rstrip('\n') for line in open(PROJECT_DIR+"/generated_files/outfreq.txt",'r')]

for i in range(0,len(l)):
        l[i] = l[i].rsplit(":",1)
        l[i][0] = l[i][0].rsplit("_",1)
        l[i][1] = int(l[i][1])
        if(l[i][0]==""):
            l[i][0] = ['','']

worddict = {}
for word in l:
    if word[0][0] not in worddict:
        worddict[word[0][0]] = 0
    worddict[word[0][0]] += int(word[1])
    
fo = open(PROJECT_DIR+"/generated_files/wordprob.txt","w")


for item in l:
    item[1] = item[1]/worddict[item[0][0]]
for item in l:
    fo.writelines(item[0][0]+"_"+item[0][1]+": "+str(item[1])+"\n")
