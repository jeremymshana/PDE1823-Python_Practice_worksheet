def calculate_area(length, width):
    area = length * width
    return area

length = float(input("Enter length: "))
width = float(input("Enter width: "))

result = calculate_area(length, width)

print("The area of the rectangle is:", result)