numbers = []

for i in range(6):
    num = int(input("Enter number {i + 1}: "))
    numbers.append(num)

count = 0
for num in numbers:
    if num > 0:
        count += 1

print("The numbers entered are:", numbers)
print("There are", count, "positive numbers.")