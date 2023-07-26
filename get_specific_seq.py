#!/usr/bin/python
import re
from Bio import SeqIO
from Bio import Seq
import sys

def fix(file_path,fasta,length):
    lengthdict = dict()   #hash   
    with open(file_path) as seqlengths:
        for line in seqlengths:
            split_IDlength  = line.strip().split('  ')
            split_ID =split_IDlength[0].split("_")
            lengthdict[split_ID[1]] = split_IDlength[1]
    with open(fasta,"r") as fasta:
        result = [] #将for循环的结果保存到list列表中
        for record in SeqIO.parse(fasta,"fasta"):
            accession_ID=record.id.split('|')[1]
            if accession_ID in lengthdict:
                # 使用append只能传递一个参数，可以将多个元组打包成一个值来传递。
                result.append((">" ,record.id ,re.sub(r"(\w{%d})" % int(length),r"\1\n",str(record.seq)))) 
                # result.append((">" ,record.id ,re.sub(r"(\w{30})",r"\1\n",str(record.seq)))) 
    return(result) #最后需要return语句来返回结果列表。

if __name__ == "__main__":
    file_path = sys.argv[1] 
    fasta = sys.argv[2]
    length = sys.argv[3] 
    result = fix(file_path,fasta,length)
    
    with open (sys.argv[4],"w") as out:
        for line in result:
            out.write("{}{}\n{}\n".format(line[0],line[1],line[2]))


        