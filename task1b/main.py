#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import sys
import os
import subprocess
from collections import Counter



def main(file):
 stats= open('movies.stats','a+')	
 with open(file,newline ='') as csvfile:
  spamreader = csv.DictReader(csvfile)
  file_temp=open("new_temp_file",'w')
  for row in spamreader:
   file_temp.write(row['country'])
   file_temp.write('\n')
  file_temp.close()
  f=subprocess.check_output(['awk','-F',',','{print $1}','new_temp_file']).decode('utf-8')
  temp= open('temp.txt','a+')
  temp.write(f)
  f=subprocess.check_output(['awk','-F',',','{print $2}','new_temp_file']).decode('utf-8')
  temp.write(f)
  temp.close()
  calc= open('temp.txt','r')
  read_data= calc.read()
  words = set(read_data.split())
  string=[]
  for word in words:
    stats.write(word)
    stats.write("|")
    stats.write(str(read_data.count(word)))
    stats.write('\n')
  ft=open('ft','a+')
  for row in spamreader:
   ft.write(row[year])
   ft.write(row[country])
   ft.write('\n')
   ft.close()
  proc_y=subprocess.check_output(['awk','-F',',','{print $1}','new_temp_file']).decode('utf-8')
  proc_c=subprocess.check_output(['awk','-F',',','{print $2}','new_temp_file']).decode('utf-8')
  process= open('proc','a+')
  process.write(proc_y)
  process.write(proc_c)
  proc_c=subprocess.check_output(['awk','-F',',','{print $3}','new_temp_file']).decode('utf-8')
  process.write(proc_y)
  process.write(proc_c)
  process.close()
  proc= open('proc','r')
  data = proc.read()
  years=set(data.split())
  string2=[]
  for year in years:
    stats.write(year)
    stats.write
  csvfile.close()
  stats.close()
  os.remove('temp.txt')
  os.remove('new_temp_file')

if __name__ == '__main__':
 file= sys.argv[1]
 main(file)
 