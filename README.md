## backend-ttt

This app aims to be the backend for a TicTacToe game.
It is a Python/Flask web app with a Postgres database.

### Features

* `backend_ttt.py` defines routes to be called from the actual game app:
  * `homepage` is not meant to be used, but more to demo the app.
  It displays the players and games in the database.
  * `start-game` is meant to be called at the start of a game to create or update the players and games database tables
  * `finish-game` is meant to be called at the end of the game to add the winner into the games database table and add the username of the players (that would have been asked by the game app) in the players database table.
  * `global-ranking` [to be implemented] is meant to display the ranking of the player once the game is over.

* `model_pg.py` defines the Postgres database model using the ORM SqlAlchemy.
  * A `Player` is created with a username and a ranking. The ranking can be null.
  * A `Game` is created with two players ids, a winner id (that can be null), a start time and a finish time (that can be null). There are two foreign keys that refer to player ids in the `Player` table.

### Install

The aim is for the app to be deployed on Heroku and accessible [here](https://backend-ttt.herokuapp.com). Unfortunately although the app is deployed it isn't functional.

Installing the app locally requires to have postgres set up ([instructions](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup)).

Steps:
1) Clone this repository:
```Bash
$ git clone git@github.com:Eleonore9/backend-ttt.git
$ cd backend-ttt/
```
2) Export the database url as an environment variable:
```Bash
$ export DATABASE_URL=postgres:///$(whoami)
```
3) Install the dependencies (better if in a virtual environment):
```Bash
$ pip3 install -r requirements.txt
```
4) Run the app:
```
$ python backend_ttt.py
```
