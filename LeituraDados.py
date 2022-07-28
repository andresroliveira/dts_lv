import re
import numpy as np
from os import listdir
from os.path import isfile, join


def to_second(form):
    h, m, s = map(int, form.split(':'))
    return h * 60 * 60 + m * 60 + s


def clean(term):
    return re.sub("[^\d\.]", "", term)


def cleanMT(origin, LM, LT):
    for x in origin:
        a = list(x.replace("\t", "@"))
        a = a[:-2]
        b = ''.join(a)
        c = b.split('@')
        LM.append(float(c[0]))
        LT.append(float(c[1]))


def leitura_dados():
    # duration_list = [
    #     '00:05:00', '00:07:00', '00:05:00', '00:05:00', '00:05:00', '00:05:00',
    #     '00:05:00', '00:05:00', '00:07:00', '00:05:00', '00:07:00'
    # ]
    # duration_list = list(map(to_second, duration_list))
    # temperaturas = [
    #     22.852642, 40.16478166666666, 31.64301, 32.852642, 33.16478166666666,
    #     31.64301, 32, 31.64301, 32.852642, 31.64301, 32.852642
    # ]

    mypath = '.'

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
        # duration = str(
        #     datetime.timedelta(seconds=float(clean(list_lines[11]))))
        duration = int(float(clean(list_lines[11])))
        duration_list.append(duration)

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

    return duration_list, temperaturas


# if __name__ == '__main__':
#     duracoes, temperaturas = leitura_dados()
#     print(duracoes, temperaturas)