#8 Dictionaries
# to store data values in key:value pairs

import random

snake = {
    'photo': '~<:<<<<<<x---',
    'name' : 'Jafaar',
    'age' : 2,
    'weight' : '220,462',
    'hungry' : True,
    'phrases' : ['Kssss', 'Aiiiie connnnfiannnce', 'Seethaaa-ssse-hathehhh-hathehhh-ayaeeh'],
}

def chat_with_snake():
    print(snake['name'] + ' says ' + random.choice(snake['phrases']))
    print()

def startup_snake():
    print('Welcome master')

def snake_stats():
    print('Say hello to your new pet ' + snake['name'])
    print(snake['photo'])
    print(snake['name'] + ' weights ' + str(snake['weight']) + ' pounds')
    if snake['hungry']:
     print(snake['name'] + ' is hungry')
    else: 
     print(snake['name'] + ' BURPS loudly')

startup_snake()
snake_stats()

terminate = False

while not terminate:
    print('###################')
    user_input = input()
    if user_input == 'quit':
        terminate = True

print ('You have quit your snake')