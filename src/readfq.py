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
    print("seqmax:", seq_len_max)    
        
    return seq_len_min, seq_len_max  
         

def get_enc_type(file_path): 
    """by dealing Base quality score, get the type of Phred qualitiy """
    if not os.path.exists(file_path):
        print('file not exists! Please check')
        return
    print('Input file: ', file_path)
    
    if file_path.endswith('.gz'):
        my_open = gzip.open
    else:
        my_open = open
        
    quali_score_list = []
    with my_open(file_path,'r') as inpf:
        i = -1 
        for line in inpf:
            line = str(line.strip())
            #print('in loop: line is ', line)
            i = i + 1
            #print(' i is: ', i)
            if i%4 == 3:
                #print('enter i%4==3, line: ',line)
                for score in line:
                    quali_score = ord(score)
                    quali_score_list.append(quali_score)
        
    quali_score_max = max(quali_score_list)
    if quali_score_max <74:
        Phred_type = 'phred_33'
    else:
        Phred_type = 'phred_64'
    return Phred_type
        
