def feed_pet(game_state):
    pet_food = input(
            "What do you want to feed " + game_state["pet_name"] + "? ")
    print()

    if pet_food in game_state["pet_favorite_food"]:
        game_state["pet_happiness"] += 20
    elif pet_food in game_state["pet_hated_food"]:
        game_state["pet_happiness"] -= 40
    elif pet_food == "rocks":
        print("Hey, you are mean!")
        print()
        return
    else:
        game_state["pet_happiness"] -= 10

    print(game_state["pet_name"] + " eats the " + pet_food + ".")

    if game_state["pet_happiness"] >= 80:
        print(game_state["pet_name"] + " seems ecstatic!!")
    elif game_state["pet_happiness"] >= 50:
        print(game_state["pet_name"] + " is happy.")
    elif game_state["pet_happiness"] >= 25:
        print(game_state["pet_name"] + " seems sad.")
    else:
        print(game_state["pet_name"] + " is clearly depressed.")
    print()

    game_state["pet_hunger"] -= 20

    if game_state["pet_hunger"] <= 0:
            print(game_state["pet_name"] + " poops on the floor, bad pet!")
            print()
            game_state["poop_on_floor"] = True
            game_state["pet_hunger"] = 100


def play_with_pet(game_state):
    if game_state["pet_happiness"] < 50:
        print(game_state["pet_name"] + " isn't in the mood to play...")
        print()
        return

    if game_state["pet_hunger"] > 60:
        print(game_state["pet_name"] + " is too hungry to play!")
        game_state["pet_happiness"] -= 20
        return

    thrown_object = input("What do you want to fetch with? ")
    print()
    print("You throw the " + thrown_object + ".")
    print()

    if game_state["pet_happiness"] >= 80:
        print(
                game_state["pet_name"] + " catches "  + thrown_object)
    elif game_state["pet_happiness"] >= 70:
        print(
                game_state["pet_name"] + " takes its time to bring back " + thrown_object)
    else:
        print(
                game_state["pet_name"] + " watches the " + thrown_object + " fall and looks at you with dumb eyes")

    print()
    game_state["pet_hunger"] += 20


def put_pet_to_bed(game_state):
    print(game_state["pet_name"] + " goes back to bed. 😃")
    game_state["taking_care_of_pet"] = False


def clean_up_poop(game_state):
    if game_state["poop_on_floor"]:
        print("Goodbye,poop!")
        print()
        game_state["poop_on_floor"] = False
    else:
        print("The floor is already clean")


def cheat(game_state):
    print("You scratches its ears and back, " + game_state["pet_name"] + " purrs")
    game_state["pet_happiness"] = 100


game_state = {}
game_state["pet_favorite_food"] = ["pizza", "mouse","fingers","grass"]
game_state["pet_hated_food"] = ["tofu", "biscuits", "mash"]
game_state["pet_happiness"] = 50
game_state["pet_hunger"] = 100
game_state["poop_on_floor"] = False
print('Meet your new digital pet')
game_state["pet_name"] = input("What is its name?")
print(game_state["pet_name"] + ' is a happy pet')
print ('ฅ/ᐠ. ̫ .ᐟ\ฅ')
game_state["taking_care_of_pet"] = True

commands = {
        "feed": feed_pet, "play": play_with_pet, "quit": put_pet_to_bed,
        "clean": clean_up_poop, "pet": cheat}
print()

while game_state["taking_care_of_pet"]:
    if not game_state["poop_on_floor"]:
        pet_activity = input(
                "Do you want to 'feed' or 'play' with "
                + game_state["pet_name"] + "? ")
    else:
        pet_activity = input(
                "Do you want to 'feed' or 'play' with "
                + game_state["pet_name"] + ", or do you want to "
                + "'clean' the room? ")
    print()

    try:
        command_callable = commands[pet_activity]
    except KeyError:
        print("Please type either 'feed', 'play', 'pet', 'quit', or 'clean'.")
    command_callable(game_state)

    if game_state["pet_hunger"] > 70:
        print(game_state["pet_name"] + " seems kind of hungry...")
        print()
        game_state["pet_happiness"] -= 10

    if game_state["poop_on_floor"]:
        game_state["pet_happiness"] -= 10

    if game_state["pet_happiness"] <= 0:
        print(
                game_state["pet_name"] + " bites you! And then poops "
                + "on the carpet!")
        print("You run away because of fear...")
        game_state["taking_care_of_pet"] = False
     
print ("You have abandoned your pet, you monster!")
print("Game Over")
