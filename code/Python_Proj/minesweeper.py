import copy
import time
from random import randint
from math import sqrt
from colorama import Fore, Style
import sys




def jogo():
    tamanho, linhas, colunas, minas, board, game, lost = 1, 0, 0, 0, [], True, False

    input(" " + Style.BRIGHT + Fore.BLUE + "M" + Fore.GREEN + "i" + Fore.RED + Fore.MAGENTA + "n"
          + Fore.CYAN + "e" + Fore.YELLOW + "s" + Fore.LIGHTBLUE_EX + "w" + Fore.LIGHTGREEN_EX + "e"
          + Fore.LIGHTRED_EX + "e" + Fore.LIGHTMAGENTA_EX + "p" + Fore.LIGHTYELLOW_EX + "e"
          + Fore.LIGHTWHITE_EX + "r" + Fore.BLACK + " (R)" + Fore.GREEN +
          " - Press any key to start!" + "\n")
    print(Style.RESET_ALL)
    start = True
    while start:
        val = input(" " + Style.BRIGHT + Fore.LIGHTWHITE_EX + "Para as comecar (S), para ajuda (H),"
                    "para sair (Q)" + "\n")
        if val.upper() == "S":
            start = False
        elif val.upper() == "H":
            print("Regras: \n O minesweeper consiste em limpar um campo minado \n"
                  " como tal, cada quadrado tem um inteiro \n com o numero de minas na proximidade."
                  "\n Cabe a si encontrar as minas com logica. \n"
                  " Uma consola aparecerera: escreva as coordenadas (linhas + colunas) \n"
                  " seguido de F para flag (marcar bomba), R(remover flag) ou C (clear). \n"
                  " Se limpar todas as bobmas ganha!!! \n")
        elif val.upper() == "Q":
            option = input(Fore.RED + "TEM A CERTEZA QUE QUER SAIR? Confime com 'Y'.\n")
            if option.upper() == "Y":
                print("A TERMINAR PROGRAMA.")
                time.sleep(2)
                sys.exit()

        else:
            print(Fore.RED + "Opcao invalida, repita por favor!")

    while tamanho:
        dificuldade = input(Style.BRIGHT + Fore.BLUE + "Qual a dificuldade? Facil (F) , medio (M) "
                                                       "ou Dificil(D)" + "\n")
        if dificuldade.upper() == "F":  # 10 minas 8x8
            linhas, colunas, tamanho, minas = 8, 8, 0, 10
            board = [[], [], [], [], [], [], [], []]

        elif dificuldade.upper() == "M":  # 40 minas 15x15
            linhas, colunas, tamanho, minas = 15, 15, 0, 40
            board = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

        elif dificuldade.upper() == "D":  # 99 minas 16x30
            linhas, colunas, tamanho, minas = 16, 30, 0, 99
            board = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        else:
            print(Fore.RED + "Dificuldade invalida, repita por favor!")
    print(Style.RESET_ALL)

    # playsound(r'C:\Users\nobre\PycharmProjects\Fundamentos\projetos_pessoais\Jogosr\ bomb.mp3')

    # inicialzacao dos 0 na grid
    for p in board:
        for k in range(colunas):
            p.append(0)

    show_board = copy.deepcopy(board)

    for p in show_board:
        p.clear()
        for k in range(colunas):
            p.append("*")

    numer_board = copy.deepcopy(board)
    coords = []
    coords_board = []

    def coord_generator():  # gera grid com todas as posições do tabuleiro
        cnt, cnt2 = -1, -1
        for argumento in board:
            cnt2 = -1
            cnt += 1
            for coisa in argumento:
                cnt2 += 1
                coords_board.append((cnt, cnt2))

    coord_generator()

    def mine_placer():
        mines_board = 0

        while mines_board < minas:
            cordx = randint(0, linhas - 1)  # escolher linha
            cordy = randint(0, colunas - 1)  # escolher coluna

            if board[cordx][cordy] == 0:
                board[cordx][cordy] = 9
                coords.append((cordx, cordy))
                mines_board += 1

    def bomb_checker():  # Dá valores de proximidade de bombas
        near_bombs, tracker_l, tracker_c = 0, -1, -1
        for i in board:
            tracker_l += 1
            tracker_c = -1
            for j in i:
                tracker_c += 1
                if (tracker_l, tracker_c) in coords:
                    numer_board[tracker_l][tracker_c] = 9
                else:
                    for coordenadas in coords:
                        if sqrt((coordenadas[0]-tracker_l)**2 + (coordenadas[1]-tracker_c)**2) < 1.5:

                            near_bombs += 1

                    numer_board[tracker_l][tracker_c] = near_bombs
                near_bombs = 0

    def colour_aux(arg):  # Escolher cores de texto
        if arg == 0:
            return '\033[37m' + str(arg)
        elif arg == 1:
            return '\033[34m' + str(arg)
        elif arg == 2:
            return '\033[32m' + str(arg)
        elif arg == 3:
            return '\033[31m' + str(arg)
        elif arg == 4:
            return '\033[35m' + str(arg)
        elif arg == 5:
            return '\033[33m' + str(arg)
        elif arg == 6:
            return '\033[36m' + str(arg)
        elif arg == 7:
            return '\033[37m' + str(arg)
        elif arg == 8:
            return '\033[31m' + str(arg)
        elif arg == 9:
            return str(arg)
        elif arg == "?":
            return Fore.LIGHTYELLOW_EX + str(arg)
        else:
            return '\033[37m' + str(arg)

    def printer(arg):
        visual, line, line2, cnt = " ", "   ", "", 1

        for j in range(1, colunas+1):
            if j < 9:
                line += str(j) + "  "
            else:
                line += str(j) + " "
        line += "\n  "
        for pos in range((colunas-2)*2):
            line += "_ "
        visual += line + "\n"

        for i in arg:
            if cnt < 10:
                line2 = str(cnt) + " | "
            else:
                line2 = str(cnt) + "| "
            for j in i:
                # Para tirar brightness remover Style.BRIGHT
                line2 += Style.BRIGHT + str(colour_aux(j)) + "  " + '\033[39m'
            line2 += "\n"
            visual += line2
            cnt += 1

        print(visual)

    def clearer_aux(posl, posc):
        for elemento in coords_board:
            if elemento[0] == posl and elemento[1] == posc:
                show_board[elemento[0]][elemento[1]] = 0
                continue
            else:
                if sqrt((elemento[0]-posl)**2 + (elemento[1]-posc)**2) < 1.5:
                    if numer_board[elemento[0]][elemento[1]] == 0 and show_board[elemento[0]][elemento[1]] == "*":
                        show_board[elemento[0]][elemento[1]] = 0
                        # Vê recursivamente todas as células visinhas
                        clearer_aux(elemento[0], elemento[1])

                    elif show_board[elemento[0]][elemento[1]] == "*":
                        show_board[elemento[0]][elemento[1]] = numer_board[elemento[0]][elemento[1]]
                    else:
                        continue

    def selector():  # Escolhe a casa inicial do jogo
        finish = True
        while finish:
            cordx = randint(0, linhas - 1)  # escolher linha
            cordy = randint(0, colunas - 1)  # escolher coluna
            if numer_board[cordx][cordy] == 0:
                clearer_aux(cordx, cordy)
                printer(show_board)
                finish = False

    def choice(posl, posc, obj):
        if isinstance(show_board[posl][posc], int):
            return 1
        elif obj.upper() == "F" and show_board[posl][posc] == "?":
            return 1
        elif obj.upper() == "R" and show_board[posl][posc] != "?":
            return 1
        elif obj.upper() == "C" and show_board[posl][posc] == "?":
            return 1
        else:
            return 0

    def ender(posl, posc, obj):
        if obj == "C":
            if numer_board[posl][posc] == 9:
                return 1
            elif numer_board[posl][posc] == 0:
                clearer_aux(posl, posc)
            else:
                show_board[posl][posc] = numer_board[posl][posc]

        elif obj == "F":
            show_board[posl][posc] = "?"
        else:
            show_board[posl][posc] = "*"
        return 0

    def end_game():
        loop = 1
        if lost:
            while loop:
                resposta = input(Fore.BLUE + "Que pena, quer jogar outra vez (Y) ou encerrar o jogo"
                                             " (Q)? \n" + Fore.RESET)
                if resposta.upper() == "Y":
                    loop = 0
                elif resposta.upper() == "Q":
                    options = input(Fore.RED + " TEM A CERTEZA QUE QUER SAIR? Confime com 'Y'.\n" + Fore.RESET)
                    if options.upper() == "Y":
                        print(Fore.RED + " A TERMINAR PROGRAMA.")
                        time.sleep(2)
                        sys.exit()
        else:
            print(Fore.YELLOW + "WOW you are really good!!! \n" + Fore.RESET)
            while loop:
                resposta = input(Fore.BLUE + "Quer jogar outra vez (Y) ou encerrar o jogo "
                                             "(Q)? \n" + Fore.RESET)
                if resposta.upper() == "Y":
                    loop = 0
                elif resposta.upper() == "Q":
                    options = input(
                        Fore.RED + " TEM A CERTEZA QUE QUER SAIR? Confime com 'Y'.\n" + Fore.RESET)
                    if options.upper() == "Y":
                        print(Fore.RED + " A TERMINAR PROGRAMA.")
                        time.sleep(2)
                        sys.exit()
        print(Fore.MAGENTA + "Here we go again!!! \n" + Fore.RESET)
        jogo()

    ########################################### GAME DYNAMICS

    printer(show_board)
    print(Fore.YELLOW + Style.BRIGHT + " A escolher casa inicial!" + Fore.GREEN)
    contador = 0
    while contador < 9:
        print(" *", end="")
        contador += 1
        time.sleep(0.5)
    print("\n" + Fore.BLUE + " DONE!" + Fore.RESET)

    mine_placer()
    bomb_checker()
    selector()

    mines_left = minas
    real_mines_left = minas

    while game:

        message = True
        x, y, z = 0, 0, ""

        while message:
            cordl = str(input(Fore.GREEN + " Escreva a coordenada da linha!"))

            cordc = str(input(Fore.GREEN + " Escreva a coordenada da coluna!"))

            ordem = str(input(Fore.GREEN + " Escreva F(flag), R(remove) ou C(clear) ou "
                                           "W(wipe choices)"
                                           "Q para sair!"))
            print(Fore.RESET)

            if ordem.upper() == "Q":
                option = input(Fore.RED + " TEM A CERTEZA QUE QUER SAIR? Confime com 'Y'.\n")
                if option.upper() == "Y":
                    print(" A TERMINAR PROGRAMA.")
                    time.sleep(2)
                    sys.exit()
            elif ordem.upper() == "W":
                print(Fore.YELLOW + " A resetar escolhas!\n" + Fore.RESET)
            elif not cordl.isnumeric() or not cordc.isnumeric() \
                    or not ordem.isalpha() or int(cordl) <= 0 or int(cordl) > linhas or \
                     int(cordc) <= 0 or int(cordc) > colunas or not (ordem.upper() == "F" or
                                        ordem.upper() == "R" or ordem.upper() == "C"):
                print(Fore.RED + " Opcao invalida, repita por favor!\n" + Fore.RESET)

            elif choice(int(cordl)-1, int(cordc)-1, ordem):
                print(Fore.RED + " Opcao invalida, repita por favor!\n" + Fore.RESET)
            else:
                x, y, z = int(cordl)-1, int(cordc)-1, str(ordem.upper())
                message = False
        if z.upper() == "F":
            if board[x][y] == 0:
                real_mines_left -= 1
            else:
                mines_left -= 1
        elif z.upper() == "R":
            if board[x][y] == 0:
                real_mines_left += 1
            else:
                mines_left += 1

        if ender(x, y, z):
            contador = 0
            print(Fore.RED + " BOOOOOOOOOOOOOOOOOOM!!!! \n YOU LOST! \n" + Fore.RESET)
            while contador < 9:
                print(Fore.GREEN + " *", end="")
                contador += 1
                time.sleep(0.5)
            print(Fore.YELLOW + " \n Aqui estao as bombas (os 9). \n" + Fore.RESET)
            printer(numer_board)
            lost = True
            game = False

        elif real_mines_left == 0:
            game = False
        else:
            print(Fore.YELLOW + "   Faltam " + str(mines_left) + " Flags" + Fore.RESET)
            printer(show_board)

    # ENDGAME
    end_game()


jogo()
