class Product:

    def __init__(self, name, price, stock):

        self.name = name
        self.price = price
        self.stock = stock



    def display_product(self):

        print(
            f"{self.name} | Price: Rs {self.price} | Stock: {self.stock}"
        )



    def sell(self, quantity):

        if quantity <= self.stock:

            self.stock -= quantity

            total = quantity * self.price

            return total

        else:

            return -1




# Main Program

products = []


number_of_products = int(
    input("How many products do you want to enter? ")
)



for i in range(number_of_products):

    print("\nEnter product", i + 1)

    name = input("Enter product name: ")

    price = float(
        input("Enter price: ")
    )

    stock = int(
        input("Enter stock quantity: ")
    )


    product = Product(name, price, stock)

    products.append(product)



total_sales = 0



while True:

    print("\nShop Menu")
    print("1. Display products")
    print("2. Sell product")
    print("3. Exit")


    choice = int(input("Menu choice: "))



    if choice == 1:

        print("\nProduct List:")

        for i, product in enumerate(products):

            print(i + 1, end=". ")

            product.display_product()



    elif choice == 2:


        number = int(
            input("Enter product number to sell: ")
        )


        quantity = int(
            input("Enter quantity: ")
        )


        selected_product = products[number - 1]


        sale_amount = selected_product.sell(quantity)



        if sale_amount != -1:


            total_sales += sale_amount


            print("Sale successful.")

            print(
                "Amount for this sale: Rs",
                sale_amount
            )


            print(
                "Remaining stock for",
                selected_product.name,
                ":",
                selected_product.stock
            )


        else:

            print(
                "Not enough stock available for",
                selected_product.name
            )

            print(
                "Current stock:",
                selected_product.stock
            )



    elif choice == 3:


        print("\nTotal sales amount: Rs", total_sales)


        print("\nRemaining Stock:")


        for product in products:

            print(
                product.name,
                ":",
                product.stock,
                "left"
            )


        break



    else:

        print("Invalid option.")