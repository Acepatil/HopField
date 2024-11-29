import random
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

