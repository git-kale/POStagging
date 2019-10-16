import os
from natsort import natsorted
import xml.etree.ElementTree as ET
from multiprocessing import Pool
from time import time

def process_file(file_name):
    print(file_name)
    #opening the xml file
    tree = ET.parse(DATA_DIR+file_name)
    
    #fetching the root tag of read xml file
    root = tree.getroot()
    
    #fetching all the word tags inside root
    strings = root.iter('w')
    
    #empty processed sting to store words in word_POS format
    processed_string = ''
    
    #iterating over found word tags
    for item in strings:
        word = item.text
        pos_tag = item.attrib['c5']
        processed_string += word.strip()+'_'+pos_tag+'\n'
    
    #writing the processed string to txt file
    outfile = open(PROCESS_DIR+file_name[0:3]+'.txt','w+')
    outfile.write(processed_string.encode('utf-8'))
    outfile.close()

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = PROJECT_DIR+'/files/xmldata/'
PROCESS_DIR = PROJECT_DIR+'/files/processed_files/'
NUM_PROCESSES = 5
all_filenames = natsorted(os.listdir(DATA_DIR))

all_filenames = [file for file in all_filenames if '.xml' in file]

start = time()
pool = Pool(NUM_PROCESSES)
pool.map(process_file, all_filenames)
time_taken = time() - start
print("DONE in "+str(time_taken)+" seconds")