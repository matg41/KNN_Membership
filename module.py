import numpy as np
import scipy as sc
import pandas as pd
#import matplotlib.pyplot as plt
from scipy import pi
#import astropy as asp
from tqdm.auto import tqdm
import math
#from Mass import Mass

def distance(df4):
    df7 = pd.DataFrame()
    Rt = []
    R20 = []
    for i in tqdm(range(len(df4['ra'])), position=0, leave=True):
        #if i%10==0:
            #print(i)
        Rt1 = []
        Rt2 = []
        df7[df4['source_id'][i]] = np.zeros((len(df4['ra'])))

        if i > 0:
            Rt1 = np.array(df7.iloc[i][0:i])
        for j in range(i, len(df4['ra'])):
            r = ((df4['r_med_photogeo'][i] / 2) + (df4['r_med_photogeo'][i] / 2))
            a = (df4['ra'][i] - df4['ra'][j])*(pi/180)
            b = (df4['dec'][i] - df4['dec'][j])*(pi/180)
            c = (df4['r_med_photogeo'][i] - df4['r_med_photogeo'][j])
            R = (((a * r) ** 2) + ((b * r) ** 2) + (c ** 2)) ** 0.5
            Rt1 = np.append(Rt1, R)
        df7[df4['source_id'][i]] = Rt1
    print('distance done!')
    return df7

def knn_density(df4,df6):
    df5 = pd.DataFrame(columns=['source_id','R_10','Mt','Ro_10'])
    dist_two=[]
    for i in tqdm(range(len(df4['source_id'])), position=0, leave=True):
        a=df6['source_id'][i]

        #R=df6[str(df6['source_id'][i])]
        R_20=0
        Mt=0
        Ro_20=0
        dist_two=list(df6[a])
        print(i)
        for n in range(11):
            for k in range(len(dist_two)):
                #print(k)
                #print(k," ",np.min(R)," ",R[k])
                if (dist_two[k]==min(dist_two)):
                    #print('chek',min(dist_two))
                    #print('   ',df6[a][k])
                    v=k
                    Mt=Mt+df6['Mass'][v]
                    if n==10:
                        R_20=float(dist_two[v])
                        Ro_20=(Mt/(pi*(R_20**3)*4/3))
                        
                    dist_two[v]=10000
                    #print(Mt)
                    break

        #print(df6['source_id'][i], R_20, Mt, Ro_20)
        df5 = df5.append({'source_id':str(df6['source_id'][i]), 'R_10':R_20, 'Mt':Mt, 'Ro_10':Ro_20},ignore_index=True)
        #if(i%100==0):
            #print(i)
        #print(df5)
    print('density done')
    return df5



