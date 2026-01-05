"""
File that is responsbile for the animal management system of the zoo
"""

from d1_project_pitch.src.zoo_species_data import get_species_data, SPECIES_HEALTH_BASELINES

def validate_animal_data(animal_id, name, species, age):
    """
    Validate animal data
    """
    if not animal_id or not animal_id.strip(): 
        return False, "Animal ID cannot be empty" 
    if not name or not name.strip(): 
        return False, "Animal name cannot be empty" 
    if not species or not species.strip(): 
        return False, "Species cannot be empty" 
    if age == 0: 
        return False, "Age cannot be zero" 

    if not get_species_data(species): 
        return False, f"Unknown species: '{species}'"
    
    if age < 0: 
        return False, "Age cannot be negative"
    
    return True, "Valid"

def is_duplicate_animal_id(animal_id, animals_list):
    """
    Check if an animal ID already exists in the system
    """
    for animal in animals_list: 
        if animal["animal_id"] == animal_id: 
            return True 
    return False

def add_new_animal(animal_id, name, species, age=0, existing_animals=None):
    """
    Adds a new animal to the system
    """

    is_valid, error_message = validate_animal_data(animal_id, name, species, age) 
    
    if not is_valid: 
        print(f"Validation error: {error_message}") 
        return None
    
    if existing_animals is not None and is_duplicate_animal_id(animal_id, existing_animals): 
        print(f"Duplicate animal ID: {animal_id}") 
        return None
    
    species_data = get_species_data(species)

    animal = { 
        "animal_id": animal_id, 
        "name": name, 
        "species": species, 
        "age": age, 
        "health_records": [],
        "current_medications": [], 
        "feeding_history": [] 
    }

    #update the values for known species based on the info given
    if species_data: 
        animal.update({ 
            "diet": species_data["diet"], 
            "habitat_type": species_data["habitat_type"], 
            "temperament": species_data["temperament"], 
            "social_needs": species_data["social_needs"] 
        }) 
    else: 
        animal.update({ 
            "diet": "unknown", 
            "habitat_type": "unknown", 
            "temperament": "unknown", 
            "social_needs": "unknown" 
        })

    return animal

def display_species_list():
    """
    Display available species to user
    """
    species_keys = list(SPECIES_HEALTH_BASELINES.keys()) 
    
    print("\n=== Available Species ===") 
    
    print(f"{'No.':<4} {'Species':<15} {'ID':<14}") 
    print("-" * 60) 
    
    for i, sp in enumerate(species_keys, start=1): 
        d = SPECIES_HEALTH_BASELINES[sp] 
        
        print(f"{i:<4} {sp:<15} {d.get('id','-'):<14}") 
        
    print("-" * 60)