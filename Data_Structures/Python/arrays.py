# Questions - https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md

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
