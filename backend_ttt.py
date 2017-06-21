#from flask import Flask
from model_pg import app, Player, Game


@app.route('/')
def foo():
    p = Player.get(1)
    print(p)
    name = p.username
    return 'Player 1 is {}'.format(name)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
