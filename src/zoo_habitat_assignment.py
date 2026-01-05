"""
File responsible for the habitat assignment of animals
"""

from d1_project_pitch.src.zoo_business_logic import check_habitat_compatibility

def assign_animal_to_habitat(animal, habitat_name, habitats, all_animals=None):
    """
    Assign an animal to a habitat after checking compatibility
    """
    if habitat_name not in habitats: 
        return False, f"Habitat '{habitat_name}' does not exist."
    
    habitat = habitats[habitat_name] 
    
    if len(habitat["current_animals"]) >= habitat["capacity"]: 
        return False, f"Habitat '{habitat_name}' is at full capacity."
    
    if all_animals: 
        for existing_animal_id in habitat["current_animals"]: 
            existing_animal = find_animal_by_id(existing_animal_id, all_animals) 

            if existing_animal: 
                compatible, reason = check_habitat_compatibility(animal, existing_animal) 
                if not compatible: 
                    return False, f"Not compatible with {existing_animal['name']}: {reason}"

    habitat["current_animals"].append(animal["animal_id"]) 
    return True, f"Successfully assigned {animal['name']} to habitat"

def find_animal_by_id(animal_id, animals):
    """ 
    Helper function to find animal by ID 
    """ 
    for animal in animals: 
        if animal.get('animal_id') == animal_id: 
            return animal 
    return None
    
def remove_animal_from_habitat(animal_id, habitat_name, habitats):
    """
    Remove an animal from a habitat
    """
    if habitat_name not in habitats: 
        return False, f"Habitat '{habitat_name}' does not exist."

    habitat = habitats[habitat_name]

    if animal_id in habitat["current_animals"]: 
        habitat["current_animals"].remove(animal_id) 
        return True, f"Removed animal {animal_id} from {habitat['name']}" 
    else: 
        return False, f"Animal {animal_id} not found in {habitat['name']}"


def get_animal_habitat(animal_id, habitats):
    """
    Find which habitat an animal is assigned to
    """
    for habitat_name, habitat in habitats.items(): 
        if animal_id in habitat["current_animals"]: 
            return habitat_name 
    
    return None

def generate_habitat_report(habitats, animals):
    """
    Generate report for the habitat and animals
    """
    report = { 
        "total_habitats": len(habitats), 
        "total_animals_assigned": 0,
         "habitats": {} 
    }

    #loop for habitat
    for habitat_name, habitat in habitats.items(): 
        habitat_info = { 
            "name": habitat["name"], 
            "capacity": habitat["capacity"], 
            "current_count": len(habitat["current_animals"]), 
            "available_space": habitat["capacity"] - len(habitat["current_animals"]), 
            "animals": [] 
        }
    
        #loop for animals in this habitat
        for animal_id in habitat["current_animals"]: 
            animal = find_animal_by_id(animal_id, animals) 
            
            if animal: 
                habitat_info["animals"].append({ 
                    "id": animal_id, 
                    "name": animal.get("name", "Unknown"),
                    "species": animal.get("species", "Unknown") 
            })
                
        report["habitats"][habitat_name] = habitat_info 
        report["total_animals_assigned"] += len(habitat["current_animals"])
    
    return report


    