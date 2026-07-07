import numpy as np
def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    top_k = recommended[:k]
    
    # Convert relevant items to a set for O(1) fast lookup
    relevant_set = set(relevant)
    
    # Count how many items in top_k appear in the relevant set (hits)
    hits = sum([1 for item in top_k if item in relevant_set])
    
    # Hint 2: Calculate precision and recall
    precision = hits / k
    
    # Handle edge case where relevant list might be empty to prevent DivisionByZero
    recall = hits / (len(relevant)+10e-16)
    
    # Return them as a two-element list
    return [precision, recall]