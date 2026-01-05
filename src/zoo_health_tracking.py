"""
File that records the health check for an animal
"""

import datetime
from d1_project_pitch.src.zoo_species_data import *

def record_health_check(animal, health_data):
    """
    
    Record health check for animal
    
    """
    updated_animal = animal.copy()

    #initialise if not there alrady
    if "health_records" not in updated_animal:
        updated_animal["health_records"] = []

    #create entry for a health record with a format
    health_record = { 
        "date": datetime.datetime.now().isoformat(), 
        "data": health_data
          }
    
    #adds the new health record to the animals list of past records
    updated_animal["health_records"].append(health_record) 
    return updated_animal

def check_weight(latest_record, baseline, issues):
    """
    Records the weigh of an animal
    """
    if "weight_kg" in latest_record:
        weight = latest_record["weight_kg"]
        min_weight, max_weight = baseline["weight_range"]

        if weight <= 0:
            issues.append("invalid weight")
        elif weight < min_weight:
            issues.append(f"underweight ({weight}kg < {min_weight}kg)")
        elif weight > max_weight:
            issues.append(f"overweight ({weight}kg > {max_weight}kg)")

def check_temperature(latest_record, baseline, issues):
    """
    Records the temp of an animal
    """
    if "temperature_c" in latest_record: 
        temp = latest_record["temperature_c"] 
        min_temp, max_temp = baseline["temp_range"] 
        
        if temp < min_temp: 
            issues.append(f"low temperature ({temp}°C < {min_temp}°C)") 
        elif temp > max_temp: 
            issues.append(f"high temperature ({temp}°C > {max_temp}°C)")

def check_heart_rate(latest_record, baseline, issues):
    """
    Records the heart rate
    """
    if "heart_rate" in latest_record: 
        hr = latest_record["heart_rate"] 
        min_hr, max_hr = baseline["hr_range"] 
        
        if hr <= 0: 
            issues.append("invalid heart rate") 
        elif hr < min_hr: 
            issues.append(f"low heart rate ({hr}bpm < {min_hr}bpm)") 
        elif hr > max_hr: 
            issues.append(f"high heart rate ({hr}bpm > {max_hr}bpm)")

def calculate_health_status(animal):
    """
    Calculate overall health status based on latest health check
    """

    if "health_records" not in animal or not animal["health_records"]: 
        return "unknown", "No health records available"

    #since we store previous ones as well
    latest_record = animal["health_records"][-1]["data"]


    issues = []
    species = animal.get("species", "")

    baseline = get_health_baseline(species)

    check_weight(latest_record, baseline, issues) 
    check_temperature(latest_record, baseline, issues) 
    check_heart_rate(latest_record, baseline, issues)

    #generic health
    if latest_record.get("vaccination_status") == "overdue": 
        issues.append("vaccinations overdue") 
    elif latest_record.get("vaccination_status") == "none": 
        issues.append("no vaccinations")
    
    #checking vet notes
    vet_notes = latest_record.get("vet_notes", "").lower() 
    concerning_terms = ["lethargic", "lethargy", "not eating", "anorexic", "limping", "injured", "infection"] 
    
    for term in concerning_terms: 
        if term in vet_notes: 
            issues.append(f"noted: {term}") 
            break

    #overall status
    if not issues: 
        return "healthy", "All health indicators normal" 
    elif len(issues) <= 2 and not any("temperature" in issue for issue in issues): 
        return "needs attention", f"Minor issues: {', '.join(issues)}" 
    else: 
        return "critical", f"Health concerns: {', '.join(issues)}"

    
        