"""
Author: Adarsh Bulusu 
Type B
"""
#import all libraries needed here
import pandas as pd 
import re
import csv


#create the dataframe out of the large planers dataset s
df=pd.read_csv('/Users/adarshbulusu/Desktop/FRP /planets.csv',low_memory=False)



A_indexes = [] #list to hold the values to where Type A planets area
for x in df['st_spstr']:
    if(re.search("A",str(x)[0])):
        pos=df[df['st_spstr'] == str(x)].index[0]
        A_indexes.append(pos)
        
f = open('/Users/adarshbulusu/Desktop/FRP /TypeA.csv','w')
with f:
    writer = csv.writer(f)
    writer.writerow(df.columns)
    for val in A_indexes:
        writer.writerow(df.iloc[val])

    

    