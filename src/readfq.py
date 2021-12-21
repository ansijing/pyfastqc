import gzip
file_read = gzip.open("/root/data/asj/pyfastqc/data/SRR1976948_1.fastq.gz", 'rb')
file_out=open("SRR1976948_1.fastq","w")   
file_content = file_read.readlines() 
line_counts= len(file_content)
line_out = int(line_counts / 4)
print(line_out)    