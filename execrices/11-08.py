# dicts in python

d = {
    'key_name': 'Key Value'
}

# get key's value
d['key_name'] # 'Key Value'
d.get('key_name') # 'Key Value'

# set key value
d['another_key'] = 500;


def generate_user(name, age):
    user = {
        'name':name,
        'age':age
    }
    return user
    
users = [
    generate_user('John', 12),
    generate_user('Dave', 22),
    generate_user('Oleg', 42),
    generate_user('Tim', 31),
    generate_user('Kianu', 15),
]
def filter_correct_ages(users, age = 16):
    result = []
    for i in users:
        if i.get('age') >= age:
            result.append(i)
            
    return result