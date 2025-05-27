#!/usr/bin/env python3

#open file from terminal input
import sys
fastafile=open(sys.argv[1])
contents=fastafile.read()
file_lines = contents.split("\n")


#create a seq_list that puts only sequences in a list (removes headers)
seq_list=[]
for line in file_lines:
    if line.startswith(">")==False:
        seq_list.append(line)


#create an alignment string that matches bases with pipe or space
alignment_str=""
for index in range(len(seq_list[0])):
    if seq_list[0][index]==seq_list[1][index]:
        alignment_str+=("|")
    else:
        alignment_str+=(" ")

#prints alignment surrounded by two sequences
print(seq_list[0])
print(alignment_str)
print(seq_list[1])

#close file
fastafile.close()