from chess.main import start as StartGame
from chess.helpers import inverse, compare, get_range, to_x_cord, from_x_cord

def pawn(game, from_i, to_i, from_j, to_j):
    color = game.queue
    is_straight = from_j == to_j
    move_to_fig = game.find(to_i, to_j)

    max_move = 1
    if (color is 'black' and from_i == 2) or (color is 'white' and from_i == 7):
        max_move = 2

    if is_straight:
        return move_to_fig == ' ' and to_i - from_i <= max_move if color is 'black' else from_i - to_i <= max_move
    else:
        if abs(compare(from_j, to_j)) <= max_move and move_to_fig != ' ' and game.get_color(move_to_fig) != color:
            return {
                'figure': move_to_fig,
                'color': inverse(color),
            }
        else:
            return False

def rook(game, from_i, to_i, from_j, to_j):
    color = game.queue
    is_horizontal = from_i == to_i
    is_vertical = from_j == to_j
    move_to_fig = game.find(to_i, to_j)

    if is_horizontal:
        for x in get_range(to_x_cord(from_j), to_x_cord(to_i)):
            if game.find(to_i, from_x_cord(x)) != ' ':
                    return False
    else:
        for y in get_range(from_i, to_i):
            if game.find(y,to_j) != ' ':
                    return False

    if move_to_fig != ' ':
        return game.get_color(move_to_fig) != color
    
    return True

moves = {
    '♙': pawn,
    '♟': pawn,
    '♜': rook,
    '♖': rook,
}

game = StartGame(moves)