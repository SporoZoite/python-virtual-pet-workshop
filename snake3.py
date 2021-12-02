#6.Python's standard library
import random

name = 'Bitey'

#7.Lists
phrases = ['Kssss', 'Aiiiie connnnfiannnce', 'Seethaaa-ssse-hathehhh-hathehhh-ayaeeh']

def chat_with_snake():
    print(name + ' says ' + random.choice(phrases) )
    print()

def startup_snake():
    print('Welcome master')

startup_snake()

terminate = False

while not terminate:
    print('###################')
    user_input = input()
    if user_input == 'quit':
        terminate = True
    elif user_input == 'chat':
       chat_with_snake() 
    else:
        print('command not recognised, try again') 

print ('You have quit your snake')

#okay, further?