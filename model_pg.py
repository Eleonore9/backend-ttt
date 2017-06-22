from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
import datetime, os
from sqlalchemy.orm import relationship
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Player(db.Model):
    __tablename__ = "players"

    id = Column(Integer, primary_key = True)
    username = Column(String(20), nullable=False)
    num_games_played = Column(Integer, nullable=False)
    ranking = Column(Integer, nullable=True)

    def __init__(self, username, num_games_played, ranking):
        self.username = username
        self.num_games_played = num_games_played
        self.ranking = ranking

    @classmethod
    def new(cls, username, num_games_played, ranking):
        player = Player(username, num_games_played, None)
        db.session.add(player)
        db.session.commit()
        return player

    @classmethod
    def all(cls):
        players = Player.query.order_by(Player.id.desc()).all()
        return players

    @classmethod
    def get_by_id(cls, id):
        player = Player.query.get(id)
        return player

    @classmethod
    def get_by_username(cls, username):
        players = Player.query.filter_by(username=username).first()
        return players

    # Instance methods
    def get_username_from_id(self, player_id):
        player = Player.query.get(player_id)
        return player.username

    def update_player(self, player_id, player_name):
        player = Player.query.get(player_id)
        player.username = player_name
        db.session.commit()

    def update_num_games(self, player_id):
        return 'foo'
        # TO BE FINISHED

    def calculate_ranking(self, player_id):
        return 'foo'
        # TO BE FINISHED

    def get_player_rank(self, player_id):
        player = Player.query.get(player_id)
        rank = player.ranking
        return rank


class Game(db.Model):
    __tablename__ = "games"

    id = Column(Integer, primary_key = True)
    player1_id = Column(Integer, ForeignKey('players.id'), nullable=False)
    player2_id = Column(Integer, ForeignKey('players.id'), nullable=False)
    winner_id = Column(Integer, nullable=True)
    started_at = Column(DateTime())
    finished_at = Column(DateTime())

    player1 = relationship('Player', foreign_keys=[player1_id])
    player2 = relationship('Player', foreign_keys=[player2_id])

    def __init__(self, player1_id, player2_id, winner_id, started_at, finished_at):
        self.player1_id = player1_id
        self.player2_id = player2_id
        self.winner_id = winner_id
        self.started_at = started_at
        self.finished_at = finished_at

    @classmethod
    def new(cls, player1_id, player2_id, winner_id, started_at, finished_at):
        now = datetime.datetime.now()
        game = Game(player1_id, player2_id, None, now, None)
        db.session.add(game)
        db.session.commit()
        return game

    @classmethod
    def get(cls, id):
        game = Game.query.get(id)
        return game

    @classmethod
    def all(cls):
        games = Game.query.order_by(Game.id.desc()).all()
        return games

    # Instance method
    def update_game(self, game_id, winner_id):
        now = datetime.datetime.now()
        game = Game.query.get(game_id)
        game.winner_id = winner_id
        game.finished_at = now
        db.session.commit()

    def get_player_score(self, player_id):
        foo = 'foo'
        return foo
        # TO BE FINISHED


def check_player(name):
    '''Add a new player if they don't exist already'''
    if name is None:
        player = Player.new('unknown', 1, None)
    else:
        player = Player.get_by_username(name)
        if not player:
            player = Player.new(name, 1, None)
    return player

def get_player_name(id):
    '''Get the name of a player from it's id'''
    player = Player.get_by_id(id)
    name = Player.get_username_from_id(player, id)
    return name


def main():
    '''Create tables and seed them with fake players and games.'''
    db.create_all(bind=None)
    eleonore = check_player('éléonore')
    gaspard = check_player('gaspard')
    ma = check_player('marie-amélie')
    Game.new(eleonore.id, gaspard.id, None, None, None)
    Game.new(eleonore.id, ma.id, None, None, None)
    Game.new(gaspard.id, ma.id, None, None, None)


if __name__ == "__main__":
    # chantal = Player.new("chantal", 0, 1)
    # victor = Player.new("victor", 0, 1)
    # Game.new(chantal.id, victor.id, None, None, None)
    manager.run()
