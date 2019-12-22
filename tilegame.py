import random
import copy
import tkinter.messagebox
from tkinter import *
import sys
player1 = []
player2 = []
board = [[0 for i in range(13)]for j in range(13)]

def make_tile():
    color = {"red","orange", "blue", "black"}
    number = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
    global tile
    tile = []
    for i in color:
        for j in number:
            ap = {'color':i, 'number':j}
            tile.append(ap)
    for i in color:
        for j in number:
            ap = {'color':i, 'number':j}
            tile.append(ap)
    random.shuffle(tile)
    return tile

def dist_tile(tile):
    for i in range(13):
        a = random.choice(tile)
        player1.append(a)
        tile.remove(a)
        b = random.choice(tile)
        player2.append(b)
        tile.remove(b)

def show_tile(who):
    if who == player1:
        print("player1 tile is")
        for tile in who:
            print(str(tile['color']) + ' '+ str(tile['number']), end = ' ')
        print()
    elif who == player2:
        print("player2 tile is")
        for tile in who:
            print(str(tile['color']) + ' '+ str(tile['number']), end = ' ')
        print()

def more(message):
    answer = input(message)
    while not (answer == 'y' or answer == 'n'):
        answer = input(message)
    if answer =='y':
        return True
    else:
        return False

def register(who,tile, board) :
    cptile = copy.deepcopy(who)
    cpboard = copy.deepcopy(board)
    if more("Do you want to register?(y/n) ") == True:
        global answer1
        answer1 = input("몇개의 묶음을 등록하시겠습니까? ")
        while answer1.isdigit() == False:
            answer1 = input("몇개의 묶음을 등록하시겠습니까? ")
        answer1 = int(answer1)
        row: int = len(board)
        col = len(board[0])
        realcard(who,cptile)
        a = []
        global jud_row
        jud_row = 0
        for i in range(row):
            original = []
            judge = []
            for j in range(col):
                if board[i][j] != 0:
                    a.append(board[i][j])
            if board[i] != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0]:
                jud_row += 1
        global jud
        for i in range(jud_row):
            jud_board = []
            col = 0
            for j in range(13):
                if (board[i][j] != 0):
                    col += 1
                    jud_board.append(board[jud_row-1][j])
            for j in range(col-1):
                if jud_board[j]['number'] == jud_board[j+1]['number']:
                    if jud_board[j]['color'] != jud_board[j+1]['color']:
                        jud = 0
                    else:
                        jud = 1
                        break
                elif jud_board[j]['number'] == jud_board[j+1]['number']-1:
                    if jud_board[j]['color'] == jud_board[j+1]['color']:
                        jud = 0
                    else:
                        jud = 1
                        break
                else:
                    jud = 1
                    break
        sum = 0
        for i in range(len(a)):
            sum += a[i]['number']
        if sum < 30 and jud == 1:
            print("Sum is not over 30 and you entered unaligned tiles.")
            print("You get 1 tile.")
            for i in range(len(board)):
                board[i] = cpboard[i]
            who = cptile
            emptytile(who)
            print('\n')
        elif sum < 30:
            print("Sum is not over 30")
            print("You get 1 tile.")
            for i in range(len(board)):
                board[i] = cpboard[i]
            who = cptile
            emptytile(who)
            print('\n')
        elif jud == 1:
            print("You entered an unaligned tiles.")
            print("You get 1 tile.")
            for i in range(len(board)):
                board[i] = cpboard[i]
            who = cptile
            emptytile(who)
            print('\n')
        elif sum >= 30 and jud == 0:
            print("You success to register.")
        else:
            print("You get 1 tile.")
            for i in range(len(board)):
                board[i] = cpboard[i]
            who = cptile
            emptytile(who)
            print('\n')
    else:
        print("You get 1 tile.")
        who = cptile
        emptytile(who)
        print('\n')


def realcard(who,cptile):
    for row in range(answer1):
        global answer2
        answer2 = input("How many tiles do you want to enter? ")
        while answer2.isdigit() == False:
            answer2 = input("How many tiles do you want to enter? ")
        answer2 = int(answer2)
        if answer2 >= 3:
            enter_tile(row,who,cptile)
        else:
            print("You should register more than 3 tiles.")
            print("Please re-enter.")
            realcard(who,cptile)

def enter_tile(row,who,cptile):
    print("Please enter tiles!")
    row = 0
    for i in range(13):
        global board
        if board[i] != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
            row += 1
    for j in range(answer2):
        try:
            a, b = input().split()
            b = int(b)
            c = {'color':a, 'number':b}
            if c in who:
                board[row][j] = c
                who.remove(c)
                global judge
                judge = True
            else:
                print("This tile is not yours")
                print("Please re-enter the tile.")
                who = cptile
                enter_tile(i,who,cptile)
        except:
            print("Tile input is not formatted.")
            print("Please re-enter the tile.")
            who = cptile
            enter_tile(i,who,cptile)

def emptytile(who):
    if tile != []:
        a = random.choice(tile)
        who.append(a)
        tile.remove(a)
        show_tile(who)
    else:
        print("There are no tile.")

def arrange_tile(who):
    answer = input("타일 등록조건을 보시겠습니까?(y/n) ")
    if answer == 'y':
        Msgbox()
    else:
        pass
    while 1:
        answer = input("Do you want sort? (789/777/NO) ")
        while not (answer == '789' or answer == '777' or answer == 'NO'):
            answer = input("Do you want sort? (789/777/NO) ")
        if answer == '777':
            who.sort(key=lambda x: x['number'])
            show_tile(who)
            if more("Do you want sort again?(y/n) ") == False:
                return 0
        elif answer == '789':
            who.sort(key=lambda x: (x['color'],x['number']))
            show_tile(who)
            if more("Do you want sort again?(y/n) ") == False:
                return 0
        else:
            return 0

def show_regboard():
    row = 0
    for i in range(13):
        if board[i] != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
            row += 1
    for i in range(row):
        print(i+1,'th:')
        for j in range(13):
            if board[i][j] != 0:
                print(str(board[i][j]['color'])+' '+str(board[i][j]['number']), end = ' ')
        print("\n")

def regist_newtile(who,board):
    ans = input("몇개의 묶음을 등록하시겠습니까?")
    while ans.isdigit() == False:
        ans = input("몇개의 묶음을 등록하시겠습니까?")
    ans = int(ans)
    cpboard = copy.deepcopy(board)
    cptile = copy.deepcopy(who)
    bdrow = 0
    jud_col = 0
    for i in range(13):
        if board[i] != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0]:
            bdrow += 1
    for i in range(ans):
        realcard(who,cptile)
    for i in range(ans):
        jud_col1 = []
        col = 0
        for j in range(13):
            if board[bdrow][j] != 0:
                col += 1
                jud_col1.append(board[bdrow][j])
        for j in range(col-1):
            if jud_col1[j]['number'] == jud_col1[j+1]['number']:
                if jud_col1[j]['color'] != jud_col1[j+1]['color']:
                    jud_col = 0
                else:
                    jud_col = 1
                    break
            elif jud_col1[j]['number'] == jud_col1[j+1]['number']-1:
                if jud_col1[j]['color'] == jud_col1[j+1]['color']:
                    jud_col = 0
                else:
                    jud_col = 1
                    break
            else:
                jud_col = 1
                break
        bdrow += 1
    if jud_col == 1:
        print("You enter unaligned tile.")
        print("Please re-enter the tile.")
        for i in range(len(board)):
            board[i] = cpboard[i]
        regist_newtile(who,board)
    else:
        print("You are success to register tiles!")
        print('\n')

def regist_atile(who):
    ans = input("Where do you want to register?")
    while ans.isdigit() == False:
        ans = input("Where do you want to register?")
    ans = int(ans)
    col = 0
    cpcol = copy.deepcopy(board[ans-1])
    for i in range(13):
        if board[ans-1][i] != 0:
            col += 1
    ans1 = input("Where do you want to register a tile?(front/back) ")
    if ans1 == 'front':
        th = 0
    else:
        th = col
    print("Please enter a tile!")
    a, b = input().split()
    b = int(b)
    c = {'color':a, 'number':b}
    col = 0
    jud_col1 = []
    jud_col = 0
    if c in who:
        board[ans-1].insert(th,c)
        for i in range(13):
            if board[ans-1][i] != 0:
                jud_col1.append(board[ans-1][i])
        for i in range(col):
            if jud_col1[i]['number'] == jud_col1[i+1]['number']:
                if jud_col1[i]['color'] != jud_col1[i+1]['color']:
                    jud_col = 0
                else:
                    jud_col = 1
                    break
            elif jud_col1[i]['number'] == jud_col1[i+1]['number']-1:
                if jud_col1[i]['color'] == jud_col1[i+1]['color']:
                    jud_col = 0
                else:
                    jud_col = 1
                    break
            else:
                jud_col = 1
                break
    else:
        print("This tile is not yours.")
        print("Please re-enter the tile.")

    if jud_col == 1:
        print("You sould enter aligned tile.")
        print("Please re-enter a tile.")
        board[ans-1] = cpcol
        regist_atile(who)

    else:
        print("You success to register a tile!")

def turn_dice():
    global turn
    turn = True
    roll = input("Press the enter to throw the dice.")
    if roll == '':
        dice1 = random.randrange(1, 7)
        dice2 = random.randrange(1, 7)
        print("player1's dice is", dice1)
        print("player2's dice is", dice2)
        if dice1 > dice2:
            turn = True
            print("player1 plays first!")
        elif dice1 < dice2:
            turn = False
            print("player2 plays first!")
        else:
            print("re_roll a dice!")
            turn_dice()

def start():
    start = input("Press Enter to start the game.")
    if start == '':
        tilegame()
    else:
        start()

def stockExit(self):
    sys.exit(0)

def Msgbox():
    tkinter.messagebox.showinfo("<카드 등록할 수 있는 조건>", "1. 등록하려는 카드들의 숫자가 같을 경우 그 카드들의 색깔은 서로 달라야한다.\n2. 등록하려는 카드들의 색깔이 같을 경우 그 카드들의 숫자는 서로 달라야한다.\n3. 등록하려는 카드의 개수는 3개 이상이여야 한다.\n4. 등록하려는 카드의 숫자들의 합은 30이 넘어야한다.")

def end():
    a = input("Do you want to play again?(y/n) ")
    if a == 'y':
        start()
    elif a == 'n':
        stockExit()
    else:
        end()

def player1_turn(player1_success, player2_success):
    enter = input("\nIt's player1's turn.(Press Enter!)")
    if enter == '':
        if turn == True:
            if player1_success == 0:
                show_tile(player1)
                arrange_tile(player1)
                register(player1, tile, board)
                if player2_success != 1:
                    if board[0][0] != 0:
                        player1_success += 1
                else:
                    if board[1][0] != 0:
                        player1_success += 1
            else:
                nextstage1()
        else:
            if player1_success == 0:
                show_tile(player1)
                arrange_tile(player1)
                register(player1, tile, board)
                if player2_success == 1:
                    if board[1][0] != 0:
                        player1_success += 1
                else:
                    if board[0][0] != 0:
                        player1_success += 1
            else:
                nextstage1()
    return player1_success

def player2_turn(player1_success, player2_success):
    enter = input("\nIt's player2's turn.(Press Enter!)")
    if enter == '':
        if turn == False:
            if player2_success == 0:
                show_tile(player2)
                arrange_tile(player2)
                register(player2, tile, board)
                if player1_success == 0:
                    if board[0][0] != 0:
                        player2_success += 1
                else:
                    if board[0][0] != 0:
                        player2_success += 1
            else:
                nextstage2()
        else:
            if player2_success == 0:
                show_tile(player2)
                arrange_tile(player2)
                register(player2, tile, board)
                if player1_success == 1:
                    if board[1][0] != 0:
                        player2_success += 1
                else:
                    if board[0][0] != 0:
                        player2_success += 1
            else:
                nextstage2()
    return player2_success

def nextstage1():
    print("\nIt's player1's turn.")
    print("Put down your card.")
    print("Menu : show_board(1), register_newtile(2), register_a_tile(3),pick_atile(4), show_tile(5)")
    a = input("Select menu: ")
    while a.isdigit() == False:
        a = input("Select menu: ")
    a = int(a)
    if a == 1:
        show_regboard()
    elif a == 2:
        regist_newtile(player1,board)
    elif a == 3:
        regist_atile(player1)
    elif a == 4:
        emptytile(player1)
    elif a == 5:
        show_tile(player1)

def nextstage2():
    print("\nIt's player2's turn.")
    print("Put down your card.")
    print("Menu : show_board(1), register_newtile(2), register_a_tile(3),pick_atile(4), show_tile(5)")
    a = input("Select menu: ")
    while a.isdigit() == False:
        ans = input("Select menu: ")
    a = int(a)
    if a == 1:
        show_regboard()
    elif a == 2:
        regist_newtile(player2, board)
    elif a == 3:
        regist_atile(player2)
    elif a == 4:
        emptytile(player2)
    elif a == 5:
        show_tile(player2)

def jud_end():
    if player1 == []:
        return 1
    elif player2 == []:
        return 2
    else:
        return 0

def tilegame():
    tile = make_tile()
    dist_tile(tile)
    print("Decide who's going first.")
    turn_dice()
    player1_success = 0
    player2_success = 0
    for i in range(5):
        if turn == False:
            player2_success = player2_turn(player1_success, player2_success)
            player1_success = player1_turn(player1_success, player2_success)
            if jud_end() != 0:
                break
        else:
            player1_success = player1_turn(player1_success, player2_success)
            player2_success = player2_turn(player1_success, player2_success)
            if jud_end() != 0:
                break
    if jud_end() == 1 or len(player1) < len(player2):
        print("Player1 is winner!")
    elif jud_end() == 2 or len(player2) < len(player1):
        print("Player2 is winner!")
    else:
        print("Draw!")
    end()


start()

	

