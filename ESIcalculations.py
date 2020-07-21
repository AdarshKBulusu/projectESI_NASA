
""" 
Author: Adarsh Bulusu 
""" 
#import all needed libraries
import pandas as pd
import numpy as np
import warnings
import math


df = pd.read_csv('/Users/adarshbulusu/Desktop/school/planets.csv',low_memory=False)
'''
Our T value will be 0.8 and m will be 1 as per the orignial stats used back in 2016
'''
#Get ESI(S) Through ESI(T) and ESI(e)


def esi_t(upper, lower, flat):
    t = 0.8
    e_temp = 288
    p = ((e_temp - upper) / e_temp) * 100
    q = ((lower - e_temp) / e_temp) * 100
    
    wa = abs((np.log(t) / np.log(1 - (p / (200 - p)))))
    wb = abs((np.log(t) / np.log(1 - (q / (200 + q)))))
    
    wx = (wa * wb) ** 0.5
    esi_t = (1 - abs((flat - e_temp) / (flat + e_temp))) ** wx
    return esi_t



def esi_e(true_mass,true_rad, upper_mass_e, lower_mass_e,upper_rad_e,lower_rad_e):
    t = 0.8
    uni_G = (6.67)* (10 ** -11)
    earth_v = 11186
    mass1 = (true_mass * 5.972) * (10 ** 24)
    rad1 = (true_rad * 6.371) * (10 ** 6)
    g = (mass1 * uni_G) / (rad1 ** 2)
    ve = math.sqrt(abs(2 * g * rad1)) #real value
    
    mass2 = (upper_mass_e * 5.972) * (10 ** 24)
    rad2 = (upper_rad_e * 6.371) * (10 ** 6)
    g2 = (mass2 * uni_G) / (rad2 ** 2)
    upper_ve = math.sqrt(abs(2 * g2 * rad2))
    
    mass3 = (lower_mass_e * 5.972) * (10 ** 24)
    rad3 = (lower_rad_e * 6.371) * (10 ** 6)
    g3 = (mass3 * uni_G) / (rad3 ** 2)
    lower_ve = math.sqrt(abs(2 * g3 * rad3))
    
    
    
    
    
    p = ((earth_v - upper_ve) / earth_v) * 100
    q = ((lower_ve - earth_v) / earth_v) * 100
    
    wa = abs((np.log(t) / np.log(1 - (p / (200 - p)))))
    wb = abs((np.log(t) / np.log(1 - (q / (200 + q)))))
    
    wx = (wa * wb) ** 0.5
    esi_e = (1 - abs((ve - earth_v) / (ve + earth_v))) ** wx
    return esi_e
    
    
    
    
    


if __name__ == "__main__":
    
    warnings.filterwarnings("ignore", category = RuntimeWarning)
    for i in range(0,len(df)):
        upper_t = df.loc[i]['pl_eqt'] + df.loc[i]['pl_eqterr1']
        lower_t = df.loc[i]['pl_eqt'] + df.loc[i]['pl_eqterr2']
        flat_t = df.loc[i]['pl_eqt']
        
        
        true_mass = df.loc[i]['pl_bmasse'] 
        true_rad = df.loc[i]['pl_rade']
        
        upper_mass_e = df.loc[i]['pl_bmasse'] + df.loc[i]['pl_bmasseerr1']
        lower_mass_e = df.loc[i]['pl_bmasse'] + df.loc[i]['pl_bmasseerr2']
        
        upper_rad_e =  df.loc[i]['pl_rade'] + df.loc [i]['pl_radeerr1']
        lower_rad_e = df.loc[i]['pl_rade'] +df.loc[i]['pl_radeerr2']
        
        #if not(str(esi_t(upper_t,lower_t,flat_t)) == 'nan'):
        #    print("The ESI(T) value of {} is ".format(df.loc[i]['pl_hostname']) + str(round(esi_t(upper_t,lower_t,flat_t),3)))

        #if not(str(esi_e(true_mass, true_rad, upper_mass_e, lower_mass_e, upper_rad_e, lower_rad_e)) == 'nan'):
        #    print("The ESI(E) value of {} is ".format(df.loc[i]['pl_hostname']) + str(round(esi_e(true_mass, true_rad, upper_mass_e, lower_mass_e, upper_rad_e, lower_rad_e),3)))
        
        
        if not(str(esi_t(upper_t,lower_t,flat_t)) == 'nan') and not(str(esi_e(true_mass, true_rad, upper_mass_e, lower_mass_e, upper_rad_e, lower_rad_e)) == 'nan'):
            esi_f = (esi_e(true_mass, true_rad, upper_mass_e, lower_mass_e, upper_rad_e, lower_rad_e) * esi_t(upper_t,lower_t,flat_t)) ** 0.5
            if esi_f >= 0.8:
                print("{}".format(df.loc[i]['pl_name']) + " ESI(F): " + str(round(esi_f,3)))
    
        
        
        
        
        

 
    
        



    





    






    




