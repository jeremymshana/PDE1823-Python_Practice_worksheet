shopping_list = []

for i in range(5):
    item = input("Enter item {i + 1}: ")
    shopping_list.append(item)

print("Your shopping list is:")

for item in shopping_list:
    print(item)