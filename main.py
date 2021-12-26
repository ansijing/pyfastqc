# -*- coding:utf-8 -*-
#!/usr/bin/env python

from src import readfq
from src import graph_per_bas_seq_qua
from src import graph_per_seq_qua_sco
from src import graph_per_bas_seq_con
if __name__ == '__main__':
    
    #step1. count sequence number
    count = readfq.get_fq_count('data/test2.fastq')
    print('sequence number: ', count)
    #step2. the sequence length 
    len_max, len_min = readfq.get_fq_sequence_lengh('data/test2.fastq')
    print('sequence length: ', len_max, len_min )
    # step3. estimate the type of phred
    qual_type= readfq.get_enc_type('data/test2.fastq')
    print('sequence length: ', qual_type)
    # step4. get GC content
    #contant = readfq.get_GC_cont('data/test.fastq')
    #print('GC cont: ', contant)
    
    #step5. box plot of per base sequence quality
    #plot_1, plot_2, plot_3, plot_4, plot_5, plot_6, plot_7 = graphs.qual_box_plot('data/test.fastq')
    #plot_1 = graph_per_bas_seq_qua.qual_box_plot('data/test2.fastq')

    #plot_2 = graph_per_bas_seq_qua.line_chart('data/test2.fastq')

    plot_3 = graph_per_seq_qua_sco.seq_qua_scor('data/test2.fastq')

    #plot_4 = graph_per_bas_seq_con.get_base_cont('data/test2.fastq')
    