import gzip
import os

def get_fq_count(file_path): 
    if not os.path.exists(file_path):
        print('file not exists! Please check')
        return
    print('Input file: ', file_path)
    
    if file_path.endswith('.gz'):
        my_open = gzip.open
    else:
        my_open = open
        
    with my_open(file_path,'rb') as inpf:
        count = 0
        for line in inpf:
            line = line.strip()
            count += 1
        return count//4
                
                
def get_fq_sequence_lengh(file_path): 
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
        
    seq_len_max = max(seq_len_list)
    seq_len_min = min(seq_len_list)
    #print("seqmax:", seq_len_max)    
        
    return seq_len_min, seq_len_max           
 