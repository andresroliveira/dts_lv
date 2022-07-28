import matplotlib.pyplot as plt
import numpy as np
import re
import datetime
import pandas as pd
from os import listdir
from os.path import isfile, join

VERBOSE = True


def cleanMT(origin, LM, LT):
    for x in origin:
        a = list(x.replace("\t", "@"))
        a = a[:-2]
        b = ''.join(a)
        c = b.split('@')
        LM.append(float(c[0]))
        LT.append(float(c[1]))


def clean(term):
    return re.sub("[^\d\.]", "", term)


def sum_time(timeList):
    mysum = datetime.timedelta()
    for i in timeList:
        (h, m, s) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        mysum += d
    return str(mysum)


def get_time():
    return len(
        pd.date_range("00:00:00", sum_time(duration_list),
                      freq="1S").strftime('%H:%M:%S'))


def points(time, temp):
    time = get_time()
    for _ in range(time):
        temperature_list.append(temp)


########### main #############3

#-----------------------------------
#localiza os logs
#mypath = "C:\\Users\\Usuario\AppData\Local\Programs\Editor - Programação\Saved Programs python\LabPetro"
# mypath = "C:\\Pycharm\Projeto - Labpetro"

mypath = '.'

a = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# print(a)
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

for st0 in st:

    #-----------------------------------
    #Abertura do log
    with open(st0, encoding='iso-8859-1') as f:
        lines = f.readlines()

    #-----------------------------------
    #Pescar linha especifica
    list_lines = list(lines)

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
    FT = []
    FM = []

    cleanMT(list_lines, FM, FT)

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
if VERBOSE:
    print(temperaturas)
    print(duration_list)
    print(data_list)
    print(hora_list)
#-----------------------------------

#-----------------------------------
elements = sum_time(duration_list)

#-----------------------------------
#determina a largura da barra no grafico

for i in range(len(temperaturas)):
    points(duration_list[i], temperaturas[i])

#-----------------------------------
#determina o eixo X
rangeTime = pd.date_range("00:00:00", elements,
                          periods=len(temperature_list)).strftime('%H:%M:%S')
if VERBOSE:
    print('range', rangeTime)
#-----------------------------------

y = temperature_list
x = rangeTime

fig, ax = plt.subplots()
fig.autofmt_xdate()

ax.plot(x, y)
ax.set(xlabel='Tempo',
       ylabel='Temperatura (°C)',
       title='DTS - Temperatura por Tempo')

start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 40))

ax.grid()
plt.show()
