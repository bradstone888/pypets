#!/usr/bin/env python3

# Set available pet types and actions
pet_types = ('dog', 'cat', 'rabbit', 'lizard', 'bird', 'fish')
petActions = ('feed', 'walk', 'play', 'sleep')


# Ensure that stat values are not less that 0 or more than 100
def min_max(stat_value):
    if stat_value <= 0:
        stat_value = 0
        return stat_value
    elif stat_value >= 100:
        stat_value = 100
        return stat_value
    else:
        return stat_value


# Display pet stats
def print_stats(pet_name, health, happy, rest, hunger):
    print("Now " + pet_name + "'s health is at " + str(health) + "%")
    print("Now " + pet_name + " is " + str(happy) + "% happy")
    print("Now " + pet_name + " is " + str(rest) + "% rested")
    print("Now " + pet_name + " is " + str(hunger) + "% full")


# Pet class
class Pet:
    """Pet class"""
    def __init__(self, pet_name, pet_owner):
        self.pet_name = pet_name
        self.pet_owner = pet_owner
        self.health = 100
        self.happy = 100
        self.rest = 100
        self.hunger = 50

    def feed(self, pet_name):
        """Feed pet"""
        print("What would you like to feed " + pet_name + "?")
        print("1. a treat\n2. a meal")
        feed_choice = int(input("selection: "))

        if feed_choice == 1:
            print("You give " + self.pet_name + " a treat.")

            self.health += 10
            self.health = min_max(self.health)
            self.happy += 20
            self.happy = min_max(self.happy)
            self.rest -= 10
            self.rest = min_max(self.rest)
            self.hunger += 10
            self.hunger = min_max(self.hunger)

        elif feed_choice == 2:
            print("You give " + self.pet_name + " a meal.")

            self.health += 20
            self.health = min_max(self.health)
            self.happy += 10
            self.happy = min_max(self.happy)
            self.rest -= 10
            self.rest = min_max(self.rest)
            self.hunger += 40
            self.hunger = min_max(self.hunger)

        else:
            print("That isn't a valid option.")

        print_stats(self.pet_name, self.health, self.happy, self.rest, self.hunger)

        # End of feed

    def walk(self, pet_name):
        """Walk pet"""
        print("How long of a walk do you want to take " + pet_name + " on?")
        print("1. short\n2. long")
        walk_choice = int(input("selection: "))

        if walk_choice == 1:
            print("You take " + self.pet_name + " for a short walk.")

            self.health += 10
            self.health = min_max(self.health)
            self.happy += 10
            self.happy = min_max(self.happy)
            self.rest -= 10
            self.rest = min_max(self.rest)
            self.hunger += 10
            self.hunger = min_max(self.hunger)

        elif walk_choice == 2:
            print("You take " + self.pet_name + " for a long walk.")

            self.health += 10
            self.health = min_max(self.health)
            self.happy += 20
            self.happy = min_max(self.happy)
            self.rest -= 20
            self.rest = min_max(self.rest)
            self.hunger -= 40
            self.hunger = min_max(self.hunger)

        else:
            print("That isn't a valid option.")

        print_stats(self.pet_name, self.health, self.happy, self.rest, self.hunger)

        # End of walk

    def play(self, pet_name):
        """Pet plays"""
        print("How much you want to play with " + pet_name + "?")
        # this is horrible but it's all I could think of for options
        print("1. a little\n2. a lot")
        play_choice = int(input("selection: "))

        if play_choice == 1:
            print("You play with " + self.pet_name + " a little.")

            self.health += 10
            self.health = min_max(self.health)
            self.happy += 10
            self.happy = min_max(self.happy)
            self.rest -= 10
            self.rest = min_max(self.rest)
            self.hunger -= 10
            self.hunger = min_max(self.hunger)

        elif play_choice == 2:
            print("You play with " + self.pet_name + " a lot.")

            self.health += 10
            self.health = min_max(self.health)
            self.happy += 40
            self.happy = min_max(self.happy)
            self.rest -= 40
            self.rest = min_max(self.rest)
            self.hunger -= 40
            self.hunger = min_max(self.hunger)

        else:
            print("That isn't a valid option.")

        print_stats(self.pet_name, self.health, self.happy, self.rest, self.hunger)

        # End of play

    def sleep(self, pet_name):
        """Pet sleeps"""
        print("How long is " + pet_name + " sleeping for?")
        print("1. a short nap\n2. all night")
        sleep_choice = int(input("selection: "))
        # this loop isn't working, goes straight to invalid option
        # thought it might be the leading self.pet_name but it doesn't seem to
        if sleep_choice == 1:
            print("test " + self.pet_name + " takes a short nap.")

            self.health += 10
            self.health = min_max(self.health)
            self.happy += 20
            self.happy = min_max(self.happy)
            self.rest += 20
            self.rest = min_max(self.rest)
            self.hunger -= 10
            self.hunger = min_max(self.hunger)

        elif sleep_choice == 2:
            print("test " + self.pet_name + " goes too sleep for the night")

            self.health += 40
            self.health = min_max(self.health)
            self.happy += 20
            self.happy = min_max(self.happy)
            self.rest += 40
            self.rest = min_max(self.rest)
            self.hunger -= 40
            self.hunger = min_max(self.hunger)

        else:
            print("That isn't a valid option.")

        print_stats(self.pet_name, self.health, self.happy, self.rest, self.hunger)

        # End of sleep

# End of pet class


# Species Classes
class Dog(Pet):
    """Dog class"""

    def __init__(self, pet_name, pet_owner):
        """Initialize attributes of the Pet class"""
        super().__init__(pet_name, pet_owner)

    # End of dog class


class Cat(Pet):
    """Cat class"""

    def __init__(self, pet_name, pet_owner):
        """Initialize attributes of the Pet class"""
        super().__init__(pet_name, pet_owner)

    # End of cat class


class Rabbit(Pet):
    """Rabbit class"""

    def __init__(self, pet_name, pet_owner):
        """Initialize attributes of the Pet class"""
        super().__init__(pet_name, pet_owner)

    # End of rabbit class


class Lizard(Pet):
    """Lizard class"""

    def __init__(self, pet_name, pet_owner):
        """Initialize attributes of the Pet class"""
        super().__init__(pet_name, pet_owner)

    # End of lizard class


class Bird(Pet):
    """Bird class"""

    def __init__(self, pet_name, pet_owner):
        """Initialize attributes of the Pet class"""
        super().__init__(pet_name, pet_owner)

    # End of bird class


class Fish(Pet):
    """Fish class"""

    def __init__(self, pet_name, pet_owner):
        """Initialize attributes of the Pet class"""
        super().__init__(pet_name, pet_owner)

    # End of fish class

# End of species classes


def main():

    # Get player name and pet type
    pet_owner = input("Welcome to pypets! \nWhat is your name? ").title()
    print("what kind of pet would you like?")
    type_menu_number = 1
    for types in pet_types:
        print(str(type_menu_number) + " " + types)
        type_menu_number += 1

    type_choice = int(input("selection: "))
    pet_type = pet_types[type_choice - 1]

    # Get pet name
    pet_name = input("What would you like to name your " + pet_type + "? ")

    if type_choice == 1:
        current_pet = Dog(pet_name, pet_owner)
    elif type_choice == 2:
        current_pet = Cat(pet_name, pet_owner)
    elif type_choice == 3:
        current_pet = Rabbit(pet_name, pet_owner)
    elif type_choice == 4:
        current_pet = Lizard(pet_name, pet_owner)
    elif type_choice == 5:
        current_pet = Bird(pet_name, pet_owner)
    elif type_choice == 6:
        current_pet = Fish(pet_name, pet_owner)
    else:
        print("Sorry, that isn't a valid option.")
        exit()

    print("\n\nOk, " + current_pet.pet_owner + " your new " + pet_type + "'s pet_name is " + current_pet.pet_name + "!")

    # Get and perform desired action

    print("\n\nWhat would you like to do with " + current_pet.pet_name + "?")

    action_menu_number = 1
    for action in petActions:
        print(str(action_menu_number) + " " + action)
        action_menu_number += 1

    action_choice = int(input("selection: "))
    action_type = petActions[action_choice - 1]

    if action_type == "feed":
        current_pet.feed(current_pet.pet_name)
    elif action_type == "walk":
        current_pet.walk(current_pet.pet_name)
    elif action_type == "play":
        current_pet.play(current_pet.pet_name)
    else:
        print("Sorry, that isn't a valid option.")
        exit()


if __name__ == '__main__':
    main()
