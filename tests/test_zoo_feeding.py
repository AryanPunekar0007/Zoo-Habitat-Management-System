import unittest
from d1_project_pitch.src.zoo_feeding import calculate_feeding_schedule, record_feeding, generate_daily_feeding_report

class TestFeedingSystem(unittest.TestCase):
    """
    Test suite for animal feeding schedule
    """
    
    def test_calculate_feeding_schedule_carnivore(self):
        """
        Basic test for carnivore feeding calculation
        """
        lion = { 
            "animal_id": "LION001", 
            "species": "Lion", 
            "diet": "carnivore", 
            "weight_kg": 180 
        }

        schedule = calculate_feeding_schedule(lion)

        self.assertIsInstance(schedule, dict)
        self.assertIn("daily_amount_kg", schedule) 
        self.assertIn("feeding_times", schedule) 
        self.assertIn("food_type", schedule)

    def test_carnivore_feeding_calculation(self):
        """
        Test feeding calculation for carnivores
        """
        lion = { 
            "animal_id": "LION001", 
            "species": "Lion", 
            "diet": "carnivore", 
            "weight_kg": 180 
        }

        schedule = calculate_feeding_schedule(lion)

        self.assertEqual(schedule["food_type"], "meat") 
        self.assertGreater(schedule["daily_amount_kg"], 0)

        expected_min = 180 * 0.03  # 3% 
        expected_max = 180 * 0.06  # 6% 

        self.assertTrue(expected_min <= schedule["daily_amount_kg"] <= expected_max)
    
    def test_herbivore_feeding_calculation(self):
        """
        Test feeding calculation for herbivores
        """
        zebra = { 
            "animal_id": "ZEBRA001",
            "species": "Zebra", 
            "diet": "herbivore", 
            "weight_kg": 300 
        }

        schedule = calculate_feeding_schedule(zebra)
        
        self.assertEqual(schedule["food_type"], "vegetation") 
        self.assertEqual(schedule["daily_amount_kg"], 9.0)  #300 * 0.03 
        self.assertEqual(len(schedule["feeding_times"]), 3)  #more frequent feeding

    def test_sick_animal_feeding_adjustment(self):
        """
        Test feeding adjustment for sick animals
        """
        sick_lion = { 
            "animal_id": "LION002", 
            "species": "Lion", 
            "diet": "carnivore", 
            "weight_kg": 180, 
            "health_status": "needs attention"
        }

        adjusted_schedule = calculate_feeding_schedule(sick_lion)

        normal_schedule = calculate_feeding_schedule({
            "animal_id": "LION001", 
            "species": "Lion", 
            "diet": "carnivore", 
            "weight_kg": 180 
        })

        self.assertLess(adjusted_schedule["daily_amount_kg"], normal_schedule["daily_amount_kg"])

    def test_record_feeding(self):
        """
        Test recording when animal is being fed
        """
        animal = { 
            "animal_id": "LION001", 
            "species": "Lion", 
            "diet": "carnivore" 
        }

        feeding_details = { 
            "time": "08:00", 
            "amount_kg": 3.6, 
            "food_type": "meat", 
            "keeper": "John Doe" 
        }

        updated_animal = record_feeding(animal, feeding_details)

        self.assertIn("feeding_history", updated_animal) 
        self.assertEqual(len(updated_animal["feeding_history"]), 1) 
        self.assertEqual(updated_animal["feeding_history"][0]["amount_kg"], 3.6)
        
    def test_generate_daily_feeding_report(self):
        """
        Test generate a feeding report
        """
        animals = [ { 
            "animal_id": "LION001", 
            "name": "Leo", 
            "species": "Lion",
            "diet": "carnivore", 
            "weight_kg": 180 
        },
        { 
            "animal_id": "ZEBRA001", 
            "name": "Zara", 
            "species": "Zebra", 
            "diet": "herbivore", 
            "weight_kg": 300    
        } 
    ]
        report = generate_daily_feeding_report(animals)
        
        self.assertIn("total_animals", report) 
        self.assertIn("feeding_schedule", report) 
        self.assertIn("total_meat_kg", report) 
        self.assertIn("total_vegetation_kg", report) 
        self.assertEqual(report["total_animals"], 2)


