salary = float(input("Enter your salary: "))
age = int(input("Enter your age: "))
credit_score = int(input("Enter your credit score: ")) 
if age < 18 or age > 60:
      print("Loan Rejected: Age must be between 18 and 60.")
else:
       print("loan approval")
if salary < 30000:
        print("Loan Rejected: Salary must be at least 30,000.")
else:
        print("loan approval")
        if credit_score < 650:
              print("Loan Rejected: Credit score must be 650 or above.")
        else:
              print("Loan Approved: You meet all the eligibility criteria.")

    
    