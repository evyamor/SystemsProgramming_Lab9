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
 stats= open('movies.stats','a+')	
 with open(file,newline ='') as csvfile:
  spamreader = csv.DictReader(csvfile)
  ft=open('ft','w')
  for row in spamreader:
   ft.write(row['year']+" ")
   ft.write(row['country'])
   ft.write('\n')
  ft.close()
  csvfile.close()

 proc_y=subprocess.check_output(['awk','-F',',','{print $1 ":" $2}','ft']).decode('utf-8')
 process= open('proc','a+')
 process.write(proc_y)
 proc_c=subprocess.check_output(['awk','-F',',','{print $1}','ft']).decode('utf-8')
 process.write(proc_c + " ")
 proc_c=subprocess.check_output(['awk','-F',',','{print $3}','ft']).decode('utf-8')
 process.write(proc_c )
 process.close()
 procc= open('procc','w')
 proc_c=subprocess.check_output(['awk','-F',' ','{print $1}','proc']).decode('utf-8')
 procc.write(proc_c)
 procc.close()
 proc= open('procc','r')
 data = proc.read()
 years=sorted(set(data.split()))
 str_years=[]
 str_counter=[]
 for year in years:
  str_years.append(year)
  str_counter.append(str(data.count(year)))
 counter=0
 xtick=[None]*len(str_counter)
 ytick=[None]*len(str_counter)
 y_len=[None]*len(str_counter)
 for x in str_years:
  xtick[counter]=int(str_years[counter])
  ytick[counter]=int(str_counter[counter])
  y_len[counter]=counter
  counter+=1
 proc.close()
 c_file ='file.csv' 
 with open(c_file,'w',newline ='') as ccsvfile:
  writer = csv.writer(ccsvfile)
  writer.writerow(['year'])
  arr = data.split()
  for i in arr:
    writer.writerow([i]) 
 ccsvfile.close()
 with open(c_file,newline ='') as csvfile:
  data_2 = pd.read_csv(csvfile)
  years = data_2['year']
  plt.title(r'Histogram of IMDB by years: ')
  plt.xlabel('year')
  plt.ylabel('Number of movies')
  plt.hist(years,bins=xtick,color='blue',edgecolor='black',histtype='bar',alpha=0.5)
  plt.xticks(xtick,fontsize=7)
  plt.show()
  plt.hist(years,bins=[1894,1910,1915,1920,1930,1940,1960,1980,2000,2010,2020],color='blue',edgecolor='black',histtype='bar',alpha=0.5)
  plt.show()
 csvfile.close()
 stats.close()
 os.remove('file.csv')
 os.remove('proc')
 os.remove('procc')
 os.remove('ft')
if __name__ == '__main__':
 file= sys.argv[1]
 main(file)
 