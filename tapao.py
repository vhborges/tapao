# standard modules
from random import shuffle
from itertools import cycle
from threading import Lock, Event, Thread

# project modules
import teclado
import tela
import baralho

# Carta falada pelos jogadores a cada rodada
carta_atual = '0'

# Indicador de qual jogador pertence a rodada atual
rodada_atual = 1

def main():
    baralho_inicial = baralho.cria()
    # Embaralha o baralho aleatoriamente
    shuffle(baralho_inicial)
    # Distribui o baralho entre os jogadores
    baralho_j1 = baralho_inicial[0:26]
    baralho_j2 = baralho_inicial[26:52]
    # O monte da mesa inicia vazio
    baralho_mesa = []

    # Ordem em que as cartas serão "faladas" pelos jogadores
    ordem = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    iterador = cycle(ordem)

    # Lock para realizar a exclusão mútua entre as ações de cada jogador
    # Possui o mesmo funcionamento de um Mutex
    jogada = Lock()

    # Event para anunciar o fim do jogo às threads dos jogadores
    fim_jogo = Event()

    # Events para sincronizar a atualização da tela
    j1_pronto = Event()
    j2_pronto = Event()
    j1_pronto.set()
    j2_pronto.set()

    # Threads associadas ao teclado de cada jogador
    jogador1 = Thread(target=teclado.processa_j1,
                      args=(baralho_j1, baralho_j2, baralho_mesa, iterador, jogada, j1_pronto, fim_jogo))
    jogador2 = Thread(target=teclado.processa_j2,
                      args=(baralho_j1, baralho_j2, baralho_mesa, iterador, jogada, j2_pronto, fim_jogo))
    # Thread utilizada para atualizar a tela em momentos oportunos
    atualiza_tela = Thread(target=tela.atualiza,
                           args=(baralho_j1, baralho_j2, baralho_mesa, fim_jogo, j1_pronto, j2_pronto))

    # Inicia as threads
    jogador1.start()
    jogador2.start()
    atualiza_tela.start()

    # Aguarda até que as threads terminem sua execução
    jogador1.join()
    jogador2.join()
    atualiza_tela.join()

    ganhador = baralho.calcula_ganhador(baralho_j1, baralho_j2)
    if ganhador == None:
        print("\t\tNinguém ganhou!\n")
    else:
        print(f"\t\tO jogador {ganhador} ganhou!\n")

    # Aguarda o usuário pressionar Enter antes de finalizar o jogo
    input()

if __name__ == "__main__":
    main()
