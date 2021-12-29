import gzip
import os
import numpy as np
import matplotlib.pyplot as plt

def get_base_cont(file_path): 
    """get base content"""
    if not os.path.exists(file_path):
        print('file not exists! Please check')
        return
    #print('Input file: ', file_path)
    
    if file_path.endswith('.gz'):
        my_open = gzip.open
    else:
        my_open = open
    
    seq_list = []
    with my_open(file_path,'r') as inpf:
        i = -1 
        h = 0 
        num_G = 0
        #num_all_base = 0
        j = 0
        for line in inpf:
            line = str(line.strip())

            i = i + 1
            #if i%4 == 3:
            #    quali_score_list_1 = list(map(ord, line))
            #    quali_score_list = np.array(quali_score_list_1) - phred
            #    #print(quali_score_list.shape)

            #   seq_score_list.append(quali_score_list)
        
            if i%4 == 1:
                seq_list.append(line)
        print("1111:", len(seq_list))
        dict_2d = {{'base': {'A': 0, 'T': 0, 'C': 0, 'G': 0}, 'position': {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}}}
        for read in seq_list:
            for base in read:
                h = h + 1
                
                if base == 'G':
                    num_G += 1
                num_G_1 = num_G
                #print("base: ", base)
                #print("hhhh:", h)
        print("GGGG: ", num_G_1)
        
    return
