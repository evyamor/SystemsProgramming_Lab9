#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import os
import subprocess
from collections import Counter



def main(file):	
 cmd=subprocess.call(["awk", "-F", '\t', '{print $1}', file])
 no_students= subprocess.check_output(["wc", "-l", file]).decode("utf-8")	
 no_int_stu=int(no_students[0]+no_students[1])+1
 print('Number of students : ',no_int_stu)
 cmd_2=subprocess.check_output(["awk", "-F", '\t', '{print $2}', file]).decode("utf-8")
 dup= open('newfile.txt','a+')
 dup.write(cmd_2)
 dup.close()
 dup2= open('newfile_sorted.txt','a+')
 g=subprocess.check_output(["awk", "-F", ':', '{print $1}', 'newfile.txt']).decode("utf-8")
 dup2.write(g)
 g=subprocess.check_output(["awk", "-F", '|', '{print $2}', 'newfile.txt']).decode("utf-8")
 dup2.write(g)
 g=subprocess.check_output(["awk", "-F", '|', '{print $3}', 'newfile.txt']).decode("utf-8")
 dup2.write(g)
 g=subprocess.check_output(["awk", "-F", '|', '{print $4}', 'newfile.txt']).decode("utf-8")
 dup2.write(g)
 g=subprocess.check_output(["awk", "-F", '|', '{print $5}', 'newfile.txt']).decode("utf-8")
 dup2.write(g)
 dup2.close()
 dup3= open('file_sorted.txt','a+')
 f=subprocess.check_output(["awk", "-F", ':', '{print $1}', 'newfile_sorted.txt']).decode("utf-8")
 dup3.write(f)
 dup3.close()
 os.remove('newfile.txt')
 os.remove('newfile_sorted.txt')

 errors=[]
 count =0
 filedup=open('file_sorted.txt','r')
 read_data=filedup.read()
 words=set(read_data.split())
 for word in words:
  count +=1
  if word not in errors:
    errors.append(word)
 i=0
 errors_counter=[]
 while(i<len(errors)-1):
   errors_counter.append(read_data.count(errors[i])) 
   i +=1
 print('total unique words:',count)
 print('total errors:',errors)
 print('Occurrences of errors by the same order:',errors_counter)
 filedup.close()
 os.remove('file_sorted.txt')
 

if __name__ == '__main__':
 file= sys.argv[1]
 main(file)
 