'''
Sarvagya Ranjan
'''

from itertools import count
from matplotlib.animation import FuncAnimation
import csv
import pandas as pd
import matplotlib.pyplot as plt
import time

#for obtaining the date on label
date = time.localtime().tm_mday
month = time.localtime().tm_mon
year = time.localtime().tm_year
date_Arr = (str(date)+'/'+str(month)+'/'+str(year))
def animate (i):
#read csv data using panda
  data = pd.read_csv("C:/Users/DELL/AppData/Local/Programs/Python/Python311/real_time_data.csv")
 x = data["Time"]
 y1 = data["Temperature"]
 y2 = data["Set-Point"]
#plotting parameters
 plt.cla() #clear axis
 plt.plot(x,y1, 'r-o', label = ("Temperature" +" " + date_Arr))
 plt.xlabel("Time", fontsize = 10)
 plt.ylabel("Temperature in °C", fontsize = 10)
 plt.title("Temperature °C vs Time (Real-Time Analysis)", fontsize = 15)
 plt.legend()
 ani = FuncAnimation(plt.gcf(), animate, interval = 2000)
 plt.tight_layout()
 plt.show()
