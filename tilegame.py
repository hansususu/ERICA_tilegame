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

def arrange_tile(player):
    answer = input("Do you want sort? (789/777/NO")
    while not (answer == '789' or answer == '777' or answer == 'NO') :
        answer == input("Do you want sort? (789/777/NO")
    if answer == '777':
        player.sort(key=lambda x: x['number'])
    elif answer == '789':
        player.sort(key=lambda x: (x['color'], x['number']))


