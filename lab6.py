[1:42 PM, 11/29/2024] Pradumya Gaurav: import random
import numpy as np

class HopfieldNetwork:
    def _init_(self, num_neurons):
        self.num_neurons = num_neurons
        self.synaptic_weights = np.zeros((num_neurons, num_neurons))
    
    def fit(self, input_patterns):
        for pattern in input_patterns:
            for i in range(self.num_neurons):
                for j in range(i + 1, self.num_neurons):
                    self.synaptic_weights[i, j] += pattern[i] * pattern[j]
                    self.synaptic_weights[j, i] = self.synaptic_weights[i, j]
    
    def retrieve(self, noisy_input, iterations=5):
        current_state = noisy_input.copy()
        for _ in range(iterations):
            for i in range(self.num_neurons):
                net_input = np.dot(self.synaptic_weights[i], current_state)
                current_state[i] = 1 if net_input >= 0 else -1
        return current_state
    
    def print_pattern(self, pattern):
        for i in range(0, self.num_neurons, 10):
            print(' '.join(f'{x:2}' for x in pattern[i:i+10]))


grid_dim = 10 * 10

hopfield_network = HopfieldNetwork(grid_dim)

patterns = [
    [random.choice([-1, 1]) for _ in range(grid_dim)],
    [random.choice([-1, 1]) for _ in range(grid_dim)]
]

hopfield_network.fit(patterns)

noisy_input = patterns[0].copy()
noisy_input[:10] = [-x for x in noisy_input[:10]]

reconstructed_pattern = hopfield_network.retrieve(noisy_input)

print("Original Pattern:")
hopfield_network.print_pattern(patterns[0])

print("\nNoisy Input Pattern:")
hopfield_network.print_pattern(noisy_input)

print("\nReconstructed Pattern:")
hopfield_network.print_pattern(reconstructed_pattern)
[1:43 PM, 11/29/2024] Pradumya Gaurav: lab 6 Hopfield (in lab submission)
[1:44 PM, 11/29/2024] Pradumya Gaurav: import itertools
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
    main(
