from os import walk

fo = open("./files/outfreq.txt","w")
def CountFrequency(my_list): 
      
    # Creating an empty dictionary  
    freq = {} 
    for items in my_list: 
        freq[items] = my_list.count(items) 
      
    for key, value in freq.items(): 
        fo.write("% s : % d\n"%(key, value)) 
  
f = []
for (dirpath, dirnames, filenames) in walk("./files/Train-corups/processed_files/"):
    f.extend(filenames)
    break
data = []
for file_name in f:
    with open("./files/Train-corups/processed_files/"+file_name, 'r') as file:
        data += file.read().split("\n")
        

CountFrequency(data)

