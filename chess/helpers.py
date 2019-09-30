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
