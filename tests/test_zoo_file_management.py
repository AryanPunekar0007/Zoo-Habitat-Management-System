import unittest
from unittest import mock
from d1_project_pitch.src.zoo_file_management import save_animals_to_file, load_animals_from_file

class TestFileManagement(unittest.TestCase):
    """
    Test suite for file saving and loading functionality
    """

    def test_save_animals_to_file_basic(self):
        """
        Statement Testing: Basic test for saving animals to file
        """
        animals = [ 
            { "animal_id": "LION001", 
            "name": "Leo", 
            "species": "Lion", 
            "age": 5 
        } ] 
        
        filename = "test_zoo_data.json" 
        success = save_animals_to_file(animals, filename)
        
        self.assertTrue(success)

    @mock.patch("builtins.open", new_callable=mock.mock_open) 
    @mock.patch("json.dump")
    def test_save_animals_writes_correct_data(self, mock_json_dump, mock_file):
        """
        Test that data is written correctly
        """
        animals = [ {
            "animal_id": "LION001", 
            "name": "Leo", 
            "species": "Lion", 
            "age": 5 
        } ] 
        
        filename = "test_zoo_data.json"
        success = save_animals_to_file(animals, filename)

        self.assertTrue(success) 
        mock_file.assert_called_once_with(filename, "w") #ensures data inside file is correct
        mock_json_dump.assert_called_once_with(animals, mock_file(), indent=2)
    
    @mock.patch("builtins.open", new_callable=mock.mock_open) 
    @mock.patch("json.load")
    def test_load_animals_from_file(self, mock_json_load, mock_file):
        """
        Mock Testing: Test loading animals from file
        """
        filename = "test_zoo_data.json" 
        expected_animals = [{ 
            "animal_id": "LION001", 
            "name": "Leo", 
            "species": "Lion" 
        }]

        mock_json_load.return_value = expected_animals

        mock_file.return_value.read.return_value = '[{"animal_id": "LION001", "name": "Leo", "species": "Lion"}]'

        loaded_animals = load_animals_from_file(filename) 
        self.assertEqual(loaded_animals, expected_animals)
        mock_file.assert_called_once_with(filename, "r")
        mock_json_load.assert_called_once_with(mock_file())

