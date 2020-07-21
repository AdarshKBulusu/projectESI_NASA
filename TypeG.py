"""
Author: Adarsh Bulusu 
"""
#import all libraries needed here
import pandas as pd 
import re
import csv


#create the dataframe out of the large planers dataset s
df=pd.read_csv('/Users/adarshbulusu/Desktop/FRP /planets.csv',low_memory=False)


indexes = [] #list to hold the values to where Type A planets area
for x in df['st_spstr']:
    if(re.search("G",str(x)[0])):
        pos=df[df['st_spstr'] == str(x)].index[0]
        indexes.append(pos)
        
f = open('/Users/adarshbulusu/Desktop/FRP /TypeG.csv','w')
with f:
    writer = csv.writer(f)
    writer.writerow(df.columns)
    for val in indexes:
        writer.writerow(df.iloc[val])



    
        