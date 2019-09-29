from chess.main import start as StartGame

def compare(a, b):
    l = 'ABCDEFGH'
    return l.index(a) - l.index(b)

def inverse(color):
    return 'white' if color == 'black' else 'black'

def get_range(a, b):
    if a<b:
        return list(range(a+1,b))
    else:
        return list(range(b+1,a))

def to_x_cord(letter):
    return 'ABCDEFGH'.index(letter)
def from_x_cord(num):
    return 'ABCDEFGH'[num]



def pawn(color):
    def move_to(game, from_i, to_i, from_j, to_j):
        is_straight = from_j == to_j
        move_to_fig = game.find(to_i, to_j)

        if is_straight:
            return to_i - from_i == (1 if color == 'black' else -1 ) and move_to_fig == ' '
        else:
            if abs(compare(from_j, to_j))==1 and move_to_fig != ' ':
                return {
                    'figure': move_to_fig,
                    'color': inverse(color),
                }
            else:
                return False

    return move_to

def rook(color):
    def move_to(game, from_i, to_i, from_j, to_j):
        is_horizontal = from_i == to_i
        is_vertical = from_j == to_j
        move_to_fig = game.find(to_i, to_j)
        if is_horizontal:
            for x in get_range(to_x_cord(from_j),to_x_cord(to_i)):
                if game.find(to_i,from_x_cord(x)) != ' ':
                     return False
        else:
            for y in get_range(from_i, to_i):
                if game.find(y,to_j) != ' ':
                     return False
        return True       
    return move_to

moves = {
    '♙': pawn('white'),
    '♟': pawn('black'),
    '♜': rook('black'),
    '♖': rook('white')
}

game = StartGame(moves)

game.move([2, 'A'], [3, 'A'])