import matplotlib.pyplot as plt
import time
import pandas as pd
import numpy as np


def to_second(form):
    h, m, s = map(int, form.split(':'))
    return h * 60 * 60 + m * 60 + s


def get_axis(duration_list, temperaturas):
    total_time = sum(duration_list)

    t = np.array([float(i) for i in range(total_time + 1)])
    T = np.zeros_like(t)

    cur_time = 0
    old_time = 0

    for i in range(len(temperaturas)):
        cur_time += duration_list[i]
        T[old_time:cur_time + 1] = temperaturas[i]
        old_time = cur_time

    # t_time = [time.strftime('%H:%M:%S', time.gmtime(ti)) for ti in t]
    # t_time = pd.DatetimeIndex(t_time).strftime('%H:%M:%S')

    return t, T


def main():
    #################################################
    duration_list = [
        '00:05:00', '00:07:00', '00:05:00', '00:05:00', '00:05:00', '00:05:00',
        '00:05:00', '00:05:00', '00:07:00', '00:05:00', '00:07:00'
    ]
    duration_list = list(map(to_second, duration_list))
    temperaturas = [
        22.852642, 40.16478166666666, 31.64301, 32.852642, 33.16478166666666,
        31.64301, 32, 31.64301, 32.852642, 31.64301, 32.852642
    ]

    t, T = get_axis(duration_list, temperaturas)
    plt.figure(figsize=(16, 9))
    plt.plot(t, T)

    plt.xlabel('Tempo')
    plt.ylabel('Temperatura (°C)')
    plt.title('DTS - Temperatura por Tempo')

    pos = np.cumsum(duration_list)
    legend = [time.strftime('%H:%M:%S', time.gmtime(ti)) for ti in pos]
    plt.xticks(pos, labels=legend, rotation=45)
    plt.grid()
    plt.show()

    # fig, ax = plt.subplots()
    # fig.autofmt_xdate()

    # ax.plot(t, T)

    # ax.set(xlabel='Tempo',
    #        ylabel='Temperatura (°C)',
    #        title='DTS - Temperatura por Tempo')

    # start, end = ax.get_xlim()
    # ax.xaxis.set_ticks(np.arange(start, end, 357))

    # ax.grid()
    # plt.show()

    # ################################################
    # rangeTime = pd.date_range(
    #     "00:00:00", elements,
    #     periods=len(temperature_list)).strftime('%H:%M:%S')

    # print('rangetime', rangeTime)
    # ###############################################

    # y = temperature_list
    # x = rangeTime

    # print(x, y)

    ###############################################
    # temperature_list = []

    # for i in range(len(temperaturas)):
    #     time = duration_list[i]
    #     temp = temperaturas[i]

    #     elementos = pd.date_range("00:00:00", time,
    #                               freq="1s").strftime('%h:%m:%s')
    #     rangetime = pd.date_range("00:00:00", elements,
    #                               periods=len(elementos)).strftime('%h:%m:%s')

    #     temperature_list += [temp for _ in range(len(rangetime))]

    # print(len(temperature_list))


if __name__ == '__main__':
    main()