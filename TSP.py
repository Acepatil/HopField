import itertools
import random
import math

def optimize_route_configuration(route_combinations, initial_seed, connection_matrix):
    minimum_energy = float("inf")
    optimal_route = []
    iteration_tracker = initial_seed
    optimization_active = 1
    
    while optimization_active:
        current_energy = 0
        for point_a in range(4):
            for point_b in range(4):
                for point_c in range(4):
                    adjusted_index = -1 if point_c == 3 else point_c
                    current_energy += 0.5 * (
                        connection_matrix[point_a][point_b] * 
                        route_combinations[iteration_tracker][point_a][point_c] * 
                        route_combinations[iteration_tracker][point_b][adjusted_index+1]
                    )
        
        print(f"Energy for route: {route_combinations[iteration_tracker]} is: {current_energy}")
        
        if current_energy <= minimum_energy:
            minimum_energy = current_energy
            optimal_route = route_combinations[iteration_tracker]
        
        if iteration_tracker < len(route_combinations) - 1:
            iteration_tracker += 1
        else:
            iteration_tracker = 0
        
        if iteration_tracker == initial_seed:
            optimization_active = 0
        
        current_energy = 0
    
    return optimal_route

def main():
    base_routes = [
        [0, 0, 0, 1], 
        [0, 1, 0, 0], 
        [0, 0, 1, 0], 
        [1, 0, 0, 0]
    ]
    
    route_permutations = list(itertools.permutations(base_routes))
    
    connection_matrix = [
        [0, 1, math.sqrt(2), 1],
        [1, 0, 1, math.sqrt(2)],
        [math.sqrt(2), 1, 0, 1],
        [1, math.sqrt(2), 1, 0]
    ]
    
    route_seed = random.randint(0, len(route_permutations) - 1)
    
    print("Connection Points: (0,0), (0,1), (1,0), (1,1)")
    
    optimized_path = optimize_route_configuration(
        route_permutations, 
        route_seed, 
        connection_matrix
    )
    
    print("Optimized Route Configuration:", optimized_path)

if _name_ == "_main_":
    main()
