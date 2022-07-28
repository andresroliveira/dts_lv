from numpy import cumsum
from LeituraDados import leitura_dados
from GerarEixos import gerar_eixos
from GerarGrafico import gerar_grafico


def main():
    duracoes, temperaturas = leitura_dados()
    t, T = gerar_eixos(duracoes, temperaturas)
    gerar_grafico(t, T, cumsum(duracoes))


if __name__ == '__main__':
    main()