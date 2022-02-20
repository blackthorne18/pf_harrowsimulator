import random
import numpy as np
import sys
from tabulate import tabulate
import os

harrow = {
    'str': [
        'Palladin -LG', 'Keep -NG', 'Big Sky -CG',
        'Forge -LN', 'Bear -NN', 'Uprising -CN',
        'Fiend -LE', 'Beating -NE', 'Cyclone -CE'
    ],
    'dex': [
        'Dance -LG', 'Cricket -NG', 'Juggler -CG',
        'Locksmith -LN', 'Peacock -NN', 'Rabbit Prince -CN',
        'Avalanche -LE', 'Crows -NE', 'Demons Lantern -CE'
    ],
    'con': [
        'Trumpet -LG', 'Survivor -NG', 'Desert -CG',
        'Brass Dwarf -LN', 'Teamster -NN', 'Mountain Man -CN',
        'Tangled Briar -LE', 'Sickness -NE', 'Waxworks -CE'
    ],
    'wis': [
        'Winged Serpent -LG', 'Midwife -NG', 'Publican -CG',
        'Queen Mother -LN', 'Owl -NN', 'Carnival -CN',
        'Eclipse -LE', 'Mute Hag -NE', 'Lost -CE'
    ],
    'int': [
        'Hidden Truth -LG', 'Wanderer -NG', 'Joke -CG',
        'Inquisitor -LN', 'Foreign Trader -NN', 'Vision -CN',
        'Rakshasa -LE', 'Idiot -NE', 'Snakebite -CE'
    ],
    'cha': [
        'Empty Throne -LG', 'Theatre -NG', 'Unicorn -CG',
        'Marriage -LN', 'Twin -NN', 'Courtesan -CN',
        'Tyrant -LE', 'Betrayal -NE', 'Liar -CE'
    ]
}

alignment = [
    ['LG', 'LN', 'CG'],
    ['LN', 'NN', 'CN'],
    ['LE', 'NE', 'CE']
]

gridid = {
    1: (1, 1), 2: (1, 2), 3: (1,3),
    4: (2, 1), 5: (2, 2), 6: (2,3),
    7: (3, 1), 8: (3, 2), 9: (3,3)
}

def getgrid(key, pos):
    card_grid = [[0 for _ in range(3)] for _ in range(3)]
    card_player = [[0 for _ in range(3)] for _ in range(3)]
    s = list(range(9))
    random.shuffle(s)
    grid = [[0 for _ in range(3)] for _ in range(3)]
    ct = 0
    for i in range(len(grid)):
            for j in range(len(grid[i])):
                    grid[i][j] = s[ct]
                    card = harrow[key][s[ct]].split(" -")
                    if card[1] == alignment[i][j]:
                        card[1] = "true"
                    elif card[1] == alignment[j][i]:
                        card[1] = "oppo"
                    elif card[1][0] == alignment[i][j][0] or card[1][1] == alignment[i][j][1]:
                        card[1] = "part"
                    else:
                        card[1] = "misc"
                    card_grid[i][j] = " -".join(card)
                    card_player[i][j] = card[0]
                    ct += 1
    # print(tabulate(np.array(alignment), tablefmt="grid"))
    # print(tabulate(np.array(grid), tablefmt="grid"))
    os.system("clear")
    headers = ["My Copy", f"Suite: {key.upper()}", f"Role Card: {pos}"]
    print(tabulate(np.array(card_grid), headers=headers, tablefmt="grid"))
    headers = ["Player Copy", f"Suite: {key.upper()}", f"Role Card: {pos}"]
    print(tabulate(np.array(card_player), headers=headers, tablefmt="grid"))


key, pos = sys.argv[1].split(",")
pos = gridid[int(pos)]
getgrid(key, pos)

