import unittest
from unittest.mock import patch
from d1_project_pitch.src.zoo_ui import display_main_menu, get_menu_choice, add_new_animal_to_system, record_health_check_in_system, find_animal_by_id, process_feeding_in_system, check_breeding_eligibility_in_system, assign_to_habitat_in_system, view_habitat_report_in_system

class TestZooUI(unittest.TestCase):
    """
    Test suite for main menu user interface
    """
    def test_display_main_menu_options(self):
        """
        Test the main menu with the required options
        """
        with patch('builtins.print') as mock_print:
            display_main_menu()

        #check all optons are printed
        calls = [str(call) for call in mock_print.call_args_list]
        output_text = ' '.join(calls)

        required_options = [ 
            "Add New Animal", 
            "Assign to Habitat", 
            "Record Health Check", 
            "Process Feeding", 
            "Check Breeding Eligibility", 
            "View Habitat Report", 
            "Quit" 
        ]

        for option in required_options: 
            self.assertIn(option, output_text)
    
    @patch('builtins.input', return_value='1')
    def test_get_menu_choice_valid(self, mock_input):
        """
        Branch testing: Test valid menu choice input
        """
        choice = get_menu_choice()

        self.assertEqual(choice, 1) 
        mock_input.assert_called_once_with("Enter your choice (1-7): ")


    @patch('builtins.input', side_effect=['invalid', '8', '2']) 
    @patch('builtins.print') 
    def test_get_menu_choice_invalid_then_valid(self, mock_print, mock_input):
        """
        State transition testing: Test handling of invalid then valid input
        """
        choice = get_menu_choice()

        self.assertEqual(choice, 2)
        self.assertTrue(mock_print.called) 
        self.assertIn("Invalid choice", mock_print.call_args[0][0])
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_add_new_animal(self, mock_print, mock_input):
        """
        Test that animal can be added
        """
        mock_input.side_effect = ['TEST001', 'Bob', 'Lion', '5'] 
        
        animals = []

        result_animals = add_new_animal_to_system(animals)    #add animal

        self.assertEqual(len(result_animals), 1) 
        self.assertEqual(result_animals[0]["animal_id"], "TEST001") 
        self.assertEqual(result_animals[0]["name"], "Bob") 
        self.assertEqual(result_animals[0]["species"], "Lion")

        success_printed = False 
        
        for call in mock_print.call_args_list: #if animal added properly
            if 'Successfully added' in str(call): 
                success_printed = True 
                break 
        
        self.assertTrue(success_printed)
    
    @patch('builtins.input')
    @patch('builtins.print')
    def test_add_new_animal_workflow_duplicate_id(self, mock_print, mock_input):
        """
        Test animal addition with duplicate ID
        """
        mock_input.side_effect = ['LION001', 'Leo', 'Lion', '5']

        animals = [{
            "animal_id": "LION001", 
            "name": "Existing", 
            "species": "Lion", 
            "age": 3 
        }]

        result_animals = add_new_animal_to_system(animals)

        self.assertEqual(len(result_animals), 1) #should remain the same since animal already exists
        self.assertEqual(result_animals[0]["name"], "Existing")

        failure_printed = False 
        
        for call in mock_print.call_args_list: 
            if 'Failed' in str(call) or 'duplicate' in str(call).lower(): 
                failure_printed = True 
                break 
        self.assertTrue(failure_printed)
    
    def test_record_health_check_workflow_success(self):
        """
        Test for checking health record
        """
        animals = [ { 
            'animal_id': 'LION001', 
            'name': 'Leo', 
            'species': 'Lion', 
            'health_records': [] 
        } ]

        with patch('builtins.input', side_effect=['LION001', '180', '38.5', '65', 'current', 'Healthy']), \
        patch('builtins.print') as mock_print:
            result_animals = record_health_check_in_system(animals)
        
        updated_animal = find_animal_by_id('LION001', result_animals) 
        self.assertIsNotNone(updated_animal) 
        self.assertEqual(len(updated_animal['health_records']), 1) 
        
        success_printed = any('Health check recorded' in str(call) for call in mock_print.call_args_list) 
        self.assertTrue(success_printed)

    def test_process_feeding_workflow_display_schedule(self):
        """
        Test feeding workflow displays schedule correctly
        """
        animals = [ { 
            'animal_id': 'LION001', 
            'name': 'Leo', 
            'species': 'Lion', 
            'diet': 'carnivore', 
            'weight_kg': 180 
        } ]

        with patch('builtins.input', return_value='n'), \
        patch('builtins.print') as mock_print:
            result_animals = process_feeding_in_system(animals)

        schedule_printed = any('Feeding Schedule' in str(call) for call in mock_print.call_args_list) 
        self.assertTrue(schedule_printed)

        meat_printed = any('meat' in str(call).lower() for call in mock_print.call_args_list)
        self.assertTrue(meat_printed)


    def test_process_feeding_workflow_record_feeding(self):
        """
        Test recording a feeding through the workflow
        """
        animals = [ { 
            'animal_id': 'LION001', 
            'name': 'Leo', 
            'species': 'Lion', 
            'feeding_history': [] 
        } ]

        with patch('builtins.input', side_effect=['y', 'LION001', '08:00', '3.5', 'meat', 'John']), \
        patch('builtins.print') as mock_print:
            result_animals = process_feeding_in_system(animals)

        updated_animal = find_animal_by_id('LION001', result_animals) 
        self.assertIsNotNone(updated_animal) 
        self.assertEqual(len(updated_animal['feeding_history']), 1)

        success_printed = any('Feeding recorded' in str(call) for call in mock_print.call_args_list) 
        self.assertTrue(success_printed)
    
    def test_check_breeding_eligibility_workflow(self):
        """
        Test breeding eligibility workflow
        """
        animals = [ { 
            'animal_id': 'LION001', 
            'name': 'Leo', 
            'species': 'Lion',
            'age': 5, 
            'health_status': 
            'healthy', 
            'genetic_diversity': 'high' 
        }, 
        
        { 
        'animal_id': 'LION002', 
        'name': 'Luna', 
        'species': 'Lion', 
        'age': 2,  # Too young 
        'health_status': 'healthy', 
        'genetic_diversity': 'high' 
        } ]

        with patch('builtins.print') as mock_print: 
            result_animals = check_breeding_eligibility_in_system(animals)
        
        eligibility_printed = any('Eligibility' in str(call) for call in mock_print.call_args_list)
        self.assertTrue(eligibility_printed)

        #should show both eligible and inelgible respectively
        eligible_printed = any('Eligible' in str(call) for call in mock_print.call_args_list) 
        not_eligible_printed = any('Not Eligible' in str(call) for call in mock_print.call_args_list) 

        self.assertTrue(eligible_printed) 
        self.assertTrue(not_eligible_printed)
    
    def test_assign_to_habitat_workflow_with_animals(self):
        """
        Test habitat assignment workflow with animals
        """
        animals = [ { 
            "animal_id": "ZEBRA001",
            "name": "Stripes", 
            "species": "Zebra", 
            "habitat_type": "savannah"
        } ]

        habitats = { 
            "savannah": { 
                "name": "Savannah Plains",
                "capacity": 4, "current_animals": [] 
        } }

        with patch('builtins.input', side_effect=['ZEBRA001', 'savannah']), \
        patch('builtins.print') as mock_print:
            result_animals, result_habitats = assign_to_habitat_in_system(animals, habitats)
        
        self.assertIsNotNone(result_animals)
        self.assertIsNotNone(result_habitats)
    
    def test_assign_to_habitat_workflow_failure(self):
        """
        Test a failed attempt at assigning an animal to a habitat
        """
        animals = [ { 
            "animal_id": "ZEBRA001",
            "name": "Stripes", 
            "species": "Zebra", 
            "habitat_type": "savannah"
        } ]

        habitats = { 
            "savannah": { 
                "name": "Savannah Plains",
                "capacity": 4, "current_animals": [] 
        } }

        with patch('builtins.input', side_effect=['UNKNOWN001', 'savannah']), \
        patch('builtins.print') as mock_print:
            
            result_animals, result_habitats = assign_to_habitat_in_system(animals, habitats)

            self.assertEqual(len(result_habitats["savannah"]["current_animals"]), 0)

            error_printed = any('not found' in str(call) for call in mock_print.call_args_list) 
            
            self.assertTrue(error_printed)
        
    def test_view_habitat_report_workflow(self):
        """
        Test habitat report generation through UI
        """

        animals = [ { 
            "animal_id": "ZEBRA001",
            "name": "Stripes", 
            "species": "Zebra" 
        } ] 
        
        habitats = { "savannah": 
                    { 
                        "name": "Savannah Plains", 
                        "capacity": 4, 
                        "current_animals": ["ZEBRA001"] 
                } 
                
        }

        with patch('builtins.print') as mock_print:
            result_animals, result_habitats = view_habitat_report_in_system(animals, habitats)
        
        report_printed = any('Habitat Report' in str(call) for call in mock_print.call_args_list) 
        self.assertTrue(report_printed)

        