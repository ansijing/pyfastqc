import gzip
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import collections
import operator
import numpy as np
from scipy.stats import norm

def per_bas_N(file_path): 
    """Per Base N Content"""
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
        num_N = 0
        num_all_base = 0
        for line in inpf:
            line = str(line.strip())

            i = i + 1

            if i%4 == 1:
                seq_list.append(line)
        j = 0
        count_dic = {}
        for read in seq_list:
            j = j + 1
            for base in read:
                if base == 'N':
                    num_N += 1
                num_N_1 = num_N

        #print("ALL: ", num_all_base)
            cont = num_N_1
            print("N: ", cont)
            count_dic[j] = cont
        print("dicdic", count_dic)
    y1 = count_dic.values()
    #y_smoothed = gaussian_filter1d(y1, sigma=5)
    x1 = count_dic.keys()
    
    #plt.scatter(x1, y1, label = 'mean plot', linewidth = 2, color = 'red')
    plt.plot(x1, y1, label = 'N%', linewidth = 2, color = 'red')
    plt.xlabel('position in read(bp) ')
    plt.ylabel('N counts')
    plt.ylim(0, 0.4)

    plt.title('N count across all bases')
    #plt.rcParams['axes.facecolor']='pink'
    #plt.legend()
    plt.show()
    plt.savefig('per_base_N_con.png')
    return
#        data_count2=collections.Counter(count_dic.values())
#        sort_key_dic_instance = dict(sorted(data_count2.items(), key=operator.itemgetter(0)))
#        print("clust:", sort_key_dic_instance)
#    y1 = sort_key_dic_instance.values()
#    x1 = sort_key_dic_instance.keys()
    
    #plt.scatter(x1, y1, label = 'mean plot', linewidth = 2, color = 'red')
#    plt.plot(x1, y1, label = 'GC count per read', linewidth = 2, color = 'red')
#    plt.xlabel('mean GC content ')
#    plt.ylabel('read counts')
#    plt.title('GC distribution over all sequeces')
    #plt.rcParams['axes.facecolor']='pink'
    #plt.legend()
#    plt.show()
#    plt.savefig('per_seq_GC_con.png')
    return