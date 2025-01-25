def split_bill():
    total_bill = float(input("Enter the total bill amount: "))
    num_people = int(input("Enter the number of people: "))
    tip_percentage = float(input("Enter the tip percentage: "))
    tip_amount = total_bill * (tip_percentage / 100)
    total_amount = total_bill + tip_amount
    amount_per_person = total_amount / num_people
    print(f"Each person has to pay: {amount_per_person}")

split_bill()
