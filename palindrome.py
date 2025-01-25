while True:
    value = input("Enter a value to check for palindrome (or type 'exit' to quit): ")
    if value == 'exit':
        break
    reversed_value = ""
    for char in value:
        reversed_value = char + reversed_value
    if value == reversed_value:
        print("Palindrome")
    else:
        print("Not a palindrome")
