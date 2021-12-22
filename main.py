# -*- coding:utf-8 -*-
#!/usr/bin/env python

from src import readfq

if __name__ == '__main__':
    
    #step1. count sequence number
    count = readfq.get_fq_count('data/test.fastq')
    print('sequence number: ', count)
    #step2. the sequence length 
    len_max, len_min = readfq.get_fq_sequence_lengh('data/test.fastq')
    print('sequence length: ', len_max, len_min )
    # step3. estimate the type of phred
    qual_type= readfq.get_enc_type('data/test.fastq')
    print('sequence length: ', qual_type)
    # step4. get GC content
    contant = readfq.get_GC_cont('data/test.fastq')
    print('GC cont: ', contant)