import serial
from firebase import firebase
from time import sleep
from datetime import datetime
import serial.tools.list_ports


ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
        print("{}: {} [{}]".format(port, desc, hwid))


ser = serial.Serial("COM2", 9600)
print(ser.readline())
res =1
i=0
time=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(time)

while res:
     cc=str(1234)
     print(cc)
     val=cc
     firebase1 = firebase.FirebaseApplication('https://test-1-36363-default-rtdb.firebaseio.com/', None)
     
     for i in range(0,4):
             #string1="123"
             string1=str(ser.readline())
             string1=string1[9:][:-7]
             string1=int(string1)
             data =  { 'date': datetime.now().strftime("%Y-%m-%d"),
               'reading':string1,
               'time': datetime.now().strftime("%H:%M")               
          }
             result = firebase1.patch('https://test-1-36363-default-rtdb.firebaseio.com/'+ '/Noise Value(dB)/'+ str(i), data)
             print(result)
     res=0


