import os
from natsort import natsorted
import xml.etree.ElementTree as ET
from multiprocessing import Pool
from time import time


double_tag = 0
single_tag = 0
ambiguios_tag = 0
sampleformat = ""
taglist = []
def process_file(file_name):
    global single_tag
    global double_tag
    global ambiguios_tag
    
    #opening the xml file
    tree = ET.parse(DATA_DIR+file_name)
    
    #fetching the root tag of read xml file
    root = tree.getroot()
    
    #fetching all the word tags inside root
    strings = root.iter('w')

    
    #iterating over found word tags
    for item in strings:
        word = item.text
        pos_tag = item.attrib['c5']
        if "-" in pos_tag:
            double_tag+=1
            pos_tag = pos_tag.split("-")
            for tag in pos_tag:
                if tag not in taglist:
                    taglist.append(tag)
        elif pos_tag=="":
            ambiguios_tag +=0
        else:
            single_tag+=1
            if pos_tag not in taglist:
                    taglist.append(pos_tag)

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = PROJECT_DIR+'/files/xmldata/'
PROCESS_DIR = PROJECT_DIR+"/generated_files/"

all_filenames = natsorted(os.listdir(DATA_DIR))

all_filenames = [file for file in all_filenames if '.xml' in file]

# pool = Pool(NUM_PROCESSES)
# pool.map(process_file, all_filenames)
for file in all_filenames:
    process_file(file)

analfile = open(PROCESS_DIR+"TrainingCorpusAnalysis"+'.txt','w+')
tagstr = ""
for i in range(0,5*(len(taglist)//5-1)):
    tagstr += str(i)+". "+taglist[i]+"    "+str(i+1)+". "+taglist[i+1]+"    "+str(i+2)+". "+taglist[i+2]+"    "+str(i+3)+". "+taglist[i+3]+"    "+str(i+4)+". "+taglist[i+4]+"    "+str(i+5)+". "+taglist[i+5]+"\n"
    i = i+5
for i in range(5*(len(taglist)//5-1),len(taglist)):
    tagstr += str(i)+". "+taglist[i]+"    "
analysis = "\nThe training data consist of "+str(len(all_filenames))+" files which consist of data in format :\n" +sampleformat + ".\nThe training corpus consist of following tags :\n"+tagstr+"\nOut of the words in corpus "+str(single_tag)+" words had single tag "+str(double_tag)+" words had double tag "+str(ambiguios_tag)+" words had ambiguity in their tag."


# plotting the
analfile.write(analysis)