# Questions - https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md

"""
Complexities:

array = [2200, 2350, 2600, 2130, 2190]

1. Look-up by index - Constant O(1)
    => array[1]
    
2. Look-up by Value - Linear O(n)
    => for i in range(len(array)):
        if array[i] == 2350:
            return i

3. Traverse the array (like print all elements) - Linear O(n)
    => for arr in array:
        print(arr)

4. Insert to / Remove from an array at a specific index - Linear O(n)
    => Because, these operations needs to update the following items' position
"""

expenses = [2200, 2350, 2600, 2130, 2190]

# 1
extraDollarsSpentInFeb = expenses[1] - expenses[0]
print('Extra dollars spent in Feb month ', extraDollarsSpentInFeb)

# 2
quarterTotalExpenses = expenses[0] + expenses[1] + expenses[2]
print('Total expenses of first quarter ', quarterTotalExpenses)

# 3
hasSpent2000Dollars = 2000 in expenses
print('Did we spent exactly 2000 dollars in any of the month ', hasSpent2000Dollars)

# 4
expenses.append(1980)
print('Added june month expenses ', expenses)

# 5
expenses[3] = expenses[3] - 200
print('Updated april month expenses ', expenses)
