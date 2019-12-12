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

def register(who,tile) :
    if more("Do you want to register?(y/n) ") == True:
        global answer1
        answer1 = input("몇개의 묶음을 등록하시겠습니까?")
        while answer1.isdigit() == False:
            answer1 = input("몇개의 묶음을 등록하시겠습니까?")
        answer1 = int(answer1)
        sum = 0
        global board
        board = [[0 for i in range(13)]for j in range(13)]
        realcard(who)
        show_tile(who)
        row = len(board)
        col = len(board[0])       
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
                emptytile(who)
            elif jud == 1:
                print("You entered an unaligned tiles.")
                print("You get 1 tile.")
                emptytile(who)
            else:
                print("You success to register.")
    else :
        print("You get 1 tile.")
        emptytile(who)

def realcard(who):
    for i in range(answer1):
        global answer2
        answer2 = input("How many tiles do you want to enter?")
        while answer2.isdigit() == False:
            answer2 = input("How many tiles do you want to enter?")
        answer2 = int(answer2)
        if answer2 >= 3:
            enter_tile(i,who)
        else:
            print("You should register more than 3 tiles.")
            print("Please re-enter.")
            realcard(who)

def enter_tile(i,who):
    print("Please enter tiles!")
    for j in range(answer2):
        try:
            a, b = input().split()
            b = int(b)
            c = {'color':a, 'number':b}
            if c in who:
                board[i][j] = c
                who.remove(c)
                global judge
                judge = True
            else:
                print("This tile is not yours")
                print("Please re-enter the tile.")
                enter_tile(i,who)
        except:
            print("Tile input is no formatted.")
            print("Please re-enter the tile.")
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
    for i in range(jud_row):
        print(i+1,'th:')
        for j in range(13):
            if board[i][j] != 0:
                print(str(board[i][j]['color'])+' '+str(board[i][j]['number']), end = ' ')

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
        if ans1 >= 3:
            for j in range(ans1):
                try:
                    a, b = input().split()
                    b = int(b)
                    c = {'color':a, 'number':b}
                    if c in who:
                        board[real_row][j] = c
                        who.remove(c)
                    else:
                        print("This tile is not yours.")
                        print("Please re-enter the tile.")
                except:
                    print("Tile input is not formatted.")
                    print("Please re-enter the tile.")
        else:
            print("You should register more than 3 tiles.")
            print("Please re-enter")
            regist_newtile(who)
        
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
    register(player1,tile)
    show_regboard()
    regist_newtile(player1)
    show_regboard() 

tilegame()

