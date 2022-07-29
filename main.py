import numpy as np
from LeituraDados import *
from GerarEixos import gerar_eixos
from GerarGrafico import gerar_grafico


def main():
    duracoes, temperaturas = leitura_dados_dts()

    # legendas em pontos específicos (durações)
    # pos = np.concatenate(([0], np.cumsum(duracoes)))

    # legendas com distanciamento de 3 min
    # pos = np.arange(0, np.sum(duracoes), 3 * 60)

    # 10 legendas igualmente espaçadas
    pos = np.linspace(0, np.sum(duracoes), 10)

    t, T_step = gerar_eixos(duracoes, temperaturas)
    T_cont, pres = leitura_dados_lv(t)

    gerar_grafico(t, T_step, T_cont, pres, pos)


if __name__ == '__main__':
    main()