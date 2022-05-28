#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re


def make_csv(name_input, name_output):
    

    fid = open(name_input, 'r')

    
    
    pattern = '[-]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9]';
    pattern_a = '[-]?[0-9][0-9]?[0-9]?[0-9]?[0-9]?';
    pattern_b = '[-]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9]?[0-9]';  #тут завсит от того, какими большими будут числа - увеличить при необходимости
    pattern_1 = 'MaxNoise:';
    pattern_2 = 'StdNoise:';
    pattern_3 = 'FirstPathAmp1:';
    pattern_4 = 'FirstPathAmp2:';
    pattern_5 = 'FirstPathAmp3:';
    pattern_6 = 'MaxGrowthCIR:';
    pattern_7 = 'RxPreamCount:';
    pattern_8 = 'FirstPath:';
    pattern_9 = 'RxTimeStamp:';
    pattern_10 = 'Counter:';
    pattern_11 = 'SFD:';
#re = zeros(len(fid));
    Master_real = [];
    Master_imag = [];
    Slave_real = [];
    Slave_imag = [];
    MaxNoise_master = [];
    MaxNoise_slave = [];
    StdNoise_master = [];
    StdNoise_slave = [];
    FirstPathAmp1_master = [];
    FirstPathAmp1_slave = [];
    FirstPathAmp2_master = [];
    FirstPathAmp2_slave = [];
    FirstPathAmp3_master = [];
    FirstPathAmp3_slave = [];
    MaxGrowthCIR_master = [];
    MaxGrowthCIR_slave = [];
    RxPreamCount_master = [];
    RxPreamCount_slave = [];
    FirstPath_master = [];
    FirstPath_slave = [];
    RxTimeStamp_1_master = [];
    RxTimeStamp_2_master = [];
    RxTimeStamp_1_slave = [];
    RxTimeStamp_2_slave = [];
    Counter = [];
    SFD_master = [];
    SFD_slave = [];


    count = 0;
    count_master_slave = 0;


    for line in fid:
        indicator = re.findall(pattern_1, line)
        #print(line)
        indicator_2 = re.findall(pattern_2, line)
    #print(line)
        indicator_3 = re.findall(pattern_3, line)
        indicator_4 = re.findall(pattern_4, line)
        indicator_5 = re.findall(pattern_5, line)
        indicator_6 = re.findall(pattern_6, line)
        indicator_7 = re.findall(pattern_7, line)
        indicator_8 = re.findall(pattern_8, line)
        indicator_9 = re.findall(pattern_9, line)
        indicator_10 = re.findall(pattern_10, line)
        indicator_11 = re.findall(pattern_11, line)
    
        indicator_spec_1 = re.findall('Master:', line)
        indicator_spec_2 = re.findall('Slave:', line)
    #print(indicator)
        if indicator == [pattern_1]:
            count = 2
        #print(count)
        elif indicator_2 == [pattern_2]:
            count = 3
        #print(count)
        elif indicator_3 == [pattern_3]:
            count = 4
        #print(count)
        elif indicator_4 == [pattern_4]:
            count = 5
        elif indicator_5 == [pattern_5]:
            count = 6
        elif indicator_6 == [pattern_6]:
            count = 7
        elif indicator_7 == [pattern_7]:
            count = 8
        elif indicator_8 == [pattern_8]:
            count = 9
        elif indicator_9 == [pattern_9]:
            count = 10
        elif indicator_10 == [pattern_10]:
            count = 12
        elif indicator_11 == [pattern_11]:
            count = 13
        
        elif indicator_spec_1 == ['Master:']:
            count = 1
            count_master_slave = 1
        elif indicator_spec_2 == ['Slave:']:
            count = 11
            count_master_slave = 2
        
    #else:
        #count = 0
        
    #print(count)
    
        if count == 1:
            geo_valuses = re.findall(pattern, line)
        #print(geo_valuses)
            if len(geo_valuses) > 1:
                Master_real.append(int(geo_valuses[0]))
                Master_imag.append(int(geo_valuses[1]))
            
            
        elif count == 2:
        
            geo_valuses = re.findall(pattern, line)
            if count_master_slave == 1:
                MaxNoise_master.append(geo_valuses[0])
            
            elif count_master_slave == 2:
                MaxNoise_slave.append(geo_valuses[0])
            
        elif count == 3:
            geo_valuses = re.findall(pattern, line)
            if count_master_slave == 1:
                StdNoise_master.append(geo_valuses[0])
            
            elif count_master_slave == 2:
                StdNoise_slave.append(geo_valuses[0]) 
            
        elif count == 4:
            geo_valuses = re.findall(pattern_a, line)
            #print(geo_valuses[0])
            if count_master_slave == 1:
                FirstPathAmp1_master.append(geo_valuses[0])
        
            elif count_master_slave == 2:
                FirstPathAmp1_slave.append(geo_valuses[0])
            
            
        elif count == 5:
        
            geo_valuses = re.findall(pattern_a, line)
            if count_master_slave == 1:
                FirstPathAmp2_master.append(geo_valuses[0])
        
            elif count_master_slave == 2:
                FirstPathAmp2_slave.append(geo_valuses[0])
            
        elif count == 6:
        
            geo_valuses = re.findall(pattern_a, line)
            if count_master_slave == 1:
                FirstPathAmp3_master.append(geo_valuses[0])
        
            elif count_master_slave == 2:
                FirstPathAmp3_slave.append(geo_valuses[0])
            
        elif count == 7:
        
            geo_valuses = re.findall(pattern, line)
            if count_master_slave == 1:
                MaxGrowthCIR_master.append(geo_valuses[0])
        
            elif count_master_slave == 2:
                MaxGrowthCIR_slave.append(geo_valuses[0])
            
            
        elif count == 8:
        
            geo_valuses = re.findall(pattern, line)
            if count_master_slave == 1:
                RxPreamCount_master.append(geo_valuses[0])
        
            elif count_master_slave == 2:
                RxPreamCount_slave.append(geo_valuses[0])
            
        elif count == 9:
        
            geo_valuses = re.findall(pattern, line)
            if count_master_slave == 1:
                FirstPath_master.append(geo_valuses[0])
        
            elif count_master_slave == 2:
                FirstPath_master.append(geo_valuses[0])
            
        elif count == 10:
        
            geo_valuses = re.findall(pattern_b, line)
            if len(geo_valuses) > 1:
                if count_master_slave == 1:
                    RxTimeStamp_1_master.append(geo_valuses[0])
                    RxTimeStamp_2_master.append(geo_valuses[1])
                elif count_master_slave == 2:
                    RxTimeStamp_1_slave.append(geo_valuses[0])
                    RxTimeStamp_2_slave.append(geo_valuses[1])
      
        elif count == 11:
            geo_valuses = re.findall(pattern, line)
        
            if len(geo_valuses) > 1:
                Slave_real.append(int(geo_valuses[0]))
                Slave_imag.append(int(geo_valuses[1]))
            #print(len(geo_valuses))
            
        elif count == 12:
            geo_valuses = re.findall(pattern_b, line)
            Counter.append(geo_valuses)
        
        elif count == 13:
        
            geo_valuses = re.findall(pattern, line)
            if count_master_slave == 1:
                SFD_master.append(geo_valuses)
        
            elif count_master_slave == 2:
                SFD_slave.append(geo_valuses)
            
    
    
    
    #if line == ['Master:']:
        #count = 1
        #count_master_slave = 1
    #elif line == ['Slave:']:
        #count = 11
        #count_master_slave = 2
    
    
    fid.close()


    Master_real = np.asarray(Master_real)
    Master_imag = np.asarray(Master_imag)
    Slave_real = np.asarray(Slave_real)
    Slave_imag = np.asarray(Slave_imag)
    plt.figure(figsize = (10, 7))
    plt.plot(np.abs(Master_real + 1j*Master_imag))
    plt.grid()
    plt.title('Master')
    plt.xlabel('Samples')
    plt.ylabel('The module of the complex amplitude')
    plt.show()


    plt.figure(figsize = (10, 7))
    plt.plot(np.abs(Slave_real + 1j*Slave_imag))
    plt.grid()
    plt.title('Slave')
    plt.xlabel('Samples')
    plt.ylabel('The module of the complex amplitude')
    plt.show()

#print(Master_real)

    Slave_real = Slave_real[0:len(Master_real)]
    Slave_imag = Slave_imag[0:len(Master_imag)]

#Save data in csv file
#Master_real = np.expand_dims(Master_real, axis = 1)
#Master_imag = np.expand_dims(Master_imag, axis = 1)
#Slave_real = np.expand_dims(Slave_real, axis = 1)
#Slave_imag = np.expand_dims(Slave_imag, axis = 1)

#table = pd.DataFrame([Master_real, Master_imag, Slave_real, Slave_imag]).T

    dictionary = {'Var1' : Master_real, 'Var2' : Master_imag, 'Var3' : Slave_real, 'Var4' : Slave_imag}

    table = pd.DataFrame(data = dictionary)

    table.to_csv(name_output, index = False)

    table.head()

    
    
#make_csv('13.04_test1.txt', 'SaveFile2.csv')
    


# In[ ]:




