import gzip
def readfq(file_read):
    """Total Sequences"""
    file_read_1 = gzip.open(file_read)  
    file_content = file_read_1.readlines() 
    line_counts= len(file_content)
    line_out = int(line_counts / 4)
    print(line_out)
readfq("/root/data/asj/pyfastqc/data/SRR1976948_1.fastq.gz")
        