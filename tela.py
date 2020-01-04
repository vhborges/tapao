# standard modules
import os

# project modules
import tapao

# apaga a tela executando um comando a depender do sistema operacional utilizado
def apaga():
    # caso o sistema operacional seja Windows
    if os.name == 'nt':
        os.system('cls')
    # caso contrário (Unix)
    else:
        os.system('clear')

#imprime os montes quando o centro está vazio
def imprime_montes_inicio():
    print('      .------.      .------.      .------.\n'
          '      | XXXX |      |      |      | XXXX |\n'
          '      | XXXX |      |      |      | XXXX |\n'
          '      | XXXX |      |      |      | XXXX |\n'
          '      | XXXX |      |      |      | XXXX |\n'
          '      \'------\'      \'------\'      \'------\'')

#imprime os montes durante o jogo
def imprime_montes( carta, monte_j1, monte_j2 ):

    #resgata naipe e valor da carta
    naipe, valor = carta

    #desenho dos montes, inicia como vazio
    monte = [ '    ', '    ' ]
    arte_naipe = []

    #verifica os montes dos jogadores para ver se tem cartas ou estão vazios
    #true = tem carta
    #false = vazio
    if monte_j1 > 0:
        monte[0] = 'XXXX'

    if monte_j2 > 0:
        monte[1] = 'XXXX'

    #verifica o naipe da carta do monte central e atribui arte a ela
    if naipe == 'C':
        arte_naipe = [ '(\\/)', ':\\/:' ]

    elif naipe == 'E':
        arte_naipe = [ ':/\\:', '(__)' ]

    elif naipe == 'O':
        arte_naipe = [ ':/\\:', ':\\/:' ]

    elif naipe == 'P':
        arte_naipe = [ ':():', '()()' ]

    #imprime os montes de acordo com a carta passada

    #se for 10 o desenho é diferente
    if valor == '10':
        print ('      .------.      .------.      .------.\n'
              f'      | {monte[0]} |      |{valor}..  |      | {monte[1]} |\n'
              f'      | {monte[0]} |      | {arte_naipe[0]} |      | {monte[1]} |\n'
              f'      | {monte[0]} |      | {arte_naipe[1]} |      | {monte[1]} |\n'
              f'      | {monte[0]} |      |  \'\'{valor}|      | {monte[1]} |\n'
               '      \'------\'      \'------\'      \'------\'')

    else:
        print ('      .------.      .------.      .------.\n'
              f'      | {monte[0]} |      |{valor}.--. |      | {monte[1]} |\n'
              f'      | {monte[0]} |      | {arte_naipe[0]} |      | {monte[1]} |\n'
              f'      | {monte[0]} |      | {arte_naipe[1]} |      | {monte[1]} |\n'
              f'      | {monte[0]} |      | \'--\'{valor}|      | {monte[1]} |\n'
               '      \'------\'      \'------\'      \'------\'')

#imprime a tela do jogo
def imprime ( baralho_j1, baralho_mesa, baralho_j2, carta_atual, rodada_atual):
    print (f'\n      Jogador 1    Bater em: {carta_atual:2s}   Jogador 2')

    #se o centro estiver vazio
    if len(baralho_mesa) == 0:
        imprime_montes_inicio()

    else:
        imprime_montes(baralho_mesa[-1], len(baralho_j1), len(baralho_j2))

    seta = '<' if rodada_atual == 1 else '>'

    print (f'      {len(baralho_j1):02} cartas     {len(baralho_mesa):02} cartas     {len(baralho_j2):02} cartas\n\n'
            '      pressione                   pressione\n'
           f'    W para jogar       {seta}        K para jogar\n'
           f'    S para bater       {seta}        M para bater\n\n'
            '        Pressione q para encerrar o jogo\n')

# atualiza a tela do jogo, apagando e imprimindo novamente
def atualiza(baralho_j1, baralho_j2, baralho_mesa, fim_jogo, j1_pronto, j2_pronto):
    while(not fim_jogo.is_set()):
        # Bloqueia até que as threads dos jogadores estejam prontas
        j1_pronto.wait()
        j2_pronto.wait()
        # Atualiza a tela
        apaga()
        imprime(baralho_j1, baralho_mesa, baralho_j2, tapao.carta_atual, tapao.rodada_atual)
        # Reseta os events para false
        j1_pronto.clear()
        j2_pronto.clear()

