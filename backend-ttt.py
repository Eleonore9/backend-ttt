from flask import Flask
import model-sqlite

app = Flask(__name__)

@app.route('/')
def foo():
    p = model-sqlite.Player.get(1)
    name = p.username
    return 'Player 1 is {}'.format(name)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
