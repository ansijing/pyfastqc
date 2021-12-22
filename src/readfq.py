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
    #print("list length: ", len(seq_len_list))    
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
        Phred_type = 'phred_33 (Illumina 1.8+)'
    else:
        Phred_type = 'phred_64 (Illumina 1.3+/1.5+)'
    return Phred_type
        

def get_GC_cont(file_path): 
    """get GC content"""
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
            seq_list_1 = str(seq_list)
            for base in seq_list_1:
                if base == 'G' or base == 'C':
                    num_GC += 1
            num_GC_1 = num_GC

            for base in seq_list_1:
                if base == 'G' or base == 'C' or base == 'A' or base == 'T':
                    num_all_base += 1

        #print("ALL: ", num_all_base)
        cont = float(num_GC_1 / num_all_base) 
        cont_1 = format(cont, '.0%') 
    return cont_1