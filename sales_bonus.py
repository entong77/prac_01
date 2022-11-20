JUNIOR_RATE = 0.1
SENIOR_RATE = 0.15
VALUE_OF_SALES = 1000

user_sales = float(input("Enter sales: $"))
while user_sales >= 0:
    if user_sales < VALUE_OF_SALES:
        user_bonus = user_sales * JUNIOR_RATE
        user_sales = float(input("Enter sales: $"))
    elif user_sales >= VALUE_OF_SALES:
        user_bonus = user_sales * SENIOR_RATE
        print(f"Bonus: {user_bonus:.2f} ")
        user_sales = float(input("Enter sales: $"))

else:
    print("Invalid")
    user_sales = float(input("Enter sales: $"))