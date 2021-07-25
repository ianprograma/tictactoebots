#Tic Tac Toe game in python by techwithtim

board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    
def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

def playerMove():
    run = True
    while run:
        move = input('Por favor selecciona una posición para la \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Lo siento, este espacio está ocupado!')
            else:
                print('Por favor escribe un número sin el rango!')
        except:
            print('Por favor escribe un número!')
            

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('Bienvenido a Cero mata Cero!')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Lo siento, O\'ganó esta vez!')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Juego empatado!')
            else:
                insertLetter('O', move)
                print('COM puso un \'O\' en la posición', move , ':')
                printBoard(board)
        else:
            print('X\'ganó esta vez! Buen trabajo!')
            break

    if isBoardFull(board):
        print('Juego empatado!')

while True:
    answer = input('Quieres jugar otra vez? (Y/N) presiona ENTER para jugar con un amigo')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break

def slant_check(matrix,P1,P2):
    empty_lst1 = []
    empty_lst2= []
    lst1 = []
    lst2 = []
    x = len(matrix)
    v = len(matrix) - 1
    t = 0 
    g = 0
    n = True
    while n:
        for i in range(x):
            if matrix[i][i] == P1 or matrix[t][i] == P1:
                empty_lst1.append(matrix[i][i])
            if matrix[i][i] == P2 or matrix[t][i] == P2:
                empty_lst2.append(matrix[i][i])
        while v >= g:
            if matrix[g][v] == P1:
                lst1.append(matrix[g][v]) 
            if matrix[g][v] == P2:
                lst2.append(matrix[g][v])
            t -= 1
            v -= 1
            g += 1
        if len(empty_lst1) == x:
            return True
        if len(empty_lst2) == x:
            return True
        if len(lst1) == x:
            return True
        if len(lst2) == x:
            return True
        return False
def vertical_check(lst,P1,P2):
    for i in range(len(lst) - 2):
        for j in range(len(lst)):
            if lst[i][j] == P1 and lst[i + 1][j] == P1 and lst[i + 2][j] == P1:
                return True
            if lst[i][j] == P2 and lst[i + 1][j] == P2 and lst[i + 2][j] == P2:
                return True
            
    return False
def horizontal_check(lst,P1,P2):
    for i in range(len(lst)):
        for j in range(len(lst) - 2):
            if lst[i][j]== P1 and lst[i][j + 1]== P1 and lst[i][j + 2]== P1 :
                return True
            if lst[i][j]== P2 and lst[i][j + 1]== P2 and lst[i][j + 2]== P2 :
                return True
    return False
def find_grid2(place,lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if place == lst[i][j]:
                return lst.index(lst[i])

def find_grid1(place,lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if place == lst[i][j]:
                return lst[i].index(place)
            
def print_lst(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i]) - 2):
            print(lst[i][j],'|', lst[i][j + 1],'|', lst[i][j + 2])
            print('----------')
def tic_tac_toe():
    lst = [[1,2,3],
           [4,5,6],
           [7,8,9]]
    P1 = 0
    P2 = 0
    counter_loop = 0
    _ = 0 
    new_lst = [1,2]
    while True:
        P1 = input('Jugador 1 quiere ser "X" o "O" ? (Escribe en x o o):\n').lower()
        if P1 == 'x':
            print('Jugador 2 ahora es "O"!\n')
            P2 = 'o'
            break
        if P1 == 'o':
            print('Jugador 2 ahora es "X"!\n')
            P2 = 'x'
            break
        else:
            print('Intenta otra vez\n')
    print_lst(lst)
    while _ < len(lst): 
        for i in range(len(lst[_])):
            if counter_loop == 9:
                print("Empate!")
                break
            place_grid1 = input('Donde el jugador 1 lo quiere poner? : ')
            if int(place_grid1) >= 10 or int(place_grid1) <= 0:
                print('Intenta otra vez')
                place_grid1 = input('Dónde lo quieres poner, Jugador 1? : ')
                break
            place_grid = int(place_grid1)
            counter_loop += 1
            inner_index1 = find_grid1(place_grid,lst)
            outer_index1 = find_grid2(place_grid,lst)
            lst[outer_index1][inner_index1] = P1
            print_lst(lst)
            if horizontal_check(lst,P1,P2) == True:
                print("Jugador 1 gana!!")
                counter_loop = 9 
                break
            if vertical_check(lst,P1,P2) == True:
                print("Jugador 1 gana!!")
                counter_loop = 9 
                break
            if slant_check(lst,P1,P2) == True:
                print("Jugador 1 gana!!")
                counter_loop = 9 
                break
            if counter_loop == 9:
                print("Tie!")
                break
            place_grid2 = input('Dónde lo quieres poner, Jugador 2? : ')
            if int(place_grid2) >= 10 or int(place_grid2) <=0:
                print('Intenta de nuevo')
                place_grid2 = input('Dónde el jugador 2 quiere ponerlo? : ')
                break
            place_gridy = int(place_grid2)
            counter_loop += 1
            inner_index2 = find_grid1(place_gridy,lst)
            outer_index2 = find_grid2(place_gridy,lst)
            lst[outer_index2][inner_index2] = P2
            print_lst(lst)
            if horizontal_check(lst,P1,P2) == True:
                print("Jugador 2 gana!!")
                counter_loop = 9 
                break
            if vertical_check(lst,P1,P2) == True:
                print("Jugador 2 gana!!")
                counter_loop = 9 
                break
            if slant_check(lst,P1,P2) == True:
                print("Jugador 2 gana!!")
                counter_loop = 9 
                break
            if counter_loop == 9:
                print("Empate!")
                break        
        if counter_loop == 9:
            break
        
        _ += 1

    
tic_tac_toe()

def tic_tac_toe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def draw():
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print()

    def p1():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nNo puedes ir ahí. Intenta de nuevo")
            p1()
        else:

             board[n] = "X"
           
    def p2():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nNo puedes ponerlo ahí, intentalo otra vez")
            p2()
        else:
            board[n] = "O"

    def choose_number():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nEso no está en el tablero, intenta otra vez")
                        continue
                except ValueError:
                   print("\nEse no es un número, intenta otra vez")
                   continue

    def check_board():
        count = 0
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("Jugador 1 gana!\n")
                print("Felicidades!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("Jugador 2 gana!\n")
                print("Felicidades!\n")
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("Fue un empate\n")
                return True

    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        print("Jugador 1 selecciona un lugar para poner una X")
        p1()
        print()
        draw()
        end = check_board()
        if end == True:
            break
        print("Jugador 2 selecciona un lugar para poner un O")
        p2()
        print()

    if input("Quieres jugar otra vez? (y/n)\n") == "y":
        print()
        tic_tac_toe()

tic_tac_toe()