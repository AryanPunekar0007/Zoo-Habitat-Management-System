"""
File responsible for breeding eligibility of an animal
"""

from d1_project_pitch.src.zoo_species_data import get_breeding_data

def check_breeding_eligibility(animal):
    """
    Check if animal is eligible for breeding
    """
    species = animal.get("species", "") 
    age = animal.get("age", 0)
    health_status = animal.get("health_status", "unknown") 
    genetic_diversity = animal.get("genetic_diversity", "unknown")

    breeding_data = get_breeding_data(species) 
    min_age = breeding_data["min_age"] 
    max_age = breeding_data["max_age"]

    #Age check
    age_ok, reason = check_age_eligibility(age, min_age, max_age) 
    if not age_ok: 
        return False, reason
    
    #health checks
    if health_status != "healthy": 
        return False, f"Not eligible due to health status: {health_status}" 
    
    # Genetic diversity check 
    if genetic_diversity == "low": 
        return False, "Not eligible: low genetic diversity" 
    
    return True, "Healthy and eligible for breeding program"

def check_age_eligibility(age, min_age, max_age):
    """
    Check if animal is within the right age
    """
    if age < min_age: 
        return False, f"Too young for breeding program. Minimum age: {min_age} years" 
    
    if age > max_age: 
        return False, f"Too old for breeding program. Maximum age: {max_age} years" 
    
    return True, "Age within breeding range"


