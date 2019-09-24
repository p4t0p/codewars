def create_empty_field():
    return {
        1: {
            'A': '♜',
            'B': '♞',
            'C': '♝',
            'D': '♛',
            'E': '♚',
            'F': '♝',
            'G': '♞',
            'H': '♜',
        },
        2: {
            'A': '♟',
            'B': '♟',
            'C': '♟',
            'D': '♟',
            'E': '♟',
            'F': '♟',
            'G': '♟',
            'H': '♟',
        },
        7: {
            'A': '♙',
            'B': '♙',
            'C': '♙',
            'D': '♙',
            'E': '♙',
            'F': '♙',
            'G': '♙',
            'H': '♙',
        },
        8: {
            'A': '♖',
            'B': '♘',
            'C': '♗',
            'D': '♕',
            'E': '♔',
            'F': '♗',
            'G': '♘',
            'H': '♖',
        }
    }
                
def find_in_field(i, j, field):
    try:
        return field[i][j]
    except:
        return ' '

def render(field, fallen):
    l = '  '
    for c in 'ABCDEFGH':
        l += '  ' + c + '  '

    print(l)

    white_fallen = len(fallen.get('white'))
    black_fallen = len(fallen.get('black'))

    for i in list(range(1, 9))[-1::-1]:
        divider = '  ' + '-----' * 8 + '-'

        if i == 3 or i == 5:
            divider += '-----------------'
        
        if i == 2:
            divider += ' Fallen whites ↓'
        if i == 6:
            divider += ' Fallen blacks ↑'
        
        print(divider)

        l = str(i) + ' '
        for j in 'ABCDEFGH':
            content = find_in_field(i, j, field)
            l += '| ' + content + '  '
        l += '|'
    
        if i >= 7 and fallen.get('black'):
            if black_fallen >= 0:
                t = 0
                while t < 3 and t < black_fallen:
                    l += ' ' + fallen.get('black')[t]
                    black_fallen -= 1
                    t += 1

        if i <= 2 and fallen.get('white'):
            if white_fallen >= 0:
                t = 0
                while t < 3 and t < white_fallen:
                    l += ' ' + fallen.get('white')[t]
                    white_fallen -= 1
                    t += 1
        
        print(l)

    print('  ' + '-----' * 8 + '-')

    print(fallen)

    return field

class Game:
    def __init__(self, field, moves):
        self.field = field
        self.moves = moves
        self.fallen = {
            'white': [],
            'black': []
        }
    
    def move(self, _from, _to):
        self.field = self._move_to(_from, _to)
        render(self.field, self.fallen)
        return self

    def _move_to(self, _from, _to):
        [from_i, from_j] = _from
        [to_i, to_j] = _to

        print(f"Movig from {from_i}{from_j} to {to_i}{to_j}\n")

        figure = self.find(from_i, from_j)

        if figure == ' ':
            print('No figure')
            return
        
        move_fn = self.moves[figure]

        move_result = move_fn(self, from_i, to_i, from_j, to_j)
        if move_result:
            del self.field[from_i][from_j] 
            if self.field.get(to_i):
                if self.field[to_i].get(to_j):
                    self.field[to_i][to_j] = figure
                else:
                    self.field[to_i] = self.field.get(to_i, {})
                    self.field[to_i][to_j] = figure
            else:
                self.field[to_i] = {to_j: figure}

            if isinstance(move_result, dict):
                self.fallen[move_result['color']].append(move_result['figure'])
        else:
            print('Not allowed')
        
        return self.field

    def find(self, i, j):
        return find_in_field(i, j, self.field)
    
            

def start(moves):
    field = create_empty_field()
    game = Game(field, moves)
    render(game.field, game.fallen)
    print('Game is sttarted')
    return game
