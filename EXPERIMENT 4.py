#Experiment 4
# Calculate the nth Fibonacci number efficiently

# Function to calculate the nth Fibonacci number
def fibonacci_iterative(n):

    # If n is 0
    if n == 0:
        return 0

    # If n is 1
    elif n == 1:
        return 1

    # Initialize the first two Fibonacci numbers
    a, b = 0, 1

    # Calculate Fibonacci number from 2 to n
    for _ in range(2, n + 1):

        # Add previous two numbers
        c = a + b

        # Move b to a
        a = b

        # Move c to b
        b = c

    # Return the nth Fibonacci number
    return b


# Take input from the user
n = int(input("Enter the value of n: "))

# Calculate and display the result
result = fibonacci_iterative(n)

print("Fibonacci number is:", result)