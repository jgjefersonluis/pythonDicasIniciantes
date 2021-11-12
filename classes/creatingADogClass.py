class Dog:
    """ Represent a dog. """

    def __init__(self, name):
        """ Initialize dog object. """
        self.name=name

    def sit(self):
        """ Simulate sitting. """
        print(f"{self.name} is sitting. ")

my_dog = Dog('Dante')

print(f"{my_dog.name} is a great dog!")
my_dog.sit()


