import itertools
import random
import functools
import operator

def compute_board_energy(board_configuration):
    def calculate_dimension_energy(dimension_data):
        # Use reduce to sum the dimension, then calculate energy
        dimension_sum = functools.reduce(operator.add, dimension_data)
        return (dimension_sum - 1) ** 2  # Squared penalty for extra queens in the same row/column
    
    # Calculate row energy
    row_energy = sum(
        calculate_dimension_energy(row) 
        for row in board_configuration
    )
    
    # Calculate column energy
    column_energy = sum(
        calculate_dimension_energy([row[col] for row in board_configuration])
        for col in range(len(board_configuration))
    )
    
    return row_energy + column_energy

def find_valid_configuration():
    base_states = [
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1]
    ]
    
    # Generate all permutations of the base states
    board_permutations = list(itertools.permutations(base_states))
    
    # Shuffle the permutations for randomized search
    random.shuffle(board_permutations)
    
    # Save the initial shuffled configuration
    initial_configuration = board_permutations.copy()
    
    # Recursive search for a valid configuration
    def search_configurations(configurations):
        # Base case: No configurations left
        if not configurations:
            return None
        
        # Check the first configuration
        current_config = configurations[0]
        if compute_board_energy(current_config) == 0:
            return current_config  # Return valid configuration
        
        # Recursive call with remaining configurations
        return search_configurations(configurations[1:])
    
    valid_configuration = search_configurations(board_permutations)
    return initial_configuration, valid_configuration

def main():
    initial_configurations, solution = find_valid_configuration()
    
    print("Initial shuffled configurations (showing first 5):")
    for i, config in enumerate(initial_configurations[:5]):
        print(f"Configuration {i + 1}:")
        for row in config:
            print(row)
        print()

    if solution:
        print("Final valid configuration:")
        for row in solution:
            print(row)
    else:
        print("No valid configuration found.")

if _name_ == "_main_":
    main()
