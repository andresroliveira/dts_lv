import matplotlib.pyplot as plt
import numpy as np
import re
import datetime
import pandas as pd
from os import listdir
from os.path import isfile, join


#-----------------------------------
def floter(x,Fx):
    while len(x) >> 0:
        Fx.append(float(x[0]))
        x.pop(0)

def cleanMT(origin, LM, LT):
    for x in origin:
        a = list(x.replace("\t", "@"))
        a = a[:-2]
        b = ''.join(a)
        c = b.split('@')
        LM.append(c[0])
        LT.append(c[1])

def clean(term):
    return re.sub("[^\d\.]", "", term)

def sumtime(timeList):
    mysum = datetime.timedelta()
    for i in timeList:
        (h, m, s) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        mysum += d
    return (str(mysum))

def points(time, temp):
    time = len(pd.date_range("00:00:00", sumtime(duration_list), freq="1S").strftime('%H:%M:%S'))
    for x in range(time):
        temperature_list.append(temp)

#-----------------------------------
#localiza os logs
#mypath = "C:\\Users\\Usuario\AppData\Local\Programs\Editor - Programação\Saved Programs python\LabPetro"
mypath = "C:\\Pycharm\Projeto - Labpetro"

a = [f for f in listdir(mypath) if isfile(join(mypath, f))]
b = []
for item in a:
    if ".txt" in item:
        b.append(item)
#-----------------------------------
#sequencia de logs
st = sorted(b)
#-----------------------------------

temperaturas = []
temperature_list = []
duration_list = []
data_list = []
hora_list = []
while len(st) > 0:
    #-----------------------------------
    #Abertura do log
    with open(st[0]) as f:
        lines = f.readlines()

    #-----------------------------------
    #Pescar linha especifica
    list_lines = (list(lines))

    # -----------------------------------
    # Data e hora
    data = clean(list_lines[10])[:-6]
    data_list.append(data)
    hora = clean(list_lines[10])[8:]
    hora_list.append(hora)


    # -----------------------------------
    # Duração esegundos convertida para minutos
    duration = str(datetime.timedelta(seconds=float(clean(list_lines[11]))))
    duration_list.append(duration[:-7])

    #-----------------------------------
    #remoção de cabeçalho
    del list_lines[0:41]
    #-----------------------------------
    #separa as colunas de Temperatura x Metro
    list_T = []
    list_M = []

    cleanMT(list_lines,list_M,list_T)

    #-----------------------------------
    FT = []
    FM = []

    T = floter(list_T,FT )
    M = floter(list_M,FM)

    #-----------------------------------
    #determina o range de espaço
    ini = 6
    fim = 7
    # section
    lista_sM = []
    lista_sT = []

    for x in FM:
        location = []
        if x >= ini and x <= fim + 1:
            lista_sM.append(x)
            location.append(FM.index(x))
        for y in location:
            lista_sT.append(FT[y])

    temperaturas.append(np.mean(lista_sT))
    #-----------------------------------
    #elimna log usado
    st.pop(0)

#-----------------------------------
print(temperaturas)
print(duration_list)
print(data_list)
print(hora_list)
#-----------------------------------

#-----------------------------------
elements = sumtime(duration_list)
#-----------------------------------
#determina a largura da barra no grafico

while len(temperaturas)>0:
    points(duration_list[0],temperaturas[0])
    duration_list.pop(0)
    temperaturas.pop(0)

#-----------------------------------
#determina o eixo X
rangeTime = pd.date_range("00:00:00", elements, periods=len(temperature_list)).strftime('%H:%M:%S')
print('range', rangeTime)
#-----------------------------------

y=temperature_list
x=rangeTime

fig, ax = plt.subplots()
fig.autofmt_xdate()

ax.plot(x, y)
ax.set(xlabel='Tempo', ylabel='Temperatura (°C)',
       title='DTS - Temperatura por Tempo')

start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end,40))

ax.grid()
plt.show()



