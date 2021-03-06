# --------------------------------------------------------------------------------
"""
Functions getuserdata() and adduserdata() was written from:
https://towardsdatascience.com/talking-to-python-from-javascript-flask-and-the-fetch-api-e0ef3573c451
"""
# --------------------------------------------------------------------------------
from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
from tabulate import tabulate
import numpy as np
import random
app = Flask(__name__, template_folder='static')

harrow_cards = json.load(open("data/harrow_cards.json"))
harrow_details = json.load(open("data/harrow_details.json"))
alignment = [
    ['LG', 'LN', 'CG'],
    ['LN', 'NN', 'CN'],
    ['LE', 'NE', 'CE']
]


def getharrowdeal(chosenstat):
    testset = harrow_cards[chosenstat]
    dmmode = {}
    s = list(range(9))
    grid = [[0 for _ in range(3)] for _ in range(3)]
    cardboard = [[0 for _ in range(3)] for _ in range(3)]
    random.shuffle(s)
    asciinamedict = {'True': "(1)", 'Partial': "(0.5)",
                     'Opposite': "(-1)", '_': ""}
    ct = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            card = testset[s[ct]].split(" -")
            if card[1] == alignment[i][j]:
                card[1] = "True"
            elif card[1] == alignment[j][i]:
                card[1] = "Opposite"
            elif card[1][0] == alignment[i][j][0] or card[1][1] == alignment[i][j][1]:
                card[1] = "Partial"
            else:
                card[1] = "_"
            tit, match = card
            dm = {'gtit': tit, 'gmatch': match,
                  'gbody': harrow_details[tit]}
            dmmode[str(i + 1) + str(j + 1)] = dm
            cardboard[i][j] = " ".join([card[0], asciinamedict[card[1]]])
            ct += 1

    headers = ["", f"Suite: {chosenstat.upper()}", ""]
    asciitable = tabulate(np.array(cardboard),
                          headers=headers, tablefmt="grid")

    return dmmode, asciitable


@app.route('/chosenability/<chosenstat>', methods=['GET', 'POST'])
def chosenability(chosenstat):
    if request.method == 'GET':

        modes_db, asciitable = getharrowdeal(chosenstat)
        sendvalue = {'modes_db': modes_db, 'asciitable': asciitable}
        return jsonify(sendvalue)
    if request.method == 'POST':
        print(request.get_json())
        return 'Sucesss', 200


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
