"""
The main zoo UI
"""

from d1_project_pitch.src.zoo_animal_management import add_new_animal, display_species_list
from d1_project_pitch.src.zoo_health_tracking import record_health_check, calculate_health_status
from d1_project_pitch.src.zoo_feeding import calculate_feeding_schedule, record_feeding
from d1_project_pitch.src.zoo_breeding import check_breeding_eligibility
from d1_project_pitch.src.zoo_file_management import load_animals_from_file, save_animals_to_file
from d1_project_pitch.src.zoo_habitat_assignment import get_animal_habitat, assign_animal_to_habitat, generate_habitat_report
from d1_project_pitch.src.zoo_species_data import ZOO_HABITATS

def display_main_menu():
    """
    Display the main menu
    """
    print("\n=== Zoo Habitat and Wellness Management System ===") 
    print("1. Add New Animal")
    print("2. Assign to Habitat") 
    print("3. Record Health Check")
    print("4. Process Feeding")
    print("5. Check Breeding Eligibility")
    print("6. View Habitat Report")
    print("7. Quit")
    print("==================================================")

def get_menu_choice():
    """
    Get and validate menu choice from user
    """
    while True:
        try:
            choice = int(input("Enter your choice (1-7): "))
            
            if 1 <= choice <= 7: 
                return choice 
            else: 
                print("Invalid choice. Please enter a number between 1 and 7.")

        except ValueError: 
            print("Invalid input. Please enter a number between 1 and 7.")

def list_animals(animals): 
    """ 
    Display list of animals with basic info 
    """ 
    if not animals: 
        print("No animals in the system.") 
        return 
    
    print("\nAnimals in system:") 
    
    for i, animal in enumerate(animals, 1): 
        print(f"{i}. {animal['name']} ({animal['species']}) - ID: {animal['animal_id']}")

def add_new_animal_to_system(animals):
    """
    Adding a new animal to the system
    """

    display_species_list()

    print("\n--- Add New Animal ---")

    #data
    animal_id = input("Enter animal ID: ").strip() 
    name = input("Enter animal name: ").strip()
    species = input("Enter species: ") 
    
    try: 
        age = int(input("Enter age (years): "))
    except ValueError: 
        print("Invalid age. Using default age 0.")
        age = 0
    
    new_animal = add_new_animal(animal_id, name, species, age, animals)

    if new_animal: 
        animals.append(new_animal)
        print(f"Successfully added {name} the {species} to the system!") 
        return animals
    else: 
        print("Failed to add animal. It may have a duplicate ID or invalid data.") 
        return animals
    
def find_animal_by_id(animal_id, animals): 
    """ 
    Find an animal by ID in the animals list
    """ 
    for animal in animals: 
        if animal.get('animal_id') == animal_id: 
            return animal 
    return None

def record_health_check_in_system(animals):
    """
    Recording a health check for the animal
    """
    print("\n--- Record Health Check ---")

    if not animals: 
        print("No animals in the system. Please add animals first.") 
        return animals
    
    list_animals(animals) 
    animal_id = input("\nEnter animal ID to record health check: ").strip()

    animal = find_animal_by_id(animal_id, animals) 
    
    if not animal: 
        print(f"Animal with ID {animal_id} not found.") 
        return animals 
    
    print(f"\nRecording health check for {animal['name']} the {animal['species']}")

    health_data = {} 
    
    weight_input = input("Enter weight in kg (press Enter to skip): ").strip() 
    if weight_input: 
        try: 
            health_data['weight_kg'] = float(weight_input) 
        except ValueError: 
            print("Invalid weight. Skipping weight recording.") 
        
    temp_input = input("Enter temperature in °C (press Enter to skip): ").strip() 
    if temp_input: 
        try: 
            health_data['temperature_c'] = float(temp_input) 
        except ValueError: 
            print("Invalid temperature. Skipping temperature recording.") 
    
    hr_input = input("Enter heart rate (press Enter to skip): ").strip() 
    if hr_input: 
        try: 
            health_data['heart_rate'] = int(hr_input) 
        except ValueError: 
            print("Invalid heart rate. Skipping heart rate recording.") 
    
    health_data['vaccination_status'] = input("Enter vaccination status (current/overdue/none): ").strip() 
    health_data['vet_notes'] = input("Enter vet notes: ").strip() 
    
    updated_animal = record_health_check(animal, health_data) 
    
    #update animal in list
    for i, a in enumerate(animals): 
        if a['animal_id'] == animal_id: 
            animals[i] = updated_animal 
            break 
    
    health_status, details = calculate_health_status(updated_animal) 
    
    print(f"Health check recorded. Current status: {health_status}") 
    print(f"   Details: {details}") 
    
    return animals

def process_feeding_in_system(animals):
    """
    Process animal feeding
    """
    print("\n--- Process Feeding ---") 
    
    if not animals: 
        print("No animals in the system. Please add animals first.") 
        return animals

    print("\nFeeding Schedule for Today:") 
    total_meat = 0 
    total_vegetation = 0

    for animal in animals: 
        schedule = calculate_feeding_schedule(animal) 
        print(f"\n{animal['name']} ({animal['species']}):") 
        print(f"  Food: {schedule['food_type']} - {schedule['daily_amount_kg']}kg") 
        print(f"  Times: {', '.join(schedule['feeding_times'])}")

        if schedule['food_type'] == 'meat': 
            total_meat += schedule['daily_amount_kg'] 
        elif schedule['food_type'] == 'vegetation': 
            total_vegetation += schedule['daily_amount_kg']

    print(f"\nTotal Food Requirements:") 
    print(f"  Meat: {total_meat:.2f}kg") 
    print(f"  Vegetation: {total_vegetation:.2f}kg")

    record_feeding_in_system = input("\nRecord a feeding? (y/n): ").strip().lower() 
    
    if record_feeding_in_system == 'y': 
        list_animals(animals) 
        animal_id = input("Enter animal ID to record feeding: ").strip()

        animal = find_animal_by_id(animal_id, animals)

        if animal: 
            feeding_details = { 
                'time': input("Enter feeding time: ").strip(), 
                'amount_kg': float(input("Enter amount fed (kg): ").strip()), 
                'food_type': input("Enter food type: ").strip(), 
                'keeper': input("Enter keeper name: ").strip() 
            }
            
            updated_animal = record_feeding(animal, feeding_details)

            for i, a in enumerate(animals): 
                if a['animal_id'] == animal_id: 
                    animals[i] = updated_animal 
                    break 
                
            
            print("Feeding recorded successfully!") 
            
    return animals

def check_breeding_eligibility_in_system(animals):
    """
    Checking the breeding eligibility of animals
    """
    print("\n--- Check Breeding Eligibility ---")

    if not animals: 
        print("No animals in the system. Please add animals first.") 
        return animals 
    
    list_animals(animals)

    print("\nIndividual Animal Eligibility:") 
    eligible_animals = []

    for animal in animals:
        is_eligible, reason = check_breeding_eligibility(animal) 
        status = "Eligible" if is_eligible else "Not Eligible" 

        print(f"{animal['name']} ({animal['species']}): {status}") 
        print(f"  Reason: {reason}")

        if is_eligible: 
            eligible_animals.append(animal)
        
    return animals


def assign_to_habitat_in_system(animals, habitats):
    """
    Assign an animal to a habitat
    """
    print("\n--- Assign to Habitat ---")

    if not animals: 
        print("No animals in the system. Please add animals first.")
        return animals, habitats

    print("\nAvailable Habitats:") 
    for habitat_name, habitat in habitats.items(): 
        current_count = len(habitat["current_animals"]) 
        available_space = habitat["capacity"] - current_count 
        print(f"  {habitat_name}: {habitat['name']} ({current_count}/{habitat['capacity']} animals)")
    

    #show unassigned animals
    unassigned_animals = [] 
    for animal in animals:
        current_habitat = get_animal_habitat(animal["animal_id"], habitats) 
        
        if not current_habitat: 
            unassigned_animals.append(animal)

    print("\nUnassigned Animals:") 
    for animal in unassigned_animals: 
        print(f"  {animal['animal_id']}: {animal['name']} the {animal['species']}")

    #validate animal id
    while True: 
        animal_id = input("\nEnter animal ID to assign: ").strip() 

        animal = next((a for a in unassigned_animals if a["animal_id"] == animal_id), None) #match unassigned_animals to inputted id
        
        if animal: 
            break 
        print("Invalid animal ID. Please try again.")


    
    #find compatible habitat
    compatible_habitats = [key for key, h in habitats.items() if animal["species"] in h["compatible_species"]] 
    
    print(f"\nCompatible habitats for {animal['name']} ({animal['species']}):") 
    
    for key in compatible_habitats: h = habitats[key] 
    print(f"  {key}: {h['name']} ({len(h['current_animals'])}/{h['capacity']} animals)")
    

    #validate habitat
    while True: 
        habitat_name = input("Enter habitat name: ").strip().lower() 
        
        if habitat_name in compatible_habitats: 
            break 
        print("Invalid habitat for this animal. Please choose a compatible habitat.")


    #find animal
    animal_to_assign = None 
    for animal in unassigned_animals: 
        if animal["animal_id"] == animal_id: 
            animal_to_assign = animal 
            break
    
    if not animal_to_assign:
        print(f"Animal with ID {animal_id} not found or already assigned.") 
        return animals, habitats
    

    success, message = assign_animal_to_habitat(animal_to_assign, habitat_name, habitats, animals) 
    
    if success: 
        print(f"{message}")
    else: 
        print(f"{message}") 
    
    
    return animals, habitats


def view_habitat_report_in_system(animals, habitats):
    """
    Function for viewing habitat reports
    """
    print("\n--- Habitat Report ---")

    report = generate_habitat_report(habitats, animals)

    print(f"\nZoo Habitat Report") 
    print(f"Total Habitats: {report['total_habitats']}") 
    print(f"Total Animals Assigned: {report['total_animals_assigned']}")

    for habitat_name, habitat_info in report["habitats"].items():
        print(f"\n{habitat_info['name']} ({habitat_name})") 
        print(f"  Animals: {habitat_info['current_count']}/{habitat_info['capacity']}") 
        print(f"  Available Space: {habitat_info['available_space']}")
    
        if habitat_info["animals"]: 
            print("  Inhabitants:") 
            
            for animal in habitat_info["animals"]: 
                print(f"    - {animal['name']} ({animal['species']}) - ID: {animal['id']}") 
            else: 
                print("  No animals assigned")
    
    return animals,habitats





def run_zoo_program():
    """
    Function responsible for running the main zoo program
    """
    print("Welcome to the Zoo Habitat and Wellness Management System!")

    animals = load_animals_from_file("zoo_data.json") 
    print(f"Loaded {len(animals)} animals from storage.")

    habitats = ZOO_HABITATS

    while True: 
        display_main_menu() 
        choice = get_menu_choice()

        if choice == 1: #add new animal
            animals = add_new_animal_to_system(animals)
        elif choice == 2: #habitats
            animals, habitats = assign_to_habitat_in_system(animals, habitats)
        elif choice == 3: #record health check
            animals = record_health_check_in_system(animals)
        elif choice == 4: #process feeding
            animals = process_feeding_in_system(animals)
        elif choice == 5: #check breeding eligibility
            animals = check_breeding_eligibility_in_system(animals)
        elif choice == 6: 
            animals, habitats = view_habitat_report_in_system(animals, habitats)
        elif choice == 7:   #QUIT
            if save_animals_to_file(animals, "zoo_data.json"):
                print("Animal data saved successfully.")
            else:
                print("Warning: Could not save animal data.")
            print("Thank you for using the Zoo Management System. We hope to see you again!")
            break
    
    return animals

if __name__ == "__main__": 
    run_zoo_program()