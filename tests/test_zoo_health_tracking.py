import unittest
from d1_project_pitch.src.zoo_health_tracking import record_health_check, calculate_health_status, get_health_baseline, get_species_data
from d1_project_pitch.src.zoo_species_data import SPECIES_HEALTH_BASELINES


class TestHealthTracking(unittest.TestCase):

    def test_record_health_check_basic(self):
        """
        Test to record health check for animal
        """
        animal = { 
            "animal_id": "LION001", 
            "name": "Leo", 
            "species": "Lion" 
            }
        
        health_data = { 
            "weight_kg": 190, 
            "temperature_c": 38.5, 
            "vet_notes": "Healthy, good condition" 
            }
        
        updated_animal = record_health_check(animal, health_data)

        self.assertIn("health_records", updated_animal)
        self.assertIsInstance(updated_animal["health_records"], list) #check object type is list

        self.assertEqual(len(updated_animal["health_records"]), 1) #1 record is added
        self.assertIn("date", updated_animal["health_records"][0]) #the record has a timestamp
        self.assertEqual(updated_animal["health_records"][0]["data"], health_data) #does the data match

    def test_calculate_health_status_healthy(self):
        """
        Branch testing: Test health status calculation for healthy animal
        """

        #data from zoo
        lion_data = get_species_data("Lion")
        weight_range = lion_data["weight_range"] 
        temp_range = lion_data["temp_range"] 
        hr_range = lion_data["hr_range"]

        #healthy values within range
        healthy_weight = (weight_range[0] + weight_range[1]) / 2  # Midpoint 
        healthy_temp = (temp_range[0] + temp_range[1]) / 2        # Midpoint 
        healthy_hr = (hr_range[0] + hr_range[1]) / 2              # Midpoint

        animal = { 
            "animal_id": "LION001", 
            "species": "Lion", 
            "health_records": [ 
                { "date": "2024-01-15T10:00:00", 
                 
                "data": { 
                    "weight_kg": healthy_weight, 
                    "temperature_c": healthy_temp, 
                    "heart_rate": healthy_hr, 
                    "vaccination_status": "current", 
                    "vet_notes": "Excellent condition" 

                    } 
                    } 
                    ]}

        result = calculate_health_status(animal)

        #check that the value retured is a tuple
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)

        health_status, details = result  
        self.assertEqual(health_status, "healthy") 
        self.assertIn("normal", details.lower())
    
    def test_calculate_health_status_underweight(self):
        """
        Test health status calculation for underweight animal
        """
        lion_data = get_species_data("Lion") 
        weight_range = lion_data["weight_range"]

        underweight = weight_range[0] - 10  #10 below min

        animal = { 
            "animal_id": "LION002", 
            "species": "Lion", 
            "health_records": [ 
                { "date": "2024-01-15T10:00:00", 
                
                "data": { 
                    "weight_kg": underweight, 
                    "temperature_c": 38.5, 
                    "heart_rate": 55, 
                    "vaccination_status": "current" 
                    
                    } 
                    } 
                    ]}
        
        health_status, details = calculate_health_status(animal) 
        
        self.assertEqual(health_status, "needs attention") 
        self.assertIn("underweight", details.lower()) 
        self.assertIn(f"{underweight}kg", details)

    def test_calculate_health_status_high_temperature(self):
        """
        Test health status with high temperature
        """
        elephant_data = get_species_data("Elephant") 
        temp_range = elephant_data["temp_range"]

        high_temp = temp_range[1] + 0.5

        animal = { 
            "animal_id": "ELEPH001", 
            "species": "Elephant", ""
            "health_records": [ 
                { "date": "2024-01-15T10:00:00", 
                
                "data": { 
                    "weight_kg": 4000,
                    "temperature_c": high_temp, 
                    "heart_rate": 35, 
                    "vaccination_status": "current" 
                    
                    } 
                    } 
                    ]}
        
        health_status, details = calculate_health_status(animal)

        self.assertEqual(health_status, "critical") 
        self.assertIn("high temperature", details.lower()) 
        self.assertIn(f"{high_temp}°C", details)
    
    def test_calculate_health_status_unknown_species(self):
        """
        Test health for unknown species
        """
        animal = { 
            "animal_id": "UNKN001", 
            "species": "Mystery Animal", 
            "health_records": [ 
                { "date": "2024-01-15T10:00:00", 
                 
                "data": { 
                    "weight_kg": 50,    
                    "temperature_c": 38.0,  
                    "heart_rate": 80, 
                    "vaccination_status": "current" 
                    
                    } } ] }
        
        health_status, details = calculate_health_status(animal)
        
        self.assertEqual(health_status, "healthy")
    
    def test_calculate_health_status_no_records(self):
        """
        Test health status with no record
        """
        animal = { 
            "animal_id": "LION004", 
            "species": "Lion", 
            "health_records": []
        }

        health_status, details = calculate_health_status(animal)

        self.assertEqual(health_status, "unknown") 
        self.assertIn("no health records", details.lower())



