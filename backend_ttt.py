#from flask import Flask
from model_pg import app, Player, Game, main, get_player_name

@app.route('/')
def homepage():
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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    main()
