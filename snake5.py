#9 Function arguments 

import random

snake = {
    'photo': '~<:<<<<<<x---',
    'name' : 'Jafaar',
    'age' : 2,
    'weight' : '220,462',
    'hungry' : True,
    'phrases' : ['Kssss', 'Aiiiie connnnfiannnce', 'Seethaaa-ssse-hathehhh-hathehhh-ayaeeh'],
}

cat = {
    'photo': '=^._.^=',
    'name' : 'Kitty Purry',
    'age' : 2,
    'weight' : '10',
    'hungry' : True,
    'phrases' : ['Meow', 'mewmewmewmew', 'Purrrrrrrr', 'gurrhr', 'Kaaahhkkk'],
}

def chat_with_pet(pet):
    print(pet['name'] + ' says ' + random.choice(pet['phrases']))
    print()

def startup_pet():
    print('Welcome master')

def pet_stats(pet):
    print('Say hello to your new pet ' + pet['name'])
    print(pet['photo'])
    print(pet['name'] + ' weights ' + str(pet['weight']) + ' pounds')
    if pet['hungry']:
     print(pet['name'] + ' is hungry')
    else: 
     print(pet['name'] + ' BURPS loudly')

startup_pet()
pet_stats(cat)

terminate = False

while not terminate:
    print('###################')
    user_input = input()
    if user_input == 'quit':
        terminate = True

print ('You have quit your pet')