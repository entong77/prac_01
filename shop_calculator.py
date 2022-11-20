DISCOUNT = 0.1
DISCOUNT_STANDARD = 100
LOWEST_VALUE = 0
total_price = 0

number = int(input("Number of items: "))
while number < LOWEST_VALUE:
    print("Invalid number of items!")
    number = int(input("Number of items: "))

for i in range(number):
    price = float(input("Price of item: "))
    while price < LOWEST_VALUE:
        print("Invalid price of items!")
        price = float(input("Price of item: "))
    total_price += price

    if total_price > DISCOUNT_STANDARD:
        total_price = total_price - total_price * DISCOUNT
print(f"Total price for {number} items is ${total_price:.2f}")