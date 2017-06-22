#from flask import Flask
from model_pg import app, Player, Game, main

def get_player_name(id):
    player = Player.get_by_id(id)
    name = Player.get_username_from_id(player, id)
    return name

@app.route('/')
def foo():
    all_players = Player.all()
    names = [p.username for p in all_players]
    print(names)
    all_games = Game.all()
    games = ['game {0}: {1} vs {2}'.format((all_games.index(g) + 1),
                                           get_player_name(g.player1_id),
                                           get_player_name(g.player2_id))
             for g in all_games]
    print(games)
    #return 'Player 1 is {}'.format(name)
    return ''' Players:<br>{players_list}<br>
               <br>Scores:<br>{games_scores}'''.format(players_list="<br>".join(names),
                                                       games_scores="<br>".join(games))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    main()
