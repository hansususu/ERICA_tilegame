import random 
player = []
computer = []

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
        player.append(a)
        tile.remove(a)
        b = random.choice(tile)
        computer.append(b)
        tile.remove(b)

def show_tile(player):
    print("my tile is")
    for tile in player:
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

def register(player,tile) :
    if more("Do you want to register?(y/n) ") == True:
        global answer1
        answer1 = input("몇개의 묶음을 등록하시겠습니까?")
        while answer1.isdigit() == False:
            answer1 = input("몇개의 묶음을 등록하시겠습니까?")
        answer1 = int(answer1)
        sum = 0
        global board
        board = [[0 for i in range(13)]for j in range(13)]
        realcard()
        show_tile(player)
        row = len(board)
        col = len(board[0])       
        a = []
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
                    jud_board.append(board[jud_row-1][j])
                    jud_board.append(board[jud_row-1][j])
            origin.sort(key = lambda x: x['number'])
            origin1.sort(key = lambda x: x['number'])
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
                emptytile()
            elif jud == 1:
                print("You entered an unaligned tiles.")
                print("You get 1 tile.")
                emptytile()
            else:
                print("You success to register.")
    else :
        print("You get 1 tile.")
        emptytile()

def realcard():
    for i in range(answer1):
        global answer2
        answer2 = input("How many tiles do you want to enter?")
        while answer2.isdigit() == False:
            answer2 = input("How many tiles do you want to enter?")
        answer2 = int(answer2)
        enter_tile(i)

def enter_tile(i):
    print("Please enter tiles!")
    for j in range(answer2):
        try:
            a, b = input().split()
            b = int(b)
            c = {'color':a, 'number':b}
            if c in player:
                board[i][j] = c
                player.remove(c)
               global judge
                judge = True
            else:
                print("This tile is not yours")
                print("Please re-enter the tile.")
                enter_tile(i)
        except:
            print("Tile input is no formatted.")
            print("Please re-enter the tile.")
            enter_tile(i)

def emptytile():
    if tile != []:
        a = random.choice(tile)
        player.append(a)
        tile.remove(a)
        show_tile(player)
    else:
        print("There are no tile.")

def arrange_tile(player):
    answer = input("Do you want sort? (789/777/NO)")
    while not (answer == '789' or answer == '777' or answer == 'NO'):
        answer = input("Do you want sort? (789/777/NO)")
    if answer == '777':
        player.sort(key=lambda x: x['number'])
    elif answer == '789':
        player.sort(key=lambda x: (x['color'], x['number']))

def tilegame():
    tile = make_tile()
    dist_tile(tile)
    show_tile(player)
    arrange_tile(player)
    show_tile(player)
    register(player,tile)

tilegame()

