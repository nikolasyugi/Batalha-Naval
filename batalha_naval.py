def print_board(board):
    #impressão dos índices das colunas:
    print("           ",end='')
    for coluna in range(len(board)):
        if coluna!=0:
            print(" |  %4d   " %(coluna), end='')
    print(" |  %4d    |" %(coluna+1))
    print(" ",end='')
    for coluna in range(len(board)+1):
        print("+---------", end='-')
    print("+")
    #impressão das linhas:
    for linha in range(len(board[0])+1):
        if linha!=0:
            print(" |  %4d   " %(linha), end='')
            for j in range(len(board)-1):
                print(" |  %4s   " %(board[linha-1][j]), end='')
            j=len(board[0])-1
            print(" |  %4s    |" %(board[linha-1][j]))
            print(" ",end='')
            for j in range(len(board)+1):
                print("+---------", end='-')
            print("+")

#---------------------------------------------------------------------------------#

def colocar_ship(tipo,tamanho,ships_board):
    from random import randint
    ok=True
    flag=True
    possivel=True
    while flag:
        ship_x=randint(0,9)
        ship_y=randint(0,9)
        ship_x_a=ship_x
        ship_y_a=ship_y
        if ships_board[ship_x][ship_y]=="O":
            flag=False
    ships_board[ship_x][ship_y]=tipo
    primeiro_x=ship_x
    primeiro_y=ship_y
    if tamanho>1:
        while ok:
            if ship_x!=0 and ship_x!=9 and ship_y!=0 and ship_y!=9:
                number=randint(1,4)
                if number==1:
                    ship_x+=1
                elif number==2:
                    ship_x-=1
                elif number==3:
                    ship_y+=1
                elif number==4:
                    ship_y-=1
            elif ship_x==0:
                if ship_y==0:
                    number=randint(1,2)
                    if number==1:
                        ship_x+=1
                    elif number==2:
                        ship_y+=1
                elif ship_y==9:
                    number=randint(1,2)
                    if number==1:
                        ship_x+=1
                    elif number==3:
                        ship_y-=1
                else:
                    number=randint(1,3)
                    if number==1:
                        ship_x+=1
                    elif number==2:
                        ship_y+=1
                    elif number==3:
                        ship_y-=1
            elif ship_x==9:
                if ship_y==0:
                    number=randint(1,2)
                    if number==1:
                        ship_x-=1
                    elif number==2:
                        ship_y+=1
                elif ship_y==9:
                    number=randint(1,2)
                    if number==1:
                        ship_x-=1
                    elif number==3:
                        ship_y-=1
                else:
                    number=randint(1,3)
                    if number==1:
                        ship_x-=1
                    elif number==2:
                        ship_y+=1
                    elif number==3:
                        ship_y-=1
            elif ship_y==0:
                number=randint(1,3)
                if number==1:
                    ship_x-=1
                elif number==2:
                    ship_y+=1
                elif number==3:
                    ship_x-=1
            else:
                number=randint(1,3)
                if number==1:
                    ship_x-=1
                elif number==2:
                    ship_x+=1
                elif number==3:
                    ship_y-=1
            if ships_board[ship_x][ship_y]=="O":
                ok=False
            if ok:
                ship_x=primeiro_x
                ship_y=primeiro_y
        ships_board[ship_x][ship_y]=tipo
        segundo_x=ship_x
        segundo_y=ship_y
        passo=2 #quanto somar na coordenada
        vertical=False
        horizontal=False
        while tamanho>2:
            if ship_x!=ship_x_a:
                if ship_x==0:
                    ship_x+=passo
                    ship_x_a=ship_x-1
                elif ship_x==9:
                    ship_x-=passo
                    ship_x_a=ship_x+1
                else:
                    if ship_x-ship_x_a==1:
                        ship_x+=1
                        ship_x_a=ship_x-1
                    elif ship_x-ship_x_a==-1:
                        ship_x-=1
                        ship_x_a=ship_x+1
            else:
                if ship_y==0:
                    ship_y+=passo
                    ship_y_a=ship_y-1
                elif ship_y==9:
                    ship_y-=passo
                    ship_y_a=ship_y+1
                else:
                    if ship_y-ship_y_a==1:
                        ship_y+=1
                        ship_y_a=ship_y-1
                    elif ship_y-ship_y_a==-1:
                        ship_y-=1
                        ship_y_a=ship_y+1
            tamanho-=1
            passo+=1
            ships_board[ship_x][ship_y]=tipo

#--------------------------------------------------#

board=[]
for i in range (0,10):
    board.append(["O"]*10)
    
ships_board=[]
for i in range (0,10):
    ships_board.append(["O"]*10)

#Montar o tabuleiro:

#Aircraft Carrier(x1)
colocar_ship("PA",5,ships_board)

#Battleship(x1)
colocar_ship("CO",4,ships_board)

#Cruiser(x1)
colocar_ship("CR",3,ships_board)

#Patrol Boat(x2)
colocar_ship("TD",2,ships_board)
colocar_ship("TD",2,ships_board)

#Submarine(x2)
colocar_ship("SM",1,ships_board)
colocar_ship("SM",1,ships_board)

#jogo

print("BATALHA NAVAL!")
print("O jogo é composto por 6 barcos:")
print("-1 Porta-aviões (5 casas)")
print("-1 Couraçado (4 casas)")
print("-1 Cruzeiro (3 casas)")
print("-2 Torpedeiro (2 casas)")
print("-2 Submarinos (1 casa)")
jogo_nao_acabou=True
print_board(board)
escolha_jogador=input("Escolha uma casa (Ex: linha,coluna) ")
while jogo_nao_acabou:
    jogada=escolha_jogador.split(",")
    jogada[0]=int(jogada[0])
    jogada[1]=int(jogada[1])
    if ships_board[jogada[0]-1][jogada[1]-1]=="O":
        print("ÁGUAA!")
        board[jogada[0]-1][jogada[1]-1]="X"
    elif ships_board[jogada[0]-1][jogada[1]-1]=="PA":
        if pa<5:
            print("Parabéns, você acertou o Porta-aviões!")
        elif pa==5:
            print("Você destruiu o Porta-aviões!")
        board[jogada[0]-1][jogada[1]-1]="PA"
    elif ships_board[jogada[0]-1][jogada[1]-1]=="CO":
        if co<4:
            print("Parabéns, você acertou o Couraçado!")
        elif co==4:
            print("Você destruiu o Couraçado!")
        board[jogada[0]-1][jogada[1]-1]="CO"
    elif ships_board[jogada[0]-1][jogada[1]-1]=="CR":
        if cr<3:
            print("Parabéns, você acertou o Cruzeiro!")
        elif cr==3:
            print("Você destruiu o Cruzeiro!")
        board[jogada[0]-1][jogada[1]-1]="CR"
    elif ships_board[jogada[0]-1][jogada[1]-1]=="TD":
        print("Parabéns, você acertou o Torpedeiro!")
        board[jogada[0]-1][jogada[1]-1]="TD"
    elif ships_board[jogada[0]-1][jogada[1]-1]=="SM":
        print("Você destruiu um Submarino!")
        board[jogada[0]-1][jogada[1]-1]="SM"
    print_board(board)
    pa=0
    co=0
    cr=0
    td=0
    sm=0
    for row in board:
        for i in row:
            if i=="PA":
                pa+=1
            elif i=="CO":
                co+=1
            elif i=="CR":
                cr+=1
            elif i=="TD":
                td+=1
            elif i=="SM":
                sm+=1
    if pa==5 and co==4 and cr==3 and td==4 and sm==2:
        jogo_nao_acabou=False
    if jogo_nao_acabou==False:
        print("Parabéns, você venceu!!")
    else:
        print("Para desistir e ver onde estavam os barcos digite (d)")
        print("Para saber quais os barcos do jogo, digite (s)")
        saber_o_que_falta=input("Para continuar APERTE ENTER ")
        if saber_o_que_falta=="s":
            print("1 Porta-aviões (5 casas), 1 Couraçado (4 casas), 1 Cruzeiro (3 casas), 2 Torpedeiros (2 casas), 2 Submarinos (1 casa)")
        elif saber_o_que_falta=="d":
            print("Ok, até a próxima!")
            print_board(ships_board)
            jogo_nao_acabou=False
        if jogo_nao_acabou:
            escolha_jogador=input("Escolha outra casa: ")
