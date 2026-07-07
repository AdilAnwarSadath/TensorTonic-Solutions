import numpy as np

def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    # Write code here
    n = len(values)
    if n == 0:
        return []
        
    # 1. Sort the indices by their corresponding values
    sorted_indices = sorted(range(n), key=lambda x: values[x])
    
    # Initialize an array to store the final ranks
    ranks = [0.0] * n
    
    i = 0
    while i < n:
        j = i
        # Find the range of elements that have the exact same value
        while j < n and values[sorted_indices[j]] == values[sorted_indices[i]]:
            j += 1
            
        # 1-based positions in the sorted list
        start_pos = i + 1
        end_pos = j
        
        # Calculate the average rank for this group (as per Hint 2)
        avg_rank = (start_pos + end_pos) / 2.0
        
        # Assign this average rank to all indices in this duplicate group
        for k in range(i, j):
            ranks[sorted_indices[k]] = avg_rank
            
        # Move the pointer to the next unique value group
        i = j
        
    return ranks