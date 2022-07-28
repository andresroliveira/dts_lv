import matplotlib.pyplot as plt
import numpy as np
import time


def gerar_grafico(t, T, pos):

    plt.figure(figsize=(16, 9))
    plt.plot(t, T)

    plt.xlabel('Tempo')
    plt.ylabel('Temperatura (°C)')
    plt.title('DTS - Temperatura por Tempo')

    legend = [time.strftime('%H:%M:%S', time.gmtime(ti)) for ti in pos]
    plt.xticks(pos, labels=legend, rotation=45)
    plt.grid()
    plt.show()