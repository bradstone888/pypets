#!/usr/bin/env python3

# Set available pet types and actions
petTypes = ('dog', 'cat', 'rabbit', 'lizard', 'bird', 'fish')
petActions = ('feed', 'walk', 'play', 'sleep')


def minmax(statvalue):
    if statvalue <= 0:
        statvalue = 0
        return statvalue
    elif statvalue >= 100:
        statvalue = 100
        return statvalue
    else:
        return statvalue

def printstats(petName, health, happy, rest, hunger):
    print("Now " + petName + "'s health is at " + str(health) + "%")
    print("Now " + petName + " is " + str(happy) + "% happy")
    print("Now " + petName + " is " + str(hunger) + "% rested")
    print("Now " + petName + " is " + str(hunger) + "% full")

## Pet class
class Pet():
    """Pet class"""

    def __init__(self, petName, petOwner):
        self.petName = petName
        self.petOwner = petOwner
        self.health = 100
        self.happy = 100
        self.rest = 100
        self.hunger = 50

    def feed(self, petName):
        """Feed pet"""
        print("What would you like to feed " + petName + "?")
        print("1. a treat\n2. a meal")
        feedChoice = int(input("selection: "))

        if feedChoice == 1:
            print("You give " + self.petName + " a treat.")

            self.health += 10
            self.health = minmax(self.health)
            self.happy += 20
            self.happy = minmax(self.happy)
            self.rest -= 10
            self.rest = minmax(self.rest)
            self.hunger += 10
            self.hunger = minmax(self.hunger)

        elif feedChoice == 2:
            print("You give " + self.petName + " a meal.")

            self.health += 20
            self.health = minmax(self.health)
            self.happy += 10
            self.happy = minmax(self.happy)
            self.rest -= 10
            self.rest = minmax(self.rest)
            self.hunger += 40
            self.hunger = minmax(self.hunger)

        else:
            print("That isn't a valid option.")

        printstats(self.petName, self.health, self.happy, self.rest, self.hunger)

        ## end of feed

    def walk(self, petName):
        """Walk pet"""
        print("How long of a walk do you want to take " + petName + " on?")
        print("1. short\n2. long")
        walkChoice = int(input("selection: "))

        if walkChoice == 1:
            print("You take " + self.petName + " for a short walk.")

            self.health += 10
            self.health = minmax(self.health)
            self.happy += 10
            self.happy = minmax(self.happy)
            self.rest -= 10
            self.rest = minmax(self.rest)
            self.hunger += 10
            self.hunger = minmax(self.hunger)

        elif walkChoice == 2:
            print("You take " + self.petName + " for a long walk.")

            self.health += 10
            self.health = minmax(self.health)
            self.happy += 20
            self.happy = minmax(self.happy)
            self.rest -= 20
            self.rest = minmax(self.rest)
            self.hunger -= 40
            self.hunger = minmax(self.hunger)

        else:
            print("That isn't a valid option.")

        printstats(self.petName, self.health, self.happy, self.rest, self.hunger)

        ## end of walk

    def play(self, petName):
        """Pet plays"""
        print("How much you want to play with " + petName + "?")
        # this is horrible but it's all I could think of for options
        print("1. a little\n2. a lot")
        playChoice = int(input("selection: "))

        if playChoice == 1:
            print("You play with " + self.petName + " a little.")

            self.health += 10
            self.health = minmax(self.health)
            self.happy += 10
            self.happy = minmax(self.happy)
            self.rest -= 10
            self.rest = minmax(self.rest)
            self.hunger -= 10
            self.hunger = minmax(self.hunger)

        elif playChoice == 2:
            print("You play with " + self.petName + " a lot.")

            self.health += 10
            self.health = minmax(self.health)
            self.happy += 40
            self.happy = minmax(self.happy)
            self.rest -= 40
            self.rest = minmax(self.rest)
            self.hunger -= 40
            self.hunger = minmax(self.hunger)

        else:
            print("That isn't a valid option.")

        printstats(self.petName, self.health, self.happy, self.rest, self.hunger)

        ## end of play

    def sleep(self, petName):
        """Pet sleeps"""
        print("How long is " + self.petName + " sleeping for?")
        print("1. a short nap\n2. all night")
        sleepChoice = int(input("selection: "))

        # this loop isn't working, goes straight to invalid option
        # thought it might be the leading self.petName but it doesn't seem to
        if sleepChoice == 1:
            print(self.petName + " takes a short nap.")

            self.health += 10
            self.health = minmax(self.health)
            self.happy += 20
            self.happy = minmax(self.happy)
            self.rest += 20
            self.rest = minmax(self.rest)
            self.hunger -= 10
            self.hunger = minmax(self.hunger)

        elif sleepChoice == 2:
            print(self.petName + " goes too sleep for the night")

            self.health += 40
            self.health = minmax(self.health)
            self.happy += 20
            self.happy = minmax(self.happy)
            self.rest += 40
            self.rest = minmax(self.rest)
            self.hunger -= 40
            self.hunger = minmax(self.hunger)

        else:
            print("That isn't a valid option.")

        printstats(self.petName, self.health, self.happy, self.rest, self.hunger)

        ## end of sleep

## End of pet class

## Species Classes
class Dog(Pet):
    """Dog class"""

    def __init__(self, petName, petOwner):
        """Initialize attributes of the Pet class"""
        super().__init__(petName, petOwner)


class Cat(Pet):
    """Cat class"""

    def __init__(self, petName, petOwner):
        """Initialize attributes of the Pet class"""
        super().__init__(petName, petOwner)


class Rabbit(Pet):
    """Rabbit class"""

    def __init__(self, petName, petOwner):
        """Initialize attributes of the Pet class"""
        super().__init__(petName, petOwner)


class Lizard(Pet):
    """Lizard class"""

    def __init__(self, petName, petOwner):
        """Initialize attributes of the Pet class"""
        super().__init__(petName, petOwner)


class Bird(Pet):
    """Bird class"""

    def __init__(self, petName, petOwner):
        """Initialize attributes of the Pet class"""
        super().__init__(petName, petOwner)


class Fish(Pet):
    """Fish class"""

    def __init__(self, petName, petOwner):
        """Initialize attributes of the Pet class"""
        super().__init__(petName, petOwner)
##End of species classes

def main():
    ## Get player petName
    petOwner = input("Welcome to pypets! \nWhat is your name? ").title()
    print("what kind of pet would you like?")
    typeMenuNumber = 1
    for types in petTypes:
        print(str(typeMenuNumber) + " " + types)
        typeMenuNumber += 1

    typeChoice = int(input("selection: "))
    petType = petTypes[typeChoice - 1]

    petName = input("What would you like to name your " + petType + "? ")

    if typeChoice == 1:
        currentPet = Dog(petName, petOwner)
    elif typeChoice == 2:
        currentPet = Cat(petName, petOwner)
    elif typeChoice == 3:
        currentPet = Rabbit(petName, petOwner)
    elif typeChoice == 4:
        currentPet = Lizard(petName, petOwner)
    elif typeChoice == 5:
        currentPet = Bird(petName, petOwner)
    elif typeChoice == 6:
        currentPet = Fish(petName, petOwner)
    else:
        print("Sorry, that isn't a valid option.")
        exit()

    print("\n\nOk, " + currentPet.petOwner + " your new " + petType + "'s petName is " + currentPet.petName + "!")

    # Get and perform desired action

    print("\n\nWhat would you like to do with " + currentPet.petName + "?")

    actionMenuNumber = 1
    for action in petActions:
        print(str(actionMenuNumber) + " " + action)
        actionMenuNumber += 1

    actionChoice = int(input("selection: "))
    actionType = petActions[actionChoice - 1]

    if actionType == "feed":
        currentPet.feed(currentPet.petName)
    elif actionType == "walk":
        currentPet.walk(currentPet.petName)
    elif actionType == "play":
        currentPet.play(currentPet.petName)
    else:
        print("Sorry, that isn't a valid option.")
        exit()

if __name__ == '__main__':
  main()
