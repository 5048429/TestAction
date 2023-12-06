# test_knapsack.py
import sys

sys.path.append(".")

from src.knapsack import knapsack_01

def test_knapsack_01():
    # Test Case 1
    values1 = [60, 100, 120]
    weights1 = [10, 20, 30]
    capacity1 = 50
    max_value1, selected_items1 = knapsack_01(values1, weights1, capacity1)
    assert max_value1 == 220
    assert selected_items1 == [1, 2]

    # Test Case 2
    values2 = [30, 40, 50, 10, 20]
    weights2 = [5, 10, 15, 2, 3]
    capacity2 = 10
    max_value2, selected_items2 = knapsack_01(values2, weights2, capacity2)
    assert max_value2 == 60
    assert selected_items2 == [0, 3, 4]

    # Test Case 3
    values3 = [10, 20, 30]
    weights3 = [1, 1, 1]
    capacity3 = 2
    max_value3, selected_items3 = knapsack_01(values3, weights3, capacity3)
    assert max_value3 == 50
    assert selected_items3 == [1, 2]