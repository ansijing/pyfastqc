import gzip
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import collections
import operator

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
            #seq_list_1 = str(seq_list)
            #for base in seq_list:
            #    if base == 'G':
            #        num_G += 1
            #num_G_1 = num_G
            j = j +1
            for j in seq_list[0]:
                if seq_list[0] == 'G':
                    num_G += 1
            num_G_1 = num_G

        print("G1: ", num_G_1)
        #cont = float(num_G_1 / 250) 
        #cont_1 = format(cont, '.0%')
        #print("counttt:", cont_1) 
        plt.savefig('graph_per_bas_seq_con.png')
    return 