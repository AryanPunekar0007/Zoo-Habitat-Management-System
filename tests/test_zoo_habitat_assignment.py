import unittest
from unittest.mock import patch
import d1_project_pitch.src.zoo_species_data
from d1_project_pitch.src.zoo_habitat_assignment import assign_animal_to_habitat, remove_animal_from_habitat, get_animal_habitat, generate_habitat_report
class TestHabitatManagement(unittest.TestCase):
    """
    Test suite for habitat assignment and management
    """

    def setUp(self): 
        """
        Set up fresh habitats for each test
        """ 
        self.habitats = { 
            "savannah": {
                "name": "Savannah Plains", 
                "capacity": 4, 
                "current_animals": [], 
                "features": ["grasslands", "watering_hole", "shade_trees"] 
            }, 
            
            "forest": { 
                "name": "Forest Enclosure", 
                "capacity": 3, 
                "current_animals": [], 
                "features": ["dense_vegetation", "climbing_trees", "stream"] 
            }, 
            
            "aquatic": { 
                "name": "Aquatic Center", 
                "capacity": 2, 
                "current_animals": [], 
                "features": ["deep_pool", "filtration_system", "viewing_glass"] 
            },

            "arctic": { 
                "name": "Arctic Zone", 
                "capacity": 3, 
                "current_animals": [], 
                "features": ["cooling_system", "snow_simulation", "ice_pond"], 
            }

        }
    
    def test_assign_elephant_to_savannah(self):
        """
        Test assigning an elephant to savannah habitat
        """
        elephant = { 
            "animal_id": "ELEPH001", 
            "name": "Ellie", 
            "species": "Elephant", 
            "habitat_type": "savannah" 
        }

        success, message = assign_animal_to_habitat(elephant, "savannah", self.habitats)

        self.assertTrue(success) 
        self.assertIn("Successfully assigned", message) 
        self.assertIn("ELEPH001", self.habitats["savannah"]["current_animals"])
    
    def test_assign_giraffe_to_full_habitat(self):
        """
        Test assigning giraffe to a full capacity savannah habitat
        """
        savannah = self.habitats["savannah"]
        savannah["current_animals"] = ["LION001", "LION002", "LION003", "LION004"]

        giraffe = { 
            "animal_id": "GIRAFFE001", 
            "name": "Stretch", 
            "species": "Giraffe", 
            "habitat_type": "savannah" 
        }


        success, message = assign_animal_to_habitat(giraffe, "savannah", self.habitats)

        self.assertFalse(success) 
        self.assertIn("full capacity", message.lower()) 
        self.assertNotIn("GIRAFFE001", self.habitats["savannah"]["current_animals"])
    
    def test_assign_incompatible_animals_fails(self):
        """
        Test that habitat assignment fails for incompatible animals
        """

        zebra = { 
            "animal_id": "ZEBRA001", 
            "name": "Stripes", 
            "species": "Zebra", 
            "diet": "herbivore", 
            "habitat_type": "savannah" 
        }

        cheetah = { 
            "animal_id": "CHEETAH001", 
            "name": "Spot", 
            "species": "Cheetah", 
            "diet": "carnivore", 
            "habitat_type": "savannah" 
        }

        success, message = assign_animal_to_habitat(cheetah, "savannah", self.habitats)
    
    def test_assign_compatible_animals_succeeds(self):
        """
        Test that habitat assignment succeeds
        """
        zebra1 = { 
            "animal_id": "ZEBRA001", 
            "name": "Stripes", 
            "species": "Zebra", 
            "diet": "herbivore", 
            "habitat_type": "savannah", 
            "temperament": "timid" 
        }, 
        
        zebra2 = { 
            "animal_id": "ZEBRA002", 
            "name": "Dotty", 
            "species": "Zebra", 
            "diet": "herbivore", 
            "habitat_type": "savannah", 
            "temperament": "timid" 
        }

        all_animals = [zebra1]

        success, message = assign_animal_to_habitat(zebra2, "savannah", self.habitats, all_animals)

        self.assertTrue(success) 
        self.assertIn("Successfully assigned", message) 
        self.assertIn("ZEBRA002", self.habitats["savannah"]["current_animals"])
    
    def test_remove_animal_from_habitat(self):
        """
        Test to remove animal from a habitat
        """

        bear1 = { 
            "animal_id": "BEAR001", 
            "name": "Bobby", 
            "species": "Bear", 
            "diet": "carnivore", 
            "habitat_type": "forest", 
            "temperament": "timid" 
        }

        self.habitats["forest"]["current_animals"].append("BEAR001")

        success, message = remove_animal_from_habitat("BEAR001", "forest", self.habitats) 
        
        self.assertTrue(success) 
        self.assertIn("Removed", message) 
        self.assertNotIn("BEAR001", self.habitats["forest"]["current_animals"])
    
    def test_get_animal_habitat(self):
        """
        Test finding which habitat an animal is in
        """
        self.habitats["forest"]["current_animals"].append("WOLF001")

        habitat_name = get_animal_habitat("WOLF001", self.habitats)

        self.assertEqual(habitat_name, "forest")
    
    def test_generate_habitat_report_empty(self):
        """
        Test generating habitat report when no animals are assigned
        """
        habitats = {
             "savannah": { 
                "name": "Savannah Plains", 
                "capacity": 4,
                "current_animals": [] 
            }, 
            
            "forest": { 
                "name": "Forest Enclosure", 
                "capacity": 3, 
                "current_animals": [] 
            } }
        
        animals = []

        report = generate_habitat_report(habitats, animals)

        self.assertIsInstance(report, dict) 
        self.assertEqual(report["total_habitats"], 2) 
        self.assertEqual(report["total_animals_assigned"], 0) 
        self.assertIn("savannah", report["habitats"]) 
        self.assertIn("forest", report["habitats"])
    
    def test_generate_habitat_report_with_animals(self):
        """
        Test generating habitat report with assigned animals
        """
        self.habitats["savannah"]["current_animals"] = ["ZEBRA001", "GIRAFFE001"]
        self.habitats["forest"]["current_animals"] = ["WOLF001"]

        animals = [ { 
            "animal_id": "ZEBRA001", 
            "name": "Stripes", 
            "species": "Zebra",
            "habitat_type": "savannah"
        }, 
        
        { 
            "animal_id": "GIRAFFE001", 
            "name": "Stretch", 
            "species": "Giraffe",
            "habitat_type": "savannah"
        }, 
        
        { 
            "animal_id": "WOLF001", 
            "name": "Fang",
            "species": "Wolf",
            "habitat_type": "forest"
        } ]


        report = generate_habitat_report(self.habitats, animals)

        self.assertEqual(report["total_habitats"], 4)  # since setUp defines 4 total
        self.assertEqual(report["total_animals_assigned"], 3)

        #habitat details
        savannah_info = report["habitats"]["savannah"] 
        self.assertEqual(savannah_info["current_count"], 2)

        self.assertEqual(savannah_info["available_space"], 2)
        self.assertEqual(len(savannah_info["animals"]), 2) # 4 capacity - 2 animals
        self.assertEqual(savannah_info["animals"][0]["name"], "Stripes")

        #check forest details
        forest_info = report["habitats"]["forest"] 
        self.assertEqual(forest_info["current_count"], 1)
        self.assertEqual(forest_info["available_space"], 2)  # 3 capacity - 1 animal
    
    def test_generate_habitat_report_mixed_occupancy(self):
        """
        Test report with some habitats empty and some with animals
        """

        self.habitats["savannah"]["current_animals"] = ["ZEBRA001"]  # One animal 
        self.habitats["forest"]["current_animals"] = []  # Empty 
        self.habitats["aquatic"]["current_animals"] = ["HIPPO001", "HIPPO002"]  # Full
    
        animals = [ { 
            "animal_id": "ZEBRA001", 
            "name": "Stripes", 
            "species": "Zebra" 
        }, 
        { 
            "animal_id": "HIPPO001", 
            "name": "Hank",
            "species": "Hippopotamus" 
        }, 
        { 
            "animal_id": "HIPPO002", 
            "name": "Henrietta", 
            "species": "Hippopotamus" 
        } ]

        report = generate_habitat_report(self.habitats, animals)

        self.assertEqual(report["total_animals_assigned"], 3) #3 animals assigned

        #savannah
        self.assertEqual(report["habitats"]["savannah"]["current_count"], 1) 
        self.assertEqual(report["habitats"]["savannah"]["available_space"], 3)

        #forest
        self.assertEqual(report["habitats"]["forest"]["current_count"], 0) 
        self.assertEqual(report["habitats"]["forest"]["available_space"], 3)

        #acquatic
        self.assertEqual(report["habitats"]["aquatic"]["current_count"], 2) 
        self.assertEqual(report["habitats"]["aquatic"]["available_space"], 0) 

