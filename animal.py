# Assignment: Animal
# Create an Animal class and give it the below attributes and methods. Extend the Animal class to two child classes, Dog and Dragon.

class Animal(object):
	def __init__(self,name,health):
		self.name=name
		self.health=health
	def walk(self):
		self.health-=1
		return self
	def run(self):
		self.health-=5
		return self
	def display_health(self):
		print self.health

animal1=Animal("Jade",500)

#to test to see if methods above work
# animal1.run().run().walk().walk().run().display_health()

class Dog(Animal):
	def __init__(self):
		self.health=150
	def pet(self):
		self.health+=5
		return self

dog1=Dog()

#test to see if methods were inherited and new methods were applied 
dog1.walk().walk().walk().run().run().pet().pet().display_health()
#it works!

class Dragon(Animal):
	def __init__(self):
		self.health=170
	def display_roar(self):
		display_health()
		print "I am a Dragon"

animal2=Animal("Mike",610)


#just making sure my dog can't fly.. maybe one of these days
dog1.fly()