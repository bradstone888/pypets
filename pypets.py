## Set available pet types and actions
petTypes = ('dog', 'cat', 'rabbit', 'lizard', 'bird', 'fish')
petActions = ('feed', 'walk', 'play', 'sleep', 'nap') 

## Pet class
class Pet():
	"""Pet class"""
	def __init__(self, petName, petOwner):
		self.petName = petName
		self.petOwner = petOwner
		self.heath = 100
		self.happy = 100
		self.rest = 100
		self.hunger = 0
	
	def get_health(self):
		return self.health

	def get_happy(self):
		return self.happy
	
	def get_rest(self):
		return self.rest

	def get_hunger(self):
		return self.hunger

	def update_health(self, health):
		self.health = health

	def update_happy(self, happy):
		self.happy = happy

	def update_rest(self, rest):
		self.rest = rest

	def update_hunger(self, hunger):
		self.hunger = hunger

	def feed(self):
		"""Pet eats"""
		print(self.petName + " eats what you gave them.")
	
	def walk(self):
		"""Walk pet"""
		print("You take " + self.petName + " for a walk.")

	def play(self):
		"""Pet plays"""
		print("You play with" + self.petName + ".")

	def sleep(self):
		"""Pet sleeps"""
		print(self.petName + " sleeps.")

	def nap(self):
		"""Pet naps"""
		print(self.petName + " takes a nap.")

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
		"""Initialize attibutes of the Pet class"""
		super().__init__(petName, petOwner)

class Rabbit(Pet):
	"""Rabbit class"""

	def __init__(self, petName, petOwner):
		"""Initialize attibutes of the Pet class"""
		super().__init__(petName, petOwner)

class Lizard(Pet):
	"""Lizard class"""

	def __init__(self, petName, petOwner):
		"""Initialize attibutes of the Pet class"""
		super().__init__(petName, petOwner)

class Bird(Pet):
	"""Bird class"""

	def __init__(self, petName, petOwner):
		"""Initialize attibutes of the Pet class"""
		super().__init__(petName, petOwner)

class Fish(Pet):
	"""Fish class"""

	def __init__(self, petName, petOwner):
		"""Initialize attibutes of the Pet class"""
		super().__init__(petName, petOwner)

##End of species classes

## Get player petName
petOwner = input("Welcome to pypets! \nWhat is your petName? ").title()
print("what kind of pet would you like?")
typeMenuNumber = 1
for types in petTypes:
	print(str(typeMenuNumber) + " " + types)
	typeMenuNumber += 1

typeChoice = int(input("number: "))
petType = petTypes[typeChoice-1]

petName = input("What would you like to petName your " + petType +"?\n")

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
	print("Sorry, that isn't a valid option")
	exit()

print("\n\nOk, " + currentPet.petOwner + " your new " + petType + "'s petName is " + currentPet.petName + "!")

# Get and peform desired action

print("\n\nWhat would you like to do with " + currentPet.petName + "?")

actionMenuNumber = 1
for action in petActions:
	print(str(actionMenuNumber) + " " + action)
	actionMenuNumber += 1

actionChoice = int(input("number: "))
actionType = petActions[actionChoice-1]
getattr(currentPet, actionType)()

