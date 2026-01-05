"""
File that manages the files in the system
"""

import json

def save_animals_to_file(animals, filename):
    """
    Save animal data to a JSON file
    """
    try: 
        with open(filename, 'w') as file: 
            json.dump(animals, file, indent=2) 
            return True 
    except Exception as e: 
        print(f"Error saving animals to file: {e}") 
        return False

def load_animals_from_file(filename):
    """
    Load aniamals from a JSON file
    """
    try: 
        with open(filename, 'r') as file: 
            animals = json.load(file) 
            return animals 
    except FileNotFoundError: 
        print(f"File {filename} not found. Starting with empty animal list.") 
        return [] 
    except Exception as e: 
        print(f"Error loading animals from file: {e}") 
        return []
