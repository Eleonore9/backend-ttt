from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey, delete
from sqlalchemy import Column, Integer, String, DateTime, Boolean
import datetime
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session

engine = create_engine('sqlite:///backend-ttt.db', echo=True)
session = scoped_session(sessionmaker(bind=engine,
                                      autocommit = False,
                                      autoflush = False))
Base = declarative_base()
Base.query = session.query_property()

class Player(Base):
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
        session.add(player)
        session.commit()
        return player

    @classmethod
    def get(cls, id):
        player = session.query(Player).get(id)
        return player

    # Instance methods
    def get_player_rank(self, player_id):
        player = session.query(Player).get(id)
        rank = player.ranking
        return rank

    def update_num_games(self, player_id):
        #num1 = session.query(Game).filter_by()
        return 'foo'
        # TO BE FINISHED

    def update_ranking(self, player_id):
        foo = 'foo'
        return foo
       # TO BE FINISHED


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key = True)
    player1_id = Column(Integer, ForeignKey('players.id'), nullable=False)
    player2_id = Column(Integer, ForeignKey('players.id'), nullable=False)
    score_player1 = Column(Integer, nullable=True)
    score_player2 = Column(Integer, nullable=True)
    started_at = Column(DateTime())
    finished_at = Column(DateTime())

    player1 = relationship('Player', foreign_keys=[player1_id])
    player2 = relationship('Player', foreign_keys=[player2_id])

    def __init__(self, player1_id, player2_id, score_player1,
                 score_player2, started_at, finished_at):
        self.player1_id = player1_id
        self.player2_id = player2_id
        self.score_player1 = score_player1
        self.score_player2 = score_player2
        self.started_at = started_at
        self.finished_at = finished_at

    @classmethod
    def new(cls, player1_id, player2_id, score_player1,
            score_player2, started_at, finished_at):
        now = datetime.datetime.now()
        game = Game(player1, player2, None, None, now, None)
        session.add(post)
        session.commit()
        return game

    @classmethod
    def get(cls, id):
        game = session.query(Game).get(id)
        return game

    @classmethod
    def all(cls):
        games = session.query(Game).order_by(Game.id.desc()).all()
        return games

    # Instance method
    def get_player_score(self, player_id):
        foo = 'foo'
        return foo
        # TO BE FINISHED


if __name__ == "__main__":
    print('FOO')
    Base.metadata.create_all(engine)
    playerA = Player.new("eleonore", 0, 1)
    print(playerA)
