import os
from natsort import natsorted
import xml.etree.ElementTree as ET
from multiprocessing import Pool
from time import time

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = PROJECT_DIR+'/files/xmldata/'
TEST_DIR = PROJECT_DIR+'/files/testdata/'
PROCESS_DIR = PROJECT_DIR+"/generated_files/"
all_filenames = natsorted(os.listdir(DATA_DIR))
test_filenames = natsorted(os.listdir(TEST_DIR))
all_filenames = [file for file in all_filenames if '.xml' in file]
test_filenames = [file for file in test_filenames if '.xml' in file]

taglist = []
correct = 0
incorrect = 0
tagdict = {}
taglist = []
tagfreq = {}
l = [line.rstrip('\n') for line in open(
    PROJECT_DIR+"/generated_files/tagfreq.txt", 'r')]
for i in range(len(l)):
    l[i] = l[i].rsplit(":")
    l[i][0] = l[i][0][1:-1]
    tagfreq[str(l[i][0])] = int(l[i][1])
    tagdict[str(l[i][0])] = i
    taglist.append(l[i][0])

wrongtime = {}
bigram = []
for tag1 in taglist:
    sublist = []
    for tag2 in taglist:
        trans = [tag1, tag2, 0]
        sublist.append(trans)
    bigram.append(sublist)

outfreq = [line.rstrip('\n') for line in open(
    PROJECT_DIR+"/generated_files/outfreq.txt", 'r+', encoding='utf-8')]


outdict = {}
for i in range(0, len(outfreq)):
    outfreq[i] = outfreq[i].rsplit(":", 1)
    outfreq[i][0] = outfreq[i][0][1:-1]
    outfreq[i][0] = outfreq[i][0].rsplit("_")
    outfreq[i][1] = int(outfreq[i][1])/tagfreq[outfreq[i][0][1]]
    if outfreq[i][0][0] in outdict:
        outdict[outfreq[i][0][0]][outfreq[i][0][1]] = outfreq[i][1]
    else:
        outdict[outfreq[i][0][0]] = {outfreq[i][0][1]: outfreq[i][1]}


def predict_tag(file_name):
    global correct
    global incorrect
    # opening the xml file
    tree = ET.parse(TEST_DIR+file_name)

    # fetching the root tag of read xml file
    root = tree.getroot()

    # fetching all the word tags inside root
    strings = root.iter('s')

    for string in strings:

        string = string.findall('w')
        predicted_tag = ''
        if len(string) > 0:
            actual_tag = string[0].attrib['c5']
            value = 0

            for tag in outdict[str(bytes(string[0].text.strip(" "), 'utf-8'))[2:-1]]:

                if(outdict[str(bytes(string[0].text.strip(" "), 'utf-8'))[2:-1]][tag] > value):
                    predict_tag = tag
                    value = outdict[str(
                        bytes(string[0].text.strip(" "), 'utf-8'))[2:-1]][tag]

            currenttag = ""
            lasttag = predict_tag
            for i in range(1, len(string)):
                actual_tag = string[i].attrib['c5'].split("-")
                for tag in outdict[str(bytes(string[i].text.strip(" "), 'utf-8'))[2:-1]]:
                    value2 = outdict[str(bytes(string[i].text.strip(
                        " "), 'utf-8'))[2:-1]][str(tag)]*bigram[tagdict[lasttag]][tagdict[str(tag)]][2]
                    if(value2 > value):
                        currenttag = tag
                        value = value2
                
                if currenttag in actual_tag:
                    correct += 1
                else:
                    incorrect += 1
                    if(string[i].text.strip(" ")) in wrongtime:
                        wrongtime[string[i].text.strip(" ")] += 1
                    else:
                        wrongtime[string[i].text.strip(" ")] = 1
                lasttag = currenttag
                value = 0

    


def process_file(file_name):
    # opening the xml file
    tree = ET.parse(DATA_DIR+file_name)

    # fetching the root tag of read xml file
    root = tree.getroot()

    # fetching all the word tags inside root
    strings = root.iter('s')

    for string in strings:
        tagorder = []
        for element in string.findall('w'):
            tagorder.append(element.attrib['c5'].split("-"))

        for i in range(1, len(tagorder)):

            for j in range(len(tagorder[i-1])):
                for k in range(len(tagorder[i])):
                    bigram[tagdict[str(tagorder[i-1][j])]
                           ][tagdict[str(tagorder[i][k])]][2] += 1


for filename in all_filenames:
    process_file(filename)
for filename in test_filenames:
    predict_tag(filename)
    print(correct/(correct+incorrect))


