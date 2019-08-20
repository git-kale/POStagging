from os import walk
fo = open("./files/outfreq.txt","w")
f = []
for (dirpath, dirnames, filenames) in walk("./files/Train-corups/processed_files/"):
    f.extend(filenames)
    break

data = []
for file_name in f:
    with open("./files/Train-corups/processed_files/"+file_name, 'r') as file:
        data += file.read().split("\n")

wordfreq = {}
for word in data:
    if word not in wordfreq:
        wordfreq[word] = 0 
    wordfreq[word] += 1

fo.write(str(wordfreq).replace(", ","\n")[1:-1])