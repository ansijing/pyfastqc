import gzip
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import collections
def qual_box_plot(file_path): 
    """Box plot of per base sequence quality """
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
    phred = 33
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
                #list_sum = np.array(seq_score_list).sum(0)

        seq_score_list = np.array(seq_score_list)
        #print('seq_score_list shape: ',seq_score_list.shape)
        seq_score_front = seq_score_list[:,0:10].T
        #print('seq_score_front. shape: ',seq_score_front.shape)
        seq_score_behind = seq_score_list[:,10:]
        #print('seq_score_behind shape: ', seq_score_behind.shape)
        step=5
        seq_score_behind_block = [seq_score_behind[:,j:j+step].flatten().tolist() for j in range(0,seq_score_behind.shape[1],step)]
        #print('C0 len',len(seq_score_behind_block[0]))
        #print(seq_score_behind_block)

        seq_score_front = seq_score_front.tolist()
        seq_score = seq_score_front + seq_score_behind_block 

        #print(seq_score)

            #step = 5
            #b = [quali_score_list[j:j+step] for j in range(10,len(quali_score_list),step)]
            #print('xxx')

            #print(b)
            #print('xxx')
            #exit(0)
            #print(quali_score_list[:10])
            #exit(0)
            #b = quali_score_list[:10] + b
            #for x in b:
            #    print("xxxxx:", x)

            #print("longggg: ", len(quali_score_list))
    #list_mean =  list_sum // 250   
    #list_median = np.median(seq_score_list, axis = 0)
    #list_10_perc = np.percentile(seq_score_list, 10, axis = 0)
    #list_25_perc = np.percentile(seq_score_list, 25, axis = 0)
    #list_50_perc = np.percentile(seq_score_list, 50, axis = 0)
    #list_75_perc = np.percentile(seq_score_list, 75, axis = 0)
    #list_90_perc = np.percentile(seq_score_list, 90, axis = 0)
    #df = pd.DataFrame(seq_score_list)
    #df.plot.box(title="hua tu")
    #plt.grid(linestyle="--", alpha=0.3)
    #plt.show()
    #print("seq_score_list" ,seq_score_list[:15])
    fig = plt.figure()  # 创建画布
    ax = plt.subplot()  # 创建作图区域
    

    #plt.rcParams['axes.facecolor']='pink'
    #g = ax.boxplot(seq_score_list[50:100], showfliers = False, boxprops=dict(facecolor='yellow'), medianprops={'color':'red'}, meanline = True, patch_artist=True,  widths=0.4, whis=[10, 90], showbox = True)  
    g = ax.boxplot(seq_score, showfliers = False, boxprops=dict(facecolor='yellow'), medianprops={'color':'red'}, meanline = True, patch_artist=True,  widths=0.4, whis=[10, 90], showbox = True)  

    ax.set_facecolor('pink')
    # 修改x轴下标
    #ax.set_xticks([1, 2])
    #ax.set_xticklabels(['first', 'second'])
    # 显示y坐标轴的底线
    plt.grid(axis='y')
    #plt.show()
    plt.savefig('test222.png')
    return  seq_score
                        
    #return list_mean, list_median, list_10_perc, list_25_perc, list_50_perc, list_75_perc, list_90_perc
    #return plt.show()

def line_chart(file_path):
    """line chart of means for different position in read""" 
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
            i = i + 1
            if i%4 == 3:
                quali_score_list_1 = list(map(ord, line))
                quali_score_list = np.array(quali_score_list_1) - 33

                seq_score_list.append(quali_score_list)
                list_sum = np.array(seq_score_list).sum(0)
                
    #a = np.array(seq_score_list) 
    #print(a.shape)
    list_mean =  list_sum // 250
    y1 = list_mean[50:100]
    x1 = range(1, 51)
    plt.plot(x1, y1, label = 'mean plot', linewidth = 2, color = 'blue')
    plt.xlabel('position in read')
    plt.ylabel('quality score')
    plt.title('per base sequence quality')
    #plt.rcParams['axes.facecolor']='pink'
    #plt.legend()
    plt.savefig('test111.png')
    return     


  






    