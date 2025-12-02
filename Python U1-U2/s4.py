from datetime import datetime, time
import sys 


print(f"The current day is {datetime.now().strftime("%w")}")

# %d-day of the month
# %j- day of the year {3 digits 1 to 365}
# %b %B- month name(abbr, Full)
# %m- month of the year

#__________ACCESSING SYSTEM INFO___________

print(f'The python version {sys.version}') #----version

print(f'The Operating System is {sys.platform}') #------OS Details

print("Enter the username:")
u_name=sys.stdin.readline().rstrip('\n')    #Equivalent to u_name=input("Enter the username")
sys.stdout.write(u_name+"\n\n")             #Equivalent print(u_name); print('\n')
sys.stderr.write('This is error message') #Exception Handling

#Get the size of var

n=1234567890
l=[1,2,3,4,5,6,7,8,9,0]
l1=['1','2','3','4','5','6','7','8','9','0']
s={1,2,3,4,5,6,7,8,9,0}
s1={'1','2','3','4','5','6','7','8','9','0'}
t=(1,2,3,4,5,6,7,8,9,0)
t1=('1','2','3','4','5','6','7','8','9','0')
d={1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:0}
d1={'1':'2','2':'3','3':'4','4':'5','5':'6','6':'7','7':'8','8':'9','9':'0'}
d2={1:'2',2:'3',3:'4',4:'5',5:'6',6:'7',7:'8',8:'9',9:'0'}


print(f'The size of {n} is {sys.getsizeof(n)} bytes')
print(f'The size of {l} is {sys.getsizeof(l)} bytes')
print(f'The size of {l1} is {sys.getsizeof(l1)} bytes')
print(f'The size of {s} is {sys.getsizeof(s)} bytes')
print(f'The size of {s1} is {sys.getsizeof(s1)} bytes')
print(f'The size of {t} is {sys.getsizeof(t)} bytes')
print(f'The size of {t1} is {sys.getsizeof(t1)} bytes')
print(f'The size of {d} is {sys.getsizeof(d)} bytes')
print(f'The size of {d1} is {sys.getsizeof(d1)} bytes')
print(f'The size of {d2} is {sys.getsizeof(d2)} bytes')

sys.exit(1)

