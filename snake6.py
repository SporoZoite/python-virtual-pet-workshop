#10 For loops
import random
#move your pets in an array
pets = [
   {
    'photo': '~<:<<<<<<x---',
    'name' : 'Jafaar',
    'age' : 2,
    'weight' : '220,462',
    'hungry' : True,
    'phrases' : ['Kssss', 'Aiiiie connnnfiannnce', 'Seethaaa-ssse-hathehhh-hathehhh-ayaeeh'],
   },

   {
    'photo': '=^._.^=',
    'name' : 'Kitty Purry',
    'age' : 2,
    'weight' : '10',
    'hungry' : True,
    'phrases' : ['Meow', 'mewmewmewmew', 'Purrrrrrrr', 'gurrhr', 'Kaaahhkkk'],
   }
]

def startup_pet():
    print('Welcome master')
    print('Which pet do you choose?')
    for pet in pets:
        print (pet['name'])
    pet_choice = input()
    for pet in pets:
        if pet['name'] == pet_choice:
            print(pet['name'] + ' already loves you!')
            #when called functions return a value
            return pet 
    print('No pet answers by this name')
    return startup_pet()

def pet_stats(pet):
    print('Say hello to your new pet ' + pet['name'])
    print(pet['photo'])
    print(pet['name'] + ' weights ' + str(pet['weight']) + ' pounds')
    if pet['hungry']:
     print(pet['name'] + ' is hungry')
    else: 
     print(pet['name'] + ' BURPS loudly')

pet = startup_pet()
pet_stats(pet)

terminate = False

while not terminate:
    print('###################')
    user_input = input()
    if user_input == 'quit':
        terminate = True

print ('You have quit your pet')