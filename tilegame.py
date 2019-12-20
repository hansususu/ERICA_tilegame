import random 
player1 = []
player2 = []
board = [[0 for i in range(13)]for j in range(13)]
jud_success = 0

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

def register(who,tile, jud_success, board) :
    if more("Do you want to register?(y/n) ") == True:
        global answer1
        answer1 = input("몇개의 묶음을 등록하시겠습니까?")
        while answer1.isdigit() == False:
            answer1 = input("몇개의 묶음을 등록하시겠습니까?")
        answer1 = int(answer1)
        global cptile
        cptile = who
        cpboard = board
        sum = 0
        realcard(who)     
        a = []
        global jud_row
        jud_row = 0
        for i in range(13):
            original = []
            judge = []
            for j in range(13):
                if board[i][j] != 0:
                    a.append(board[i][j])
            if board[i] != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0]:
                jud_row += 1
        global jud
        for i in range(jud_row):
            jud_board = []
            col = 0
            for j in range(13):
                if (board[jud_row-1][j] != 0):
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
        for i in range(len(a)):
            sum += a[i]['number']
        if sum < 30:
            print("Sum is not over 30")
            print("You get 1 tile.")
            who = cptile
            board = cpboard
            emptytile(who)
        elif sum < 30 and jud == 1:
            print("Sum is not over 30 and you entered unaligned tiles.")
            print("You get 1 tile.")
            board = cpboard
            who = cptile
            emptytile(who)
        elif jud == 1:
            print("You entered an unaligned tiles.")
            print("You get 1 tile.")
            board = cpboard
            who = cptile
            emptytile(who)
        elif sum >= 30 and jud == 0:
            print("You success to register.")
            jud_success += 1
    else:
        print("You get 1 tile.")
        emptytile(who)

def realcard(who):
    for row in range(answer1):
        global answer2
        answer2 = input("How many tiles do you want to enter?")
        while answer2.isdigit() == False:
            answer2 = input("How many tiles do you want to enter?")
        answer2 = int(answer2)
        if answer2 >= 3:
            enter_tile(row,who)
        else:
            print("You should register more than 3 tiles.")
            print("Please re-enter.")
            realcard(who)

def enter_tile(row,who):
    print("Please enter tiles!")
    row = 0
    for i in range(13):
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
                enter_tile(i,who)
                break
        except:
            print("Tile input is no formatted.")
            print("Please re-enter the tile.")
            who = cptile
            enter_tile(i,who)
            break

def emptytile(who):
    if tile != []:
        a = random.choice(tile)
        who.append(a)
        tile.remove(a)
        show_tile(who)
    else:
        print("There are no tile.")

def arrange_tile(who):
    while 1:
        answer = input("Do you want sort? (789/777/NO)")
        while not (answer == '789' or answer == '777' or answer == 'NO'):
            answer = input("Do you want sort? (789/777/NO)")
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
    cpboard = board
    bdrow = 0
    jud_col = 0
    for i in range(13):
        if board[i] != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0]:
            bdrow += 1
    for i in range(ans):
        realcard(who)
    for i in range(ans):
        jud_col1 = []
        col = 0
        for j in range(13):
            if board[bdrow][j] != 0:
                col += 1
                jud_col1.append(board[bdrow][j])
        for j in range(col-1):
            if jud_col1[j]['number'] == jud_col1[j+1]['number']:
                if jud_col1[j]['color'] != jud_col1[j+1]['colo']:
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
    if jud_cold == 1:
        print("You should enter unaligned tile.")
        print("Please re-enter the tile")
        board = cpboard
        regist_newtile(who,board)
    else:
        print("You are success to register tiles!")

def regist_atile(who):
    ans = input("Where do you want to register?")
    while ans.isdigit() == False:
        ans = input("Where do you want to register?")
    ans = int(ans)
    col = 0
    cpcol = board[ans-1]
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
        print("This tile tis not yours.")
        print("Please re-enter the tile.")
    if jud_col == 1:
        print("You sould enter aligned tile.")
        print("Please re-enter a tile.")
        board[ans-1] = cpcol
        regist_atile(who)
    else:
        print("You success to register a tile!")

def turn_dice():
    dice1 = random.randrange(1,7)
    dice2 = random.randrange(1,7)
    global turn
    turn = True
    print("Player1's dice is", dice1)
    print("Player2's dice is", dice2)
    if dice1 > dice2:
        turn = True
        print("Player1 plays first!")
    elif dice1 < dice2:
        turn = False
        print("Player2 plays first!")
    else:
        print("Re-roll dice!")
        turn_dice()

def jud_end():
    if player1 == []:
        print("Player1 is winner!")
        return 1
    elif player2 == []:
        print("Player2 is winner!")
        return 1
    else:
        return 0

def player1_turn():
    if turn == True:
        if jud_success == 0:
            show_tile(player1)
            arrange_tile(player1)
            register(player1, tile, jud_success, board)
        elif jud_success == 1 or jud_success == 2:
            a = input("Menu : show_board(1), register_newtile(2), register_a_tile(3),pick_atile(4), show_tile(5)")
            if a == 1:
                show_regboard()
            elif a == 2:
                regist_newtile(player1, board)
            elif a == 3:
                regist_atile(player1)
            elif a == 4:
                emptytile(player1)
            elif a == 5:
                show_tile(player1)
    else:
        if jud_success == 0 or jud_success == 1:
            show_tile(player1)
            arrange_tile(player1)
            register(player1, tile, jud_success, board)
        elif jud_success == 2:
            a = input("Menu : show_board(1), register_newtile(2), register_a_tile(3),pick_atile(4), show_tile(5)")
            if a == 1:
                show_regboard()
            elif a == 2:
                regist_newtile(player1, board)
            elif a == 3:
                regist_atile(player1)
            elif a == 4:
                emptytile(player1)
            elif a == 5:
                show_tile(player1)

def player2_turn():
    if turn == False:
        if jud_success == 0:
            show_tile(player2)
            arrange_tile(player2)
            register(player2, tile, jud_success, board)
        elif jud_success == 1 or jud_success == 2:
            a = input("Menu : show_board(1), register_newtile(2), register_a_tile(3),pick_atile(4), show_tile(5)")
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
    else:
        if jud_success == 0 or jud_success == 1:
            show_tile(player2)
            arrange_tile(player2)
            register(player2, tile, jud_success, board)
        elif jud_success == 2:
            a = input("Menu : show_board(1), register_newtile(2), register_a_tile(3),pick_atile(4), show_tile(5)")
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


def tilegame():
    tile = make_tile()
    dist_tile(tile)
    turn_dice()
    for i in range(2):
        if turn == False:
            player1_turn()
            player2_turn()
            if jud_end() == 1:
                break
        else:
            player1_turn()
            player2_turn()
            if jud_end() == 1:
                break

tilegame()

