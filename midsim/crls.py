import json
from itertools import combinations
from pkg_resources import resource_filename

def calculate_all_combinations(lens_indexes):
    """
    Calculate all possible combinations of lens indexes.

    Parameters:
    lens_indexes (list): List of lens indexes (e.g., [1, 2, 3, ..., 9])

    Returns:
    list: List of all possible combinations
    """
    all_combinations = []
    n = len(lens_indexes)
    
    # Generate combinations for all possible lengths (1 to n)
    for k in range(1, n + 1):
        combs = list(combinations(lens_indexes, k))
        all_combinations.extend(combs)
    
    return all_combinations

def calculate_combined_focal_length(indexes, delta=0.01):
    """
    Calculate the combined focal length for specified indexes using the mid_crl2 configuration.

    Parameters:
    indexes (str): String of indexes (e.g., "3589")
    delta (float): Constant for focal length calculation (default is 0.01)

    Returns:
    float: Combined focal length of the specified actuators

    Raises:
    ValueError: If 1 or 10 are specified in the indexes
    """
    crl_2_values = mid_crl2()
    
    # Sort indexes and handle '10' correctly
    sorted_indexes = sorted(indexes, key=lambda x: (len(x), x))
    
    lens_data = []
    for idx in sorted_indexes:
        index = int(idx)
        if index == 1 or index == 10:
            raise ValueError("Index 1 and 10 are not allowed.")
        
        lens_info = crl_2_values.get(index)
        if lens_info and lens_info['lenses']:
            lens_data.append(lens_info['lenses'])
    
    if not lens_data:
        raise ValueError("No valid lens data found for the specified indexes.")
    
    return focal_length_stack(delta, lens_data)

def mid_crl2():
    """
    Returns the configuration of the actuators of CRL-2 at the mid beamline (931 m) of the European XFEL.

    Returns:
    dict: Dictionary with actuator number as keys and a nested dictionary containing 'lenses' and 'N/R' as values.
    """
    crl_2_values = {
        1: {'lenses': None, 'N/R': None},
        2: {'lenses': (1, 5.8), 'N/R': 0.172},
        3: {'lenses': (2, 5.8), 'N/R': 0.345},
        4: {'lenses': (4, 5.8), 'N/R': 0.689},
        5: {'lenses': (7, 5.8), 'N/R': 1.21},
        6: {'lenses': (10, 4.0), 'N/R': 2.5},
        7: {'lenses': (10, 2.0), 'N/R': 5},
        8: {'lenses': (10, 1.0), 'N/R': 10},
        9: {'lenses': (10, 0.5), 'N/R': 20},
        10: {'lenses': None, 'N/R': None}
    }
    return crl_2_values

def save_focal_lengths_to_json(focal_lengths, filename):
    """
    Save the focal lengths dictionary to a JSON file.

    Parameters:
    focal_lengths (dict): Dictionary of focal lengths
    filename (str): Name of the file to save the JSON data
    """
    with open(filename, 'w') as json_file:
        json.dump(focal_lengths, json_file, indent=4)

def mid_crl2_flengths():
    """
    Load the focal lengths dictionary from JSON file and return as mid_crl2_flengths.

    Returns:
    dict: Dictionary of focal lengths loaded from the file
    """
    filename = __file__.replace("crls.py", "data/crl2_focal_lengths.json")
 
    with open(filename, 'r') as json_file:
        mid_crl2_flengths = json.load(json_file)
    return mid_crl2_flengths


if __name__ == '__main__':

    # Generate all possible combinations of indexes 2-9 (since 1 and 10 are not allowed)
    lens_indexes = [2, 3, 4, 5, 6, 7, 8, 9]
    all_combinations = calculate_all_combinations(lens_indexes)

    # Calculate focal lengths for all possible combinations
    focal_lengths = {}
    for combination in all_combinations:
        indexes_str = ''.join(map(str, combination))
        try:
            focal_length = calculate_combined_focal_length(indexes_str)
            focal_lengths[indexes_str] = focal_length
        except ValueError as e:
            print(f"Error for combination {indexes_str}: {e}")

    # Save the focal lengths to a JSON file
    json_filename = './crl2_focal_lengths.json'
    save_focal_lengths_to_json(focal_lengths, json_filename)

