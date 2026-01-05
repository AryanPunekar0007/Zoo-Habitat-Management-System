"""
File that is responsible for the feeding of an animal
"""

import datetime

def calculate_feeding_schedule(animal):
    """
    Calculate feeding schedule based on animal species, diet, and weight
    """
    diet = animal.get("diet", "unknown") 
    weight = animal.get("weight_kg", 0)
    health_status = animal.get("health_status", "healthy")

    base_amount = 0 
    food_type = "unknown" 
    feeding_times = []

    if diet == "carnivore":
        base_amount = weight * 0.04
        food_type = "meat"
        feeding_times = ["08:00", "17:00"]
    elif diet == "herbivore":
        base_amount = weight * 0.03  # Average of 3%
        food_type = "vegetation" 
        feeding_times = ["06:00", "12:00", "18:00"]

    adjustment_factor = 1.0   #how much the normal food intake should be increased or decreased depending on the animals state
    if health_status == "needs attention": 
        adjustment_factor = 0.8  # 20% reduction 
    elif health_status == "critical": 
        adjustment_factor = 0.6  # 40% reduction 
    elif health_status == "healthy": 
        adjustment_factor = 1.0  # Normal amount


    final_amount = base_amount * adjustment_factor

    return { 
        "daily_amount_kg": round(final_amount, 2), 
        "feeding_times": feeding_times, 
        "food_type": food_type, 
        "health_adjustment": f"{adjustment_factor * 100}%" 
    }

def record_feeding(animal, feeding_details):
    """
    Record feeding for an animal
    """
    updated_animal = animal.copy()

    if "feeding_history" not in updated_animal: 
        updated_animal["feeding_history"] = []

    feeding_record = feeding_details.copy() 
    feeding_record["timestamp"] = datetime.datetime.now().isoformat()

    updated_animal["feeding_history"].append(feeding_record) 
    return updated_animal

def generate_daily_feeding_report(animals):
    """
    Generate a daily feeding report for all animals
    """
    report = { 
        "total_animals": len(animals), 
        "feeding_schedule": [], 
        "total_meat_kg": 0, 
        "total_vegetation_kg": 0, 
        "report_date": datetime.datetime.now().date().isoformat() 
    }

    for animal in animals: 
        schedule = calculate_feeding_schedule(animal) 
        
        report["feeding_schedule"].append({ 
            "animal_id": animal["animal_id"], 
            "name": animal.get("name", "Unknown"), 
            "species": animal["species"], 
            "schedule": schedule 
        })

        if schedule["food_type"] == "meat":
            report["total_meat_kg"] += schedule["daily_amount_kg"] 
        elif schedule["food_type"] == "vegetation": 
            report["total_vegetation_kg"] += schedule["daily_amount_kg"] 
        
        return report
