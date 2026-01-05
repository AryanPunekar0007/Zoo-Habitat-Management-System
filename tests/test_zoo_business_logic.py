import unittest 
from d1_project_pitch.src.zoo_business_logic import is_predator, have_compatible_diets, have_compatible_habitats, check_habitat_compatibility, have_compatible_temperaments, have_compatible_social_needs


class TestAnimalCreation(unittest.TestCase):

    def test_can_create_animal_object(self):
        """
        Testing whether animal data structures can be created, 
        helping define the properties of the animal
        """

        test_animal = {
            "animal_id": "LION001", 
            "name": "Leo", 
            "species": "Lion", 
            "diet": "carnivore" 
            }
        

        self.assertIn("animal_id", test_animal) 
        self.assertIn("species", test_animal) 
        self.assertIn("diet", test_animal) 
        self.assertEqual(test_animal["species"], "Lion")
    

    def test_identify_carnivore_as_predator(self):
        """
        Test to see if carnivores can be identified as potential predetors
        """

        carnivore = { 
            "animal_id": "LION001", 
            "species": "Lion",
            "diet": "carnivore" 
            }
        

        self.assertTrue(is_predator(carnivore))

    def test_identify_herbivore_as_non_predator(self):
        """
        Test to see that herbivores aren't predators
        """

        herbivore = { 
            "animal_id": "ZEBRA001",
            "species": "Zebra", 
            "diet": "herbivore" 
            }
        
        self.assertFalse(is_predator(herbivore))

    def test_same_diet_animals_are_compatible(self):
        """
        Test to check that animals that are on the same diet are compatible
        """
        herbivore1 = { 
            "animal_id": "ZEBRA001", 
            "species": "Zebra", 
            "diet": "herbivore" 
                    }
        
        herbivore2 = { 
            "animal_id": "GIRAFFE001", 
            "species": "Giraffe", 
            "diet": "herbivore" 
            }
        
        self.assertTrue(have_compatible_diets(herbivore1, herbivore2))
    
    def test_carnivore_and_herbivore_diets_are_incompatible(self):
        """
        Test the False branch of have_compatible_diets when one is carnivore and one is herbivore
        """
        carnivore = { 
            "animal_id": "LION001", 
            "species": "Lion", 
            "diet": "carnivore" 
            }
        
        herbivore = { 
            "animal_id": "ZEBRA001", 
            "species": "Zebra", 
            "diet": "herbivore" 
                    }
        
        self.assertFalse(have_compatible_diets(carnivore, herbivore))

        
    def test_same_habitat_type_is_compatible(self):
        """
        Test for habitat compatibility function with same habitat types
        """
        animal1 = { 
            "animal_id": "LION001",
            "species": "Lion", 
            "diet": "carnivore", 
            "habitat_type": "savannah" 
            }
        
        animal2 = { 
            "animal_id": "ZEBRA002", 
            "species": "Zebra", 
            "diet": "herbivore", 
            "habitat_type": "savannah" 
            }
        
        self.assertTrue(have_compatible_habitats(animal1, animal2))

    def test_full_habitat_compatibility_check(self):
        """
        Integration test: Combine diet and habitat checks
        """
        animal1 = { 
            "animal_id": "ZEBRA001", 
            "species": "Zebra", 
            "diet": "herbivore", 
            "habitat_type": "savannah" 
            }
        
        animal2 = { 
            "animal_id": "GIRAFFE001", 
            "species": "Giraffe", 
            "diet": "herbivore", 
            "habitat_type": "savannah" 
            }
        
        self.assertTrue(check_habitat_compatibility(animal1, animal2))
    
    def test_animals_with_same_temperament_are_compatible(self):
        """
        Test temperament compatibility function
        """
        animal1 = { 
            "animal_id": "ZEBRA001",
            "species": "Zebra", 
            "diet": "herbivore", 
            "habitat_type": "savannah", 
            "temperament": "social" 
            }
        
        animal2 = { 
            "animal_id": "GIRAFFE001", 
            "species": "Giraffe", 
            "diet": "herbivore", 
            "habitat_type": "savannah",
            "temperament": "social" 
            }
        
        self.assertTrue(have_compatible_temperaments(animal1, animal2))
        

    def test_aggressive_and_timid_temperaments_are_incompatible(self):
        """
        Test different temperaments are incompatible
        """
        aggressive_animal = { 
            "animal_id": "LION001",
            "species": "Lion",
            "diet": "carnivore", 
            "habitat_type": "savannah", 
            "temperament": "aggressive" 
            }
        
        timid_animal = { 
            "animal_id": "GAZELLE001", 
            "species": "Gazelle", 
            "diet": "herbivore", 
            "habitat_type": "savannah", 
            "temperament": "timid" 
            }
        
        self.assertFalse(have_compatible_temperaments(aggressive_animal, timid_animal))

    def test_compatible_social_needs(self):
        """
        Test social needs
        """
        animal1 = { 
            "animal_id": "TIGER001", 
            "species": "Tiger", 
            "social_needs": "solitary" 
            }
        
        animal2 = { 
            "animal_id": "LEOPARD001", 
            "species": "Leopard", 
            "social_needs": "solitary" 
            }
        
        self.assertTrue(have_compatible_social_needs(animal1, animal2))
