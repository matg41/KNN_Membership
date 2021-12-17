import numpy as np
import pandas as pd
from scipy import pi
import astropy as asp
from tqdm import tqdm
import math

def Mass(m,d): #Mass estimation function
    M=m-5*(math.log(d,10)-1)
    L=10**(0.4*(4.83-M))
    if (L<=0.033):
        m=((L)**(1/2.3))/0.23
    elif(L>0.033 and L<=16):
        m=((L)**0.25)
    elif(L>16 and L<=1727418):
        m=((L)**(1/3.5))*(1/1.4)
    else:
        m=(L)*(1/32000)
    return m,M



source_file=input('source file: ')
df1=pd.read_csv(source_file)
df4=df1
df4.drop_duplicates('source_id',keep='first',inplace=True)
df4=df4.dropna(subset=['parallax'])
df4=df4.reset_index(drop=True)
del df1
df4['Mass']=np.zeros(len(df4['source_id']))
df4['A_Mag']=np.zeros(len(df4['source_id']))
print('loop begin!')
for i in tqdm(range(len((df4['source_id'])))):
    df4['Mass'][i], df4['A_Mag'][i] =Mass(df4['phot_g_mean_mag'][i],
                                          df4['r_med_photogeo'][i])

path=input('where to Mass: ')
df4.to_csv(path)
