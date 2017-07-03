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
  ```
  id | username  | ranking
  ```
  * A `Game` is created with two players ids, a winner id (that can be null), a start time and a finish time (that can be null). There are two foreign keys that refer to player ids in the `Player` table.
  ```
   id | player1_id | player2_id | winner_id | started_at | finished_at
  ```
### Usage

The app is deployed on Heroku. You can access it [here](https://backend-ttt.herokuapp.com).

#### Demo
To get an overview of how the app works there are two demo routes:

1) [`backend-ttt.herokuapp.com`](https://backend-ttt.herokuapp.com) Seeds the database and displays info from the content of the players and games database tables.

2) [`backend-ttt.herokuapp.com/delete-records`](https://backend-ttt.herokuapp.com/delete-records) Enables you to delete the players and games records from the database tables.

#### Game
When playing a game of TicTacToe, the aim is for the frontend app to use the backend app as an API and reach the following routes:

1) [`backend-ttt.herokuapp.com/start-game`](https://backend-ttt.herokuapp.com/start-game) creates new rows in the players and games tables which generates their ids.

Use the link above and you'll return something like:
```
New game started (game id: 7, id player1: 4, id player2: 5)
```

2) [`backend-ttt.herokuapp.com/finish-game/7/4/laure/auguste`](https://backend-ttt.herokuapp.com/finish-game/7/4/laure/auguste) updates the rows created before with the winner of the game and the players' names.

Use the link above (note: make sure to update the players and game ids in the url) and you'll return something like:
```
Game (7) finished and won by auguste
```

3) [`backend-ttt.herokuapp.com/global-ranking/4`](https://backend-ttt.herokuapp.com/global-ranking/4) is not implemented yet, but aims at getting a player's rank amongst all players.

### Install

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
