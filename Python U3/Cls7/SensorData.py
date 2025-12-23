#Simulation of sensor

# %%

import random as r
import time as t

for i in range(50):
    t_c=25+r.uniform(-2,2)
    print(f"Reading {i+1}: {t_c:.3f} C")
    t.sleep(0) #1sec delay

#Simulate a virtual sensor

import random as r 
import time as t
import csv

with open('sensor_read.csv','w', newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['Timestamp','Temperature'])
    #Colum headers are created for the csv fle
    for i in range(50):
        ts=t.time() #current time is captured in sec from Unix epoch time   .... Float val
        t_c=25+r.uniform(-2,2)#random temperature is being generated
        writer.writerow([ts,f'{t_c:2f}'])
        print(ts,t_c)
        t.sleep(0.5)



#-----------------------------------------
#      Visualization of the readings
#-----------------------------------------

import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('sensor_read.csv')
print(df.shape)
#convert the str to numeric data
print(df.columns)
df['Timestamp']=pd.to_numeric(df['Timestamp'],errors='coerce')

print(df.dtypes)

#convert timestamp to standart format
df['Timestamp']=pd.to_datetime(df['Timestamp'],unit='s') #unit=s tels the pandas that the numbers represent the seconds
print(df.head())





print(plt.figure())
print(plt.plot(df['Timestamp'],df['Temperature']))
plt.xlabel('Time')
plt.ylabel('Temperature (C)')
plt.title('Raw Sensor Data')
plt.xticks(rotation=45)
plt.tight_layout()
print(plt.show())

