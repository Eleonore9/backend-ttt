from __init__ import app
from model_pg import Player, Game, main, get_player_name, check_player

@app.route('/')
def homepage():
    '''Route used for demo purpose'''
    main()
    all_players = Player.all()
    names = [p.username for p in all_players]
    all_games = Game.all()
    games = ['game {0}: {1} vs {2}'.format((all_games.index(g) + 1),
                                           get_player_name(g.player1_id),
                                           get_player_name(g.player2_id))
             for g in all_games]
    return ''' Players:<br>{players_list}<br>
               <br>Scores:<br>{games_scores}'''.format(players_list="<br>".join(names),
                                                       games_scores="<br>".join(games))

@app.route('/start-game')
def start_game():
    '''Route called when players are ready to start a new game'''
    player1 = check_player(None)
    player2 = check_player(None)
    game = Game.new(player1.id, player2.id, None, None, None)
    return '''New game started (game id: {0}, id player1: {1},
              id player2: {2})'''.format(game.id, game.player1_id, game.player2_id)

@app.route('/finish-game/<game_id>/<winner_id>/<player1_name>/<player2_name>')
def finish_game(game_id, winner_id, player1_name, player2_name):
    '''Route called when the game is over'''
    # Get players and game ids and update games tables with 'winner_id' and 'finish_at'
    game = Game.get(game_id)
    Game.update_game(game, game_id, winner_id)
    player1 = Player.get_by_id(game.player1_id)
    Player.update_player(player1, player1.id, player1_name)
    player2 = Player.get_by_id(game.player2_id)
    Player.update_player(player2, player2.id, player2_name)
    winner_name = player1.username if player1.id == winner_id else player2.username
    return '''Game ({0}) finished and won by {1}'''.format(game.id, winner_name)

@app.route('/global-ranking/<player_id>')
def global_ranking(player_id):
    '''Route redirected to at the end to show the players rank'''
    # For a player id calculate rank, update player row with 'ranking', return ranking
    # Will call 'Player.calculate_ranking' and 'Player.get_player_rank'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
