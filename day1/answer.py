from collections import Counter

first_column = []
second_column = []

# PART 1
with open("input.txt", "r") as file:
    for line in file:
        numbers = line.strip().split()
        first_column.append(int(numbers[0]))
        second_column.append(int(numbers[1]))

first_column.sort()
second_column.sort()

total = 0
for i in range(len(first_column)):
    total += abs(first_column[i] - second_column[i])

print(total)

# PART 2
second_count = Counter(second_column)

similarity_score = 0
for num in first_column:
    similarity_score += num*second_count[num]

print(similarity_score)