import gzip
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import collections
import operator
import numpy as np
from scipy.stats import norm

def per_seq_GC(file_path): 
    """Per Sequence GC Contentt"""
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
        num_GC = 0
        num_all_base = 0
        for line in inpf:
            line = str(line.strip())

            i = i + 1

            if i%4 == 1:
                seq_list.append(line)
        print("1111:", len(seq_list))
        base_G = []
        j = 0
        count_dic = {}
        for read in seq_list:
            j = j + 1
            for base in read:
                if base == 'G' or base == 'C':
                    num_GC += 1
                num_GC_1 = num_GC

            for base in read:

                if base == 'G' or base == 'C' or base == 'A' or base == 'T':
                    num_all_base += 1

        #print("ALL: ", num_all_base)
            cont = float(num_GC_1 / num_all_base) 
            cont_1 = format(cont, '.0%') 
        #    print("j: ", j)
        #    print("gc%: ", cont_1)
            count_dic[j] = cont_1
       # print("dicdic", count_dic)
        data_count2=collections.Counter(count_dic.values())
        sort_key_dic_instance = dict(sorted(data_count2.items(), key=operator.itemgetter(0)))
        #print("clust:", sort_key_dic_instance)
    y1 = sort_key_dic_instance.values()
    #y_smoothed = gaussian_filter1d(y1, sigma=5)
    x1 = list(sort_key_dic_instance.keys())
    x1 = [int(t[:-1])/100 for t in x1]
    #plt.scatter(x1, y1, label = 'mean plot', linewidth = 2, color = 'red')
    plt.plot(x1, y1, label = 'GC count per read', linewidth = 2, color = 'red')
    plt.xlabel('mean GC content ')
    plt.ylabel('read counts')
    plt.title('GC distribution over all sequeces')
    #plt.rcParams['axes.facecolor']='pink'
    #plt.legend()
    #plt.show()
    print('x1: ', x1)
    print('count_dict: ', count_dic)
    counts_arr = [int(t[:-1])/100 for t in list(count_dic.values())]
    print(sort_key_dic_instance.values())
    mean,std=norm.fit(counts_arr)
    print('mean,std',mean, std)
    xmin, xmax = plt.xlim()
    
    x = np.linspace(xmin, xmax, 100)
    y = norm.pdf(x, mean, std) 
    print('------x-------')
    print(x)
    print('-----y------')
    print(y)
    print('xmax,xmin',xmax,xmin)

    plt.plot(x, y)
    #plt.show()    

    plt.savefig('per_seq_GC_con.png')
    return
