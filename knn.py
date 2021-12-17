import numpy as np
import scipy as sc
import pandas as pd
import matplotlib.pyplot as plt
from scipy import pi
#import astropy as asp
import math
#from Mass import Mass
from module import *


#print('source file:') #insert source file
#source_file=input()
obj='ngc188 r=10'
df1=pd.read_csv('ngc188 r=10-result.csv')
print(df1['Mass'])
#input()
df3=df1
df3.drop_duplicates('source_id',keep='first',inplace=True) #removing duplicate sources
df3=df3.dropna(subset=['parallax']) #removing sources without parallax
df3=df3.reset_index(drop=True) #reseting index
del df1
'''distance filter
here we select a range where we know the OC is there
consider Distsnce+20% for upper and distance-20% for lower limit
'''
limits_of_distance=[]
limits_of_distance.append(float(input('lower limit: ')))  #inserting lowerlimit for distance filter
limits_of_distance.append(float(input('upper limit: ')))  #inserting upperlimit for distance filter
df3['flag_dist']=np.ones(len(df3['source_id']))
for i in range(len(df3['source_id'])):
    if df3['r_med_photogeo'][i]<limits_of_distance[0] or df3['r_med_photogeo'][i]>limits_of_distance[1]:
        df3['flag_dist'][i]=None
    if i%1000==0:
        print(i)

df4=df3.dropna(subset=['flag_dist'])
print(len(df4['flag_dist']))
#df4=pd.read_csv(r'C:\Users\MATG41\Desktop\article\open clusters\M21-distfiltered.csv')
#input()
print('distance filter done!')
df4=df4.reset_index(drop=True)
df7=distance(df4)
df6 = pd.concat([df4, df7], axis=1, sort=False)
df6.to_csv(obj+'-df7.csv')
df5=knn_density(df4,df6)
df5.to_csv(obj +'-knn k=10.csv')
