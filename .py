class Dog:
    species = "Canis familiaris"
    def __init__(self, breed):
        self.breed = breed

    def display_details(self, name):
        print(f"Dog Name: {name}")
        print(f"Species:  {Dog.species}")
        print(f"Breed:    {self.breed}")
        print("-" * 25)
dog_one = Dog("Golden Retriever")
dog_two = Dog("German Shepherd")
dog_one.display_details("Buddy")
dog_two.display_details("Max")