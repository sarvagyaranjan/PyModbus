'''
Sarvagya Ranjan
'''
from pymodbus.client import ModbusTcpClient
import time
import csv
host = '192.172.100.91' #ip adress of gateway
port = 502
#communication between client and server
client = ModbusTcpClient(host, port)
client.connect()

#header of csv file for real-time analysis
fieldnames = ["Date","Time","Temperature","Set-Point”]
with open ("C:/Users/DELL/AppData/Local/Programs/Python/Python311/real_time_data.csv", 'w') as csv_file:
  csvwriter = csv.writer(csv_file)
  csvwriter.writerow(fieldnames)

while True:
#read the holding registers
  rr = client.read_holding_registers(0x7D2, 2, unit = 3)
  time.sleep(10)
  print(rr)
#print(rr.registers)
  t = rr.registers[0]
  sp = rr.registers[1]
  temp = t/10
  setp = sp/10
#date and time of when the reading is taken from the sensor
  date = time.localtime().tm_mday
  month = time.localtime().tm_mon
  year = time.localtime().tm_year
  hrs = time.localtime().tm_hour
  mins = time.localtime().tm_min

  secs = time.localtime().tm_sec
  date_Arr = (str(date)+'/'+str(month)+'/'+str(year))
  time_Arr = (str(hrs) + ':' + str(mins) + ':' + str(secs))

   info = {
  "Date”:date_Arr,
  "Time”:time_Arr,
  "Temperature": temp,
  "Setpoint”:setp
  }
#real_time analysis csv file

with open("C:/Users/DELL/AppData/Local/Programs/Python/Python311/real_time_data.csv", 'a') as csv_file:

  writer = csv.writer(csv_file, delimiter = ',')
  writer.writerow([date_Arr, time_Arr, temp,setp])
#all time data csv file
with open ("C:/Users/DELL/AppData/Local/Programs/Python/Python311/all_time_data.csv", 'a') as csv_file:
  writer = csv.writer(csv_file, delimiter = ',')
  writer.writerow([info])
