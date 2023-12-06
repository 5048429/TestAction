import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.knapsack import knapsack_01

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
max_value, selected_items = knapsack_01(values, weights, capacity)

assert max_value == 220, "The max_value is wrong"
assert selected_items == [1, 2], "The selected_items are wrong"
