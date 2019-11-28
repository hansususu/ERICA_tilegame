import random
player = []
computer = []

def make_tile():
    color = {"red","orange", "blue", "black"}
    number = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
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
        print(str(tile['color']) + str(tile['number']), end = ' ')
    print()

def register(player,tile) :

    if more("Do you want to register?(y/n) ") == True:

        answer1 = input("몇개의 묶음을 등록하시겠습니까?")

        answer1 = int(answer1)

        for i in range(answer1):

            answer2 = input("몇개의 타일을 입력하시겠습니까?")

            answer2 = int(answer2)

            arr = []

            print("타일을 입력해주세요!")

            for j in range(answer2):

                a,b= input().split()

                b = int(b)

                c = {'color': a, 'number': b}

                arr.append(c)

    else :

        print("You get 1 tile.")

        if tile != []:

            a = random.choice(tile)

            player.append(a)

            tile.remove(a)

            show_tile(player)

        else:

            print("타일이 없어요,,,")
