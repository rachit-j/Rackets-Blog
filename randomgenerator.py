import random

# Generating a list of 1000 random numbers
numbers = [random.randint(1, 500) for _ in range(10000)]

# Converting the list to a comma-separated string
numbers_str = ",".join(map(str, numbers))

# Writing to a file
with open("random_numbers.txt", 'w') as file:
    file.write(numbers_str)
