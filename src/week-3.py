import copy
import os
PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))

def sec(val):
	return int(val[1])

l = [line.rstrip('\n') for line in open(PROJECT_DIR+"/generated_files/outfreq.txt",'r')]
	
for i in range(0,len(l)):
	l[i] = l[i].rsplit(":", 1)
	l[i][1] = int(l[i][1])

r = copy.deepcopy(l)


for i in range(0,len(r)):
	head,sep,tail = str(r[i][0]).partition("_")
	r[i][0] = tail.replace("'","").replace("\"","")
	r[i][1] = int(r[i][1])
	

l = sorted(l, key=sec, reverse=True)
r = sorted(r,key=sec,reverse=True)

tagfreq = {}
for word in r:
	if word[0] not in tagfreq:
		tagfreq[word[0]] = word[1]
	tagfreq[word[0]] += word[1]


with open(PROJECT_DIR+"/generated_files/top10_words.txt", 'w') as f:
	for i in range(10):
		f.write("{}: {}\n".format(l[i][0], l[i][1]))

fo = open(PROJECT_DIR+"/generated_files/tagfreq.txt","w")
fo.write(str(tagfreq).replace(", ","\n")[1:-1])