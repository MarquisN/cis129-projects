# Create a class named Pet to store information about pets
class Pet:
    # Set up the initial properties of the Pet when we make a new one
    def __init__(self, name='', type='', age=0):
        self.name = name  # Name of the pet
        self.type = type  # What kind of animal (like Dog, Cat)
        self.age = age    # How old the pet is

    # A function to change the pet's name
    def set_name(self, name):
        self.name = name

    # A function to change the type of the pet
    def set_type(self, type):
        self.type = type

    # A function to change how old the pet is
    def set_age(self, age):
        self.age = age

    # A function to get the pet's name when we need it
    def get_name(self):
        return self.name

    # A function to get what type of animal the pet is
    def get_type(self):
        return self.type

    # A function to find out how old the pet is
    def get_age(self):
        return self.age

# This is where we put the code that runs when we start the program
def main():
    # Ask the user to type in a name and save it
    input_name = input("Enter a pet name: ")
    # Ask the user to type in what type of pet it is and save it
    input_type = input("Enter a pet type: ")
    # Ask the user to type in the pet's age, make sure it's a number, and save it
    input_age = int(input("Enter a pet age: "))

    # Make a new pet object from the Pet class
    animal = Pet()

    # Set the details of the pet using what the user typed in
    animal.set_name(input_name)
    animal.set_type(input_type)
    animal.set_age(input_age)

    # Print out the details about the pet
    print(f"The pet name is {animal.get_name()}")
    print(f"The pet type is {animal.get_type()}")
    print(f"The pet age is {animal.get_age()}")

# This line makes sure the code in main() runs only if this file is the main program
if __name__ == "__main__":
    main()
