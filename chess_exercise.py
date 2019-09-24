from chess.main import start as StartGame

def compare(a, b):
    l = 'ABCEDFGH'
    return l.index(a) - l.index(b)

def inverse(color):
    return 'white' if color == 'black' else 'black'

def pawn(color):
    def move_to(game, from_i, to_i, from_j, to_j):
        is_straight = from_j == to_j
        move_to_fig = game.find(to_i, to_j)

        if is_straight:
            return to_i - from_i == (1 if color == 'black' else -1 ) and move_to_fig == ' '
        else:
            if abs(compare(from_j, to_j)) and move_to_fig != ' ':
                return {
                    'figure': move_to_fig,
                    'color': inverse(color),
                }
            else:
                return false

    return move_to

moves = {
    '♙': pawn('white'),
    '♟': pawn('black'),
}

game = StartGame(moves)

game.move([2, 'A'], [3, 'A']) \
    .move([3, 'A'], [4, 'A']) \
    .move([4, 'A'], [5, 'A']) \
    .move([5, 'A'], [6, 'A']) \
    .move([6, 'A'], [7, 'B']) \
    .move([7, 'A'], [6, 'A']) \
    .move([6, 'A'], [5, 'A']) \
    .move([5, 'A'], [4, 'A']) \
    .move([4, 'A'], [3, 'A']) \
    .move([3, 'A'], [2, 'A']) \
    .move([2, 'A'], [1, 'B'])
