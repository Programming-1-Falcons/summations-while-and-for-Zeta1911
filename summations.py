# summation.py using for loop

# Ask the user for a number
num = int(input("Enter a number: "))

# Initialize sum variable
total_sum = 0

# Use a for loop to calculate the sum from 1 to the entered number
for i in range(1, num + 1):
    total_sum += i

# Print the result
print(f"The sum of numbers from 1 to {num} is {total_sum}.")


# summation.py using while loop

# Ask the user for a number
num = int(input("Enter a number: "))

# Initialize sum and counter variables
total_sum = 0
i = 1

# Use a while loop to calculate the sum from 1 to the entered number
while i <= num:
    total_sum += i
    i += 1

# Print the result
print(f"The sum of numbers from 1 to {num} is {total_sum}.")
