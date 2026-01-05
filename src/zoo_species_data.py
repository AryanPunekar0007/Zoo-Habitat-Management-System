"""
File that contains all the data about the animals in the zoo
"""


SPECIES_HEALTH_BASELINES = {
    "Lion": { 
        "id": 'LION001',
        "weight_range": (150, 250),
        "temp_range": (38.0, 39.5), 
        "hr_range": (40, 70), 
        "diet": "carnivore", 
        "habitat_type": "savannah", 
        "temperament": "aggressive", 
        "social_needs": "pride",
        "breeding_age_min": 3, 
        "breeding_age_max": 15, 
        "gestation_period_days": 110
        },

    "Elephant": { 
        "id": 'ELEPHANT001',
        "weight_range": (2500, 6000), 
        "temp_range": (35.9, 36.9), 
        "hr_range": (25, 40), 
        "diet": "herbivore", 
        "habitat_type": "savannah", 
        "temperament": "calm", 
        "social_needs": "herd",
        "breeding_age_min": 10, 
        "breeding_age_max": 50, 
        "gestation_period_days": 660
        },

    "Wolf": { 
        "id": 'WOLF001',
        "weight_range": (30, 60), 
        "temp_range": (38.0, 39.0), 
        "hr_range": (60, 90), 
        "diet": "carnivore", 
        "habitat_type": "forest", 
        "temperament": "social", 
        "social_needs": "pack",
        "breeding_age_min": 2, 
        "breeding_age_max": 10, 
        "gestation_period_days": 63
        },

    "Zebra": { 
        "id": 'ZEBRA001',
        "weight_range": (200, 400), 
        "temp_range": (36.5, 38.5), 
        "hr_range": (60, 80), 
        "diet": "herbivore", 
        "habitat_type": "savannah", 
        "temperament": "timid", 
        "social_needs": "herd",
        "breeding_age_min": 2, 
        "breeding_age_max": 15, 
        "gestation_period_days": 375
        },

    "Giraffe": { 
        "id": 'GIRAFFE001',
        "weight_range": (800, 1200), 
        "temp_range": (37.5, 39.0), 
        "hr_range": (40, 60), 
        "diet": "herbivore", 
        "habitat_type": "savannah", 
        "temperament": "calm", 
        "social_needs": "herd",
        "breeding_age_min": 4, 
        "breeding_age_max": 20, 
        "gestation_period_days": 450
        },

    "Tiger": { 
        "id": 'TIGER001',
        "weight_range": (100, 200), 
        "temp_range": (37.5, 39.0),
          "hr_range": (45, 75), 
          "diet": "carnivore", 
          "habitat_type": "forest", 
          "temperament": "aggressive", 
          "social_needs": "solitary",
          "breeding_age_min": 3, 
          "breeding_age_max": 12, 
          "gestation_period_days": 105
        },

    "Gorilla": { 
        "id": 'GORILLA001',
        "weight_range": (120, 180), 
        "temp_range": (36.0, 38.0), 
        "hr_range": (60, 90), 
        "diet": "herbivore", 
        "habitat_type": "forest", 
        "temperament": "calm", 
        "social_needs": "troop",
        "breeding_age_min": 3, 
        "breeding_age_max": 12,
        "gestation_period_days": 250
        },
    
    "Kangaroo": { 
        "id": 'KANGAROO001',
        "weight_range": (25, 90), 
        "temp_range": (36.0, 38.5), 
        "hr_range": (70, 120), 
        "diet": "herbivore", 
        "habitat_type": "grassland", 
        "temperament": "timid", 
        "social_needs": "mob",
        "breeding_age_min": 2, 
        "breeding_age_max": 12, 
        "gestation_period_days": 30
        },

    "Hippopotamus": { 
        "id": 'HIPPOPOTAMUS001',
        "weight_range": (1500, 1800), 
        "temp_range": (35.5, 37.0), 
        "hr_range": (25, 35), 
        "diet": "herbivore", 
        "habitat_type": "aquatic", 
        "temperament": "aggressive", 
        "social_needs": "pod",
        "breeding_age_min": 7, 
        "breeding_age_max": 40, 
        "gestation_period_days": 240
        },

    "Cheetah": { 
        "id": 'CHEETAH001',
        "weight_range": (40, 65), 
        "temp_range": (38.0, 39.5),
        "hr_range": (55, 85), 
        "diet": "carnivore", 
        "habitat_type": "savannah", 
        "temperament": "timid", 
        "social_needs": "solitary",
        "breeding_age_min": 2,
        "breeding_age_max": 10, 
        "gestation_period_days": 95 
        },

    "Koala": { 
        "id": 'KOALA001',
        "weight_range": (8, 12), 
        "temp_range": (36.0, 37.5), 
        "hr_range": (80, 140), 
        "diet": "herbivore", 
        "habitat_type": "forest", 
        "temperament": "calm", 
        "social_needs": "solitary",
        "breeding_age_min": 2, 
        "breeding_age_max": 12, 
        "gestation_period_days": 35 
        }
}

GENERIC_BASELINES = {
"large_mammal": {
    "weight_range": (200, 1000), 
    "temp_range": (36.0, 38.5), 
    "hr_range": (40, 80)
    }, 

"medium_mammal": {
    "weight_range": (20, 200), 
    "temp_range": (37.0, 39.0), 
    "hr_range": (60, 120)
    }, 
    
"small_mammal": {
    "weight_range": (1, 20), 
    "temp_range": (37.5, 39.5), 
    "hr_range": (100, 200)
    }, 
    
"bird": {
    "weight_range": (1, 20), 
    "temp_range": (40.0, 42.0), 
    "hr_range": (120, 200)
    }, 
    
"reptile": {
    "weight_range": (5, 200), 
    "temp_range": (25.0, 35.0), 
    "hr_range": (20, 60)
    },     
}

ZOO_HABITATS = { 
    "savannah": { 
        "name": "Savannah Plains", 
        "capacity": 6,
        "current_animals": [], 
        "features": ["grasslands", "watering_hole", "shade_trees"], 
        "compatible_species": ["Lion", "Elephant", "Zebra", "Giraffe", "Cheetah", "Kangaroo"]
    },

    "forest": { 
        "name": "Forest Enclosure", 
        "capacity": 4, 
        "current_animals": [], 
        "features": ["dense_vegetation", "climbing_trees", "stream"], 
        "compatible_species": ["Wolf", "Tiger", "Bear"] 
    },

    "aquatic": { 
        "name": "Aquatic Center", 
        "capacity": 3, 
        "current_animals": [], 
        "features": ["deep_pool", "filtration_system", "viewing_glass"], 
        "compatible_species": ["Hippopotamus"] 
    },

    "arctic": { 
        "name": "Arctic Zone", 
        "capacity": 3, 
        "current_animals": [], 
        "features": ["cooling_system", "snow_simulation", "ice_pond"], 
        "compatible_species": ["Penguin"] 
    }
}

def get_species_data(species_name):
    """
    Get all data for a specific species
    """
    return SPECIES_HEALTH_BASELINES.get(species_name)

def get_health_baseline(species_name):
    """
    Get health baseline for a specific species
    """
    if species_name in SPECIES_HEALTH_BASELINES: 
        return SPECIES_HEALTH_BASELINES[species_name]
    
    species_lower = species_name.lower()

    if any(word in species_lower for word in ["bird", "eagle", 
                                              "owl", "parrot", "penguin"]):
        return GENERIC_BASELINES["bird"]
    
    elif any(word in species_lower for word in ["snake", "lizard",
                                                 "turtle", "reptile", "crocodile"]):
        return GENERIC_BASELINES["reptile"]
    else: 
        baseline = GENERIC_BASELINES["medium_mammal"].copy()
        baseline["note"] = "estimated baseline for unknown mammal species"
        return baseline

def get_breeding_data(species_name):
    """
    Get breeding specific data for a species
    """
    species_data = get_species_data(species_name)

    if species_data:
        return { 
            "min_age": species_data.get("breeding_age_min", 3), 
            "max_age": species_data.get("breeding_age_max", 15),
            "gestation_days": species_data.get("gestation_period_days", 90) 
        }

def get_habitat_data(habitat_name): 
    """ 
    Get data for a specific habitat 
    """ 
    return ZOO_HABITATS.get(habitat_name)
