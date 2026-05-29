# calculate total bill using function
def calculate_total(prices):
    return sum(prices)


prices = []

# Ask number of items
num_items = int(input("How many items did the customer buy? "))

# Enter prices
for i in range(num_items):
    price = float(input("Enter price of item {i + 1}: "))
    prices.append(price)

# Calculate total
original_total = calculate_total(prices)

# Apply discount
if original_total > 1000:
    discount = original_total * 0.10
else:
    discount = 0

final_total = original_total - discount

# show results
print("Original total: Rs", original_total)
print("Discount: Rs", discount)
print("Final amount to pay: Rs", final_total)