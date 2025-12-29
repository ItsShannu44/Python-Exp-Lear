#Simulation of sensor

# %%

import random as r
import time as t

for i in range(10):
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
    for i in range(10):
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

#----------------------------------
#       Smoothened data
#----------------------------------

df['Value']=pd.to_numeric(df['Temperature'],errors='coerce')
df['Value_Smooth']=df['Value'].rolling(window=5, min_periods=1).mean() #A rolling mean is calculated
print(df.head())


plt.figure()
plt.plot(df['Timestamp'],df['Value'],label='Raw',alpha=0.5) #alpha creates the transparency of the visualization
plt.plot(df['Timestamp'],df['Value_Smooth'],label='Smoothened')
plt.xlabel("Time")
plt.ylabel("Temperature (C)")
plt.title("Raw vs Smoothened Sensor Data")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# -----------------------

#Mean of Temperature Readings

# -----------------------

print('\n===========================\n')
mid_index=len(df)//2
print(mid_index)

first_half_mean=df['Value_Smooth'].iloc[:mid_index].mean()
second_half_mean=df['Value_Smooth'].iloc[mid_index:].mean()
print(f"Mean of first half: {first_half_mean}")
print(f"Mean of second half:{second_half_mean}")

