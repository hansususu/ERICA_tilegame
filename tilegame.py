import random
player = []
computer = []

def make_tile():
    color = {"red","orange", "blue", "black"}
    number = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
    deck = []
    for i in color:
        for j in number:
            ap = {'color':i, 'number':j}
            deck.append(ap)
    ap = {'color':"colorful", 'number':"joker"}
    deck.append(ap)
    ap = {'color':"blackandwhite", 'number':"joker"}
    deck.append(ap)
    random.shuffle(deck)
    return deck
