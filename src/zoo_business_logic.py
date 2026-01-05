
def is_predator(animal):
    """
    
    Check if animal is a predator based on diet

    """
    return animal.get("diet") == "carnivore"

def have_compatible_diets(animal1, animal2):
    """
    
    Check if two animals that compatible diets
    
    """
    diet1 = animal1.get("diet")
    diet2 = animal2.get("diet")

    if diet1 == diet2:
        return True
    
    if ("carnivore" in [diet1, diet2] and "herbivore" in [diet1, diet2]):
        return False
    
def have_compatible_habitats(animal1, animal2):
    """

    Check if two animals require the same habitat type

    """
    habitat1 = animal1.get("habitat_type")
    habitat2 = animal2.get("habitat_type")

    return habitat1 == habitat2

def check_habitat_compatibility(animal1, animal2):
    """
    
    Main habitat compatibility check combining diet + habitat rules
    
    """

    #check diets
    if not have_compatible_diets(animal1, animal2):
        print("Animals have incompatible diets.")
        return False
    
    #check habitats
    if not have_compatible_habitats(animal1, animal2):
        print("Animals have incompatible habitats.")
        return False
    
    #check temperaments
    if not have_compatible_temperaments(animal1, animal2):
        print("Animals have incompatible temperaments.")
        return False
    
    #check social needs
    if not have_compatible_social_needs(animal1, animal2):
        print("Animals have incompatible social needs.")
        return False
    
    print("Animals are compatible!")
    return True
    
def have_compatible_temperaments(animal1, animal2):
    """
    
    Check if two animals have compatible temperaments

    """
    temp1 = animal1.get("temperament")
    temp2 = animal2.get("temperament")

    return temp1 == temp2

def have_compatible_social_needs(animal1, animal2):
    """
    
    Check if two animals have social needs that are compatible

    """
    social1 = animal1.get("social_needs") 
    social2 = animal2.get("social_needs")

    solitary_animals = ["solitary", "territorial"]
    social_animals = ["group", "pack", "herd", "pride"]

    if (social1 in solitary_animals and social2 in social_animals) or \
    (social2 in solitary_animals and social1 in social_animals):
        return False
    
    return True
