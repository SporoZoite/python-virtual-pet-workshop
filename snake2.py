#4.functions

photo = '~<:<<<<<<x---'
name = 'Jafaar'
age = 2
weight = 220,462
hungry = True

def startup_snake():
    print('Welcome')

def snake_stats():
    print('Say hello to your new pet ' + name)
    print(photo)
    print(name + ' weights ' + str(weight) + ' pounds')
    if hungry:
     print(name + ' is hungry')
    else: 
     print(name + ' BURPS loudly')

startup_snake()
snake_stats()


#5.while loops

terminate = False

while not terminate:
    print('###################')
#ask user input
#input() is a function that allows the user to input a string in your program
    user_input = input()
#allow user to quit 
    if user_input == 'quit':
        terminate = True
    elif user_input == 'feed':
        print('nomnomnomnom')
        weight = weight + 1
        hungry = False
    else:
        print('command not recognised, try again') 

print ('You have quit your snake')

#nice, let's go a little further
