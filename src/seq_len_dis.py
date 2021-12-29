import gzip
import os
import collections
import operator
import matplotlib.pyplot as plt

def seq_len_distribut(file_path): 
    if not os.path.exists(file_path):
        print('file not exists! Please check')
        return
    #print('Input file: ', file_path)
    
    if file_path.endswith('.gz'):
        my_open = gzip.open
    else:
        my_open = open
    
    seq_len_list = []
    with my_open(file_path,'r') as inpf:
        i = -1 
        for line in inpf:
            line = str(line.strip())
            #print('in loop: line is ', line)
            i = i + 1
            #print(' i is: ', i)
            if i%4 == 1:
                #print('enter i%4==1, line: ',line)
                seq_len = len(line)
                seq_len_list.append(seq_len)
                
    #print("seqqq:", seq_len_list)
    #print("list length: ", len(seq_len_list))    
    seq_len_max = max(seq_len_list)
    seq_len_min = min(seq_len_list)
    print("seqmax:", seq_len_list)    
    data_count2=collections.Counter(seq_len_list)
    data_count2[250] = 0
    data_count2[252] = 0
    print("really？", data_count2) 
    print("really？keys?", data_count2.keys())
    print("really？values?", data_count2.values())
        #for sirted in sorted(data_count2.keys()):
        #    print((sirted, data_count2[sirted]), end =" ") 
        #    testt = {(sirted, data_count2[sirted])}
            #print(testt)
    sort_key_dic_instance = dict(sorted(data_count2.items(), key=operator.itemgetter(0)))  #按照key值升序
    #print("sort_key_dic_instance", sort_key_dic_instance)
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
    plt.savefig('seq_len_distribut.png')
    return        
