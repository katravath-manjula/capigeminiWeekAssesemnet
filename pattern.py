def generate_pattern(n, reverse=False):
    if reverse:
      
        for i in range(n, 0, -1):
            print("*" * i)
    else:
       
        for i in range(1, n + 1):
            print("*" * i)

n = int(input("Enter the number of rows: "))
reverse_option = input("Do you want to print the pattern in reverse? (yes/no): ")

if reverse_option == "yes":
    generate_pattern(n, reverse=True)
else:
    generate_pattern(n)
