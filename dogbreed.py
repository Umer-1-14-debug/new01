class Dog:
    species = "I dont know"

    def __init__(self, breed, age):
        self.breed = breed
        self.age = age
    def display(self):
        print("Species:", Dog.species)
        print("Breed:", self.breed)
        print("Age:", self.age)
dog1 = Dog("German Shepherd", 3)
dog2 = Dog("Bulldog", 5)
dog1.display()
dog2.display()
