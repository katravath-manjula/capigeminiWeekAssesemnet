# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def prime_numbers_in_range(start, end):
    for num in range(start,end):
        if is_prime(num):
            print(num, end=" ")

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print(f"Prime numbers between {start} and {end}:")
prime_numbers_in_range(start, end)