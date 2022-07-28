import matplotlib.pyplot as plt
import datetime
import pandas as pd
import numpy as np

def sumtime(timeList):
       mysum = datetime.timedelta()
       for i in timeList:
           (h, m, s) = i.split(':')
           d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
           mysum += d
       return (str(mysum))

def points(time, temp):
    elementos = (pd.date_range("00:00:00", time, freq="1S").strftime('%H:%M:%S'))
    rangetime = pd.date_range("00:00:00", elements, periods=len(elementos)).strftime('%H:%M:%S')
    for x in range(len(rangetime)):
        temperature_list.append(temp)

#################################################
duration_list = ['00:05:00','00:07:00', '00:05:00', '00:05:00', '00:05:00', '00:05:00', '00:05:00']
temperaturas = [22.852642, 40.16478166666666, 31.643010000000004, 32.852642, 33.16478166666666, 31.643010000000004]

elements = sumtime(duration_list)

###############################################

temperature_list = []

while len(temperaturas)>0:
    points(duration_list[0],temperaturas[0])
    duration_list.pop(0)
    temperaturas.pop(0)

################################################
rangeTime = pd.date_range("00:00:00", elements, periods=len(temperature_list)).strftime('%H:%M:%S')

print('rangetime',rangeTime)
###############################################

y=temperature_list
x=rangeTime

fig, ax = plt.subplots()
fig.autofmt_xdate()

ax.plot(x, y)

ax.set(xlabel='Tempo', ylabel='Temperatura (°C)',
       title='DTS - Temperatura por Tempo')

start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end,357))

ax.grid()
plt.show()





