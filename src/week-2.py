from os import walk,path
PROJECT_DIR = path.dirname(path.dirname(__file__))

fo = open(PROJECT_DIR+"/generated_files/outfreq.txt","w")
f = []
for (dirpath, dirnames, filenames) in walk(PROJECT_DIR+"/files/processed_files/"):
    f.extend(filenames)
    break

data = []
for file_name in f:
    with open(PROJECT_DIR+"/files/processed_files/"+file_name, 'r') as file:
        data += file.read().split("\n")

wordfreq = {}
for word in data:
    if word not in wordfreq:
        wordfreq[word] = 0 
    wordfreq[word] += 1
nullval = wordfreq['']
wordfreq.pop('')
wordfreq['_']=nullval
fo.write(str(wordfreq).replace(", ","\n")[1:-1])