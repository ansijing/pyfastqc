import gzip
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import collections
import operator
from scipy.ndimage import gaussian_filter1d
def seq_qua_scor(file_path, phred = 33):
    """plot for Per Sequence Quality Scores"""
    if not os.path.exists(file_path):
        print('file not exists! Please check')
        return
    print('Input file: ', file_path)
    
    if file_path.endswith('.gz'):
        my_open = gzip.open
    else:
        my_open = open
        
    quali_score_list = []
    seq_score_list = []
    with my_open(file_path,'rb') as inpf:
        i = -1 
        for line in inpf:
            line = str(line.strip())
            #print('in loop: line is ', line)
            i = i + 1
            #print(' i is: ', i)
            if i%4 == 3:
                quali_score_list_1 = list(map(ord, line))
                quali_score_list = np.array(quali_score_list_1) - phred
                #print(quali_score_list.shape)

                seq_score_list.append(quali_score_list)
                list_sum = np.array(seq_score_list).sum(1)
        #print("seqlist:", len(seq_score_list))
        #print("listsum", list_sum.shape)
        list_mean = list_sum // 254
        #print('seq_score_list shape: ',list_mean)
        data_count2=collections.Counter(list_mean)
        #print("really？", data_count2)
        print("really？keys?", data_count2.keys())
        print("really？values?", data_count2.values())
        #for sirted in sorted(data_count2.keys()):
        #    print((sirted, data_count2[sirted]), end =" ") 
        #    testt = {(sirted, data_count2[sirted])}
            #print(testt)
        sort_key_dic_instance = dict(sorted(data_count2.items(), key=operator.itemgetter(0)))  #按照key值升序
        print("sort_key_dic_instance", sort_key_dic_instance)
    y1 = sort_key_dic_instance.values()
    #y_smoothed = gaussian_filter1d(y1, sigma=5)
    x1 = sort_key_dic_instance.keys()
    
    #plt.scatter(x1, y1, label = 'mean plot', linewidth = 2, color = 'red')
    plt.plot(x1, y1, label = 'mean plot', linewidth = 2, color = 'red')
    plt.xlabel('mean sequence quality ')
    plt.ylabel('read counts')
    plt.title('quality score distribution over all sequeces')
    #plt.rcParams['axes.facecolor']='pink'
    #plt.legend()
    plt.show()
    plt.savefig('test333.png')
    return  