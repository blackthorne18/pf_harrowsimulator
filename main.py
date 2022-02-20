# --------------------------------------------------------------------------------
"""
Functions getuserdata() and adduserdata() was written from:
https://towardsdatascience.com/talking-to-python-from-javascript-flask-and-the-fetch-api-e0ef3573c451
"""
# --------------------------------------------------------------------------------
from flask import Flask, render_template, request, jsonify, redirect, url_for
app = Flask(__name__, template_folder='static')

testset = [
    ['Uprising -misc', 'Fiend -part', 'Cyclone -part'],
    ['Forge -true', 'Keep -part', 'Bear -part'],
    ['Beating -part', 'Big Sky -misc', 'Palladin -misc']
]


@app.route('/chosenability/<chosenstat>', methods=['GET', 'POST'])
def chosenability(chosenstat):
    if request.method == 'GET':
        dmmode = {}
        playermode = {}
        for i in range(len(testset)):
            for j in range(len(testset[i])):
                tit, match = testset[i][j].split(" -")
                dm = {'gtit': tit, 'gmatch': match, 'gbody': "lorem ipsum"}
                dmmode[str(i + 1) + str(j + 1)] = dm
                playermode[str(i + 1) + str(j + 1)] = dm

        # modes_db = {'psychic': dmmode, 'player': playermode}
        modes_db = dmmode

        return jsonify(modes_db)
    if request.method == 'POST':
        print(request.get_json())
        return 'Sucesss', 200


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
