import os
from natsort import natsorted
import xml.etree.ElementTree as ET
from multiprocessing import Pool
from time import time

def process_file(file_name):
    print("Processing "+file_name+"...")
    
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
        pos_tag = item.attrib['pos']
        processed_string += word.strip()+'_'+pos_tag+'\n'
    
    #writing the processed string to txt file
    outfile = open(DATA_DIR+'processed_files/'+file_name[:-4]+'.txt','w+')
    outfile.write(processed_string)
    outfile.close()

DATA_DIR = './files/Train-corups/'
NUM_PROCESSES = 5
all_filenames = natsorted(os.listdir(DATA_DIR))
all_filenames = [file for file in all_filenames if '.xml' in file]

start = time()
pool = Pool(NUM_PROCESSES)
pool.map(process_file, all_filenames)
time_taken = time() - start
print("DONE in "+str(time_taken)+" seconds")