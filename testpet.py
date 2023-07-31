from pet import Pet

# Program to create a Pet object and prompt the user to enter pet details
if __name__ == "__main__":
    my_pet = Pet()

    name = input("Enter the name of your pet: ")
    my_pet.set_name(name)

    animal_type = input("Enter the type of your pet (e.g., Dog, Cat, Bird): ")
    my_pet.set_animal_type(animal_type)

    age = input("Enter the age of your pet: ")
    my_pet.set_age(age)

    print("\nPet Details:")
    print("Name:", my_pet.get_name())
    print("Type:", my_pet.get_animal_type())
    print("Age:", my_pet.get_age())
