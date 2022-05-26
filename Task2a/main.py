#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pandas as pd
import csv
import sys
import os
import subprocess
from collections import Counter



def main(file):
 stats= open('genre.stats','a+')	
 with open(file,newline ='') as csvfile:
  spamreader = csv.DictReader(csvfile)
  t_proc= open ('ft','w')
  with open('ft.csv','w') as csv_t:
   writer= csv.writer(csv_t)
   for row in spamreader:
    writer.writerow([row['genre']] + [row['duration']])
    t_proc.write(row['genre'] +" "+row['duration']+'\n')  
  csv_t.close()
  csvfile.close()
  t_proc.close()
  with open('ft2.csv','w') as csv_t2:
   writer = csv.writer(csv_t2)
   writer.writerow(['genre']+['duration'])
   with open('ft.csv','r') as csv_r:
    lines = csv.reader(csv_r) 
    
    for row in lines:
     gen_list= (row[0].split(",")[0:row[0].count(',')])
     if(len(gen_list)==0):
      gen_list= [row[0].split(" ")[0]]
      writer.writerow([gen_list[0]]+ [int(row[1])])
     else:
      for i in range(0,len(gen_list)-1):
       writer.writerow([gen_list[i]]+ [int(row[1])])

 csv_r.close()
 csv_t2.close()
 
 df = pd.read_csv("ft2.csv",names =['genre','duration'])
 sum=df.groupby('genre').sum()
 print("sum: ",sum)
 str_arr=[]
 with open('ftg.csv','w') as cs:
  sum.to_csv(cs)
 cs.close()
 with open('ftg.csv',newline='') as csv_f:
  reader =csv.DictReader(csv_f)
  c=0 
  for row in reader:
    str_arr.append(row['genre']+ ","+row['duration']+"minutes"+'\n')
    stats.write(str_arr[c])
    c+=1
 csv_f.close()
 stats.close()
 os.remove('ft')
 os.remove('ft2.csv')
 os.remove('ft.csv')
 os.remove('ftg.csv')
 

if __name__ == '__main__':
 file= sys.argv[1]
 main(file)
 