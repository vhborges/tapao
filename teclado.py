# custom modules
from pynput import keyboard

# project modules
import tapao

# Processa as rodadas do jogador 1 e suas batidas no monte central
def processa_j1(baralho_j1, baralho_j2, baralho_mesa, iterador, jogada, jogador_pronto, fim_jogo):
    # Função chamada quando um jogador pressiona uma tecla
    def on_press(tecla):
        # Se a tecla pressionada é um caracter alfanumérico
        if type(tecla) is keyboard.KeyCode:
            # Se o jogador efetuou a jogada
            if tecla.char == 'w':
                # Adquire o lock da jogada para exclusão mutua dos baralhos
                with jogada:
                    # Se a rodada atual é dojogador 1 e seu baralho não está vazio
                    if (tapao.rodada_atual == 1) and (len(baralho_j1) != 0):
                        tapao.carta_atual = next(iterador)
                        carta = baralho_j1.pop()
                        baralho_mesa.append(carta)
                        # Passa a rodada apenas se o adversario tiver cartas
                        if len(baralho_j2) != 0:
                            tapao.rodada_atual = 2
                        # Se ambos os jogadores estiverem sem cartas, finaliza o jogo
                        elif len(baralho_j1) == 0:
                            fim_jogo.set()
                            # Finaliza este 'listener' do teclado
                            return False
            # Se o jogador bateu no monte central
            elif tecla.char == 's':
                # Adquire o lock da jogada para exclusão mutua dos baralhos
                with jogada:
                    if len(baralho_mesa) != 0:
                        # Se o topo do monte central for igual a carta falada
                        if tapao.carta_atual == baralho_mesa[-1][1]:
                            # Se o baralho do jogador 1 estiver vazio, ele ganha o jogo
                            if len(baralho_j1) == 0:
                                fim_jogo.set()
                                # Finaliza este 'listener' do teclado
                                return False
                            else:
                                baralho_j2.extend(baralho_mesa)
                                baralho_mesa.clear()
                        # Se o jogador bateu no momento errado, ele leva as cartas da mesa
                        else:
                            baralho_j1.extend(baralho_mesa)
                            baralho_mesa.clear()
            # Se o jogador deseja encerrar o jogo
            elif tecla.char == 'q':
                fim_jogo.set()
                return False
        # Sinaliza para a thread de atualização de tela que o jogador 1 terminou a rodada
        jogador_pronto.set()

    # Adquire e inicia um 'listener' do teclado
    teclado_j1 = keyboard.Listener(on_press=on_press)
    teclado_j1.start()
    # Aguarda até que o jogo termine
    fim_jogo.wait()
    # Sinaliza a atualização da tela para a respectiva thread
    jogador_pronto.set()
    # Finaliza o 'listener' do teclado
    teclado_j1.stop()

# Processa as rodadas do jogador 2 e suas batidas no monte central
def processa_j2(baralho_j1, baralho_j2, baralho_mesa, iterador, jogada, jogador_pronto, fim_jogo):
    # Função chamada quando um jogador pressiona uma tecla
    def on_press(tecla):
        # Se a tecla pressionada é um caracter alfanumérico
        if type(tecla) is keyboard.KeyCode:
            # Se o jogador efetuou a jogada
            if tecla.char == 'k':
                # Adquire o lock da jogada para exclusão mutua dos baralhos
                with jogada:
                    # Se a rodada atual é do jogador 2 e seu baralho não está vazio
                    if (tapao.rodada_atual == 2) and (len(baralho_j2) != 0):
                        tapao.carta_atual = next(iterador)
                        carta = baralho_j2.pop()
                        baralho_mesa.append(carta)
                        # Passa a rodada apenas se o adversario tiver cartas
                        if len(baralho_j1) != 0:
                            tapao.rodada_atual = 1
                        # Se ambos os jogadores estiverem sem cartas, finaliza o jogo
                        elif len(baralho_j2) == 0:
                            fim_jogo.set()
                            # Finaliza este 'listener' do teclado
                            return False
            # Se o jogador bateu no monte central
            elif tecla.char == 'm':
                # Adquire o lock da jogada para exclusão mutua dos baralhos
                with jogada:
                    if len(baralho_mesa) != 0:
                        # Se o topo do monte central for igual a carta falada
                        if tapao.carta_atual == baralho_mesa[-1][1]:
                            # Se o baralho do jogador 2 estiver vazio, ele ganha o jogo
                            if len(baralho_j2) == 0:
                                fim_jogo.set()
                                # Finaliza este 'listener' do teclado
                                return False
                            else:
                                baralho_j1.extend(baralho_mesa)
                                baralho_mesa.clear()
                        # Se o jogador bateu no momento errado, ele leva as cartas da mesa
                        else:
                            baralho_j2.extend(baralho_mesa)
                            baralho_mesa.clear()
            # Se o jogador deseja encerrar o jogo
            elif tecla.char == 'q':
                fim_jogo.set()
                return False
        # Sinaliza para a thread de atualização de tela que o jogador 2 terminou a rodada
        jogador_pronto.set()

    # Adquire e inicia um 'listener' do teclado
    teclado_j2 = keyboard.Listener(on_press=on_press)
    teclado_j2.start()
    # Aguarda até que o jogo termine
    fim_jogo.wait()
    # Sinaliza a atualização da tela para a respectiva thread
    jogador_pronto.set()
    # Finaliza o 'listener' do teclado
    teclado_j2.stop()

