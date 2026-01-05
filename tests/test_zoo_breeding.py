import unittest
from d1_project_pitch.src.zoo_breeding import check_breeding_eligibility
from d1_project_pitch.src.zoo_breeding import get_breeding_data

class TestBreedingSystem(unittest.TestCase):
    """
    Test suite for animal breeding program eligibility
    """

    def test_healthy_animal_breeding_eligibility(self):
        """
        Basic test for healthy animal breeding eligibility
        """
        healthy_animal = { 
            "animal_id": "LION001", 
            "species": "Lion", 
            "age": 5, 
            "health_status": "healthy", 
            "genetic_diversity": "high" 
        }

        is_eligible, reason = check_breeding_eligibility(healthy_animal)
        
        self.assertTrue(is_eligible) 
        self.assertIn("eligible", reason.lower())

    def test_animal_too_young_for_breeding(self):
        """
        Branch testing: Test that animals below minimum breeding age are ineligible
        """
        lion_data = get_breeding_data("Lion") 
        min_age = lion_data["min_age"]

        young_lion = { 
            "animal_id": "LION002", 
            "species": "Lion", 
            "age": min_age - 1,  # One year below minimum 
            "health_status": "healthy", 
            "genetic_diversity": "high" 
        }

        is_eligible, reason = check_breeding_eligibility(young_lion)

        self.assertFalse(is_eligible) 
        self.assertIn("age", reason.lower()) 
        self.assertIn(str(min_age), reason)

    def test_animal_too_old_for_breeding(self):
        """
        Branch testing: Test that animals above minimum breeding age are ineligible
        """
        lion_data = get_breeding_data("Lion") 
        max_age = lion_data["max_age"]

        old_lion = { 
            "animal_id": "LION003", 
            "species": "Lion", 
            "age": max_age + 1,  # One year above maximum 
            "health_status": "healthy", 
            "genetic_diversity": "high"
        }

        is_eligible, reason = check_breeding_eligibility(old_lion) 
        self.assertFalse(is_eligible) 
        self.assertIn("old", reason.lower()) 
        self.assertIn(str(max_age), reason)