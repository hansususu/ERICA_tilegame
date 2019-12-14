import random 
player1 = []
player2 = []

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
    print("my tile is")
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

def make_board():
    global board
    board = [[0 for i in range(13)]for j in range(13)]

def register(who,tile) :
    if more("Do you want to register?(y/n) ") == True:
        global answer1
        answer1 = input("몇개의 묶음을 등록하시겠습니까?")
        while answer1.isdigit() == False:
            answer1 = input("몇개의 묶음을 등록하시겠습니까?")
        answer1 = int(answer1)
        sum = 0
        cpboard = board
        realcard(who)
        show_tile(who)
        row = len(board)
        col = len(board[0])       
        a = []
        cptile = who
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
            origin = []
            origin1 = []
            jud_board = []
            for j in range(13):
                if (board[jud_row-1][j] != 0):
                    origin.append(board[jud_row-1][j])
                    origin1.append(board[jud_row-1][j])
                    jud_board.append(board[jud_row-1][j])
            origin.sort(key = lambda x: x['number'])
            origin1.sort(key = lambda x: (x['color'],x['number']))
            if jud_board != origin or jud_board != origin1:
                jud = 1
            else:
                jud = 0
        for i in range(len(a)):
            sum += a[i]['number']
        if judge == True:
            if sum <= 30:
                print("Sum is not over 30")
                print("You get 1 tile.")
                who = cptile
                board = cpboard
                emptytile(who)
            elif jud == 1:
                print("You entered an unaligned tiles.")
                print("You get 1 tile.")
                who = cptile
                board = cpboard
                emptytile(who)
            else:
                print("You success to register.")
    else :
        print("You get 1 tile.")
        who = cptile
        board = cpboard
        emptytile(who)

def realcard(who):
    row = 0
    for i in range(13):
        if board[i] != [0,0,0,0,0,0,0,0,0,0,0,0,0]:
            row += 1
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
    cptile = who
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
        except:
            print("Tile input is no formatted.")
            print("Please re-enter the tile.")
            who = cptile
            enter_tile(i,who)

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

def regist_newtile(who):
    ans = input("몇개의 묶음을 등록하시겠습니까?")
    while ans.isdigit() == False:
        ans = input("몇개의 묶음을 등록하시겠습니까?")
    ans = int(ans)
    row = len(board)
    real_row = 0
    for i in range(row):
        if board[i] != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
            real_row += 1
    for i in range(ans):
        ans1 = input("How many tiles do you want to enter?")
        while ans1.isdigit() == False:
            ans1 = input("How many tiles to you want to enter?")
        ans1 = int(ans1)
        cpboard = board
        bdrow = 0
        for i in range(13):
            if board[i] != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0]:
                bdrow += 1
        for i in range(ans):
            realcard(who)
        for i in range(ans):
            jud_col1 = board[bdrow]
            jud_col2 = board[bdrow]
            origin = board[bdrow]
            jud_col1.sort(key = lambda x: x['number'])
            jud_col2.sort(key = lambda x: (x['color'],x['number']))
            if origin != jud_col1 or origin != jud_col2:
                jud_col = 1
                bdrow += 1
            else:
                jud_cold = 0
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
    ans = int(ans)
    col = 0
    cpcol = board[ans]
    for i in range(13):
        if board[ans][i] != 0:
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
    if c in who:
        board[i].insert(th,c)
    jud_col1 = []
    jud_col2 = []
    for i in range(col):
        if (board[ans-1][i] != 0):
            jud_col1.append(board[ans-1][i])
            jud_col2.append(board[ans-1][i])
    jud_col1.sort(key = lambda x: x['number'])
    jud_col2.sort(key = lambda x: (x['color'], x['number']))
    if board != jud_col1 or board != jud_col2:
        print("You should enter unaligned tile")
        print("Pleas re-enter a tile.")
        board[ans] = cpcol
        regist_newtile(who)

def tilegame():
    tile = make_tile()
    dist_tile(tile)
    show_tile(player1)
    arrange_tile(player1)
    register(player1, tile)
    a = 0
    while a != 4:
        a = input("Menu : show_board(1), register_newtile(2), register_a_tile(3), pass(4)")
        if a == 1:
            show_regboard()
        elif a == 2:
            regist_newtile(player1,board)
        elif a == 3:
            regist_atile(player1)
        
tilegame()

