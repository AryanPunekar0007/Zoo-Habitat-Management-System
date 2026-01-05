import unittest
from d1_project_pitch.src.zoo_animal_management import add_new_animal, is_duplicate_animal_id
from d1_project_pitch.src.zoo_health_tracking import calculate_health_status
from d1_project_pitch.src.zoo_feeding import calculate_feeding_schedule
from d1_project_pitch.src.zoo_breeding import check_breeding_eligibility
from d1_project_pitch.src.zoo_business_logic import have_compatible_diets

class TestAnimalManagement(unittest.TestCase):
    """
    Test suite for animal creation
    """

    def test_create_basic_animal(self):
        """
        Statement testing: Basic test for creating a new animal
        """
        animal_id = "LION001" 
        name = "Leo" 
        species = "Lion" 
        age = 5

        animal = add_new_animal(animal_id, name, species, age)

        self.assertIsInstance(animal, dict) 
        self.assertEqual(animal["animal_id"], animal_id) 
        self.assertEqual(animal["name"], name) 
        self.assertEqual(animal["species"], species) 
        self.assertEqual(animal["age"], age)
    
    def test_animal_creation_with_species_defaults(self):
        """
        Integration testing: Test that animal creation uses species data for defaults
        """
        animal_id = "LION002" 
        name = "Luna" 
        species = "Lion"

        animal = add_new_animal(animal_id, name, species)

        self.assertEqual(animal["diet"], "carnivore") 
        self.assertEqual(animal["habitat_type"], "savannah") 
        self.assertEqual(animal["temperament"], "aggressive") 
        self.assertIn("health_records", animal) 
        self.assertIn("current_medications", animal)

    def test_duplicate_animal_id_prevention(self):
        """
        Branch testing: Test that duplicate animal IDs are prevented
        """
        existing_animals = [] 
        
        animal1 = add_new_animal("LION001", "Leo", "Lion") 
        existing_animals.append(animal1) 
        
        animal2 = add_new_animal("LION001", "Luna", "Lion")
        is_duplicate = is_duplicate_animal_id("LION001", existing_animals) 
        
        self.assertTrue(is_duplicate)

    def test_animal_integration_with_other_systems(self):
        """
        Integration testing: Test that new animals work with all systems
        """
        animal = add_new_animal("TEST001", "Testy", "Lion", 4)

        #for health status
        health_status, details = calculate_health_status(animal) 
        self.assertEqual(health_status, "unknown")  # No health records yet

        #feeding
        feeding_schedule = calculate_feeding_schedule(animal) 
        self.assertEqual(feeding_schedule["food_type"], "meat") 

        #breeding
        is_eligible, reason = check_breeding_eligibility(animal) 
        self.assertFalse(is_eligible)  # Lion age 4 shouldnt be eligible

        #habitat diets
        another_animal = add_new_animal("TEST002", "Testa", "Zebra", 3) 
        are_compatible = have_compatible_diets(animal, another_animal) 
        self.assertFalse(are_compatible)  # Lion and Zebra diets incompatible
