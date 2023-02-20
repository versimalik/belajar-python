products = [('diapers', 10.00), ('peanuts', 5.00), ('butter', 6.25), ('cheese', 
    3.00), ('milk', 3.5), ('yogurt', 1.99), ('eggs', 4.5), ('bread', 4), 
('shrimp', 2.5), ('coffee', 1.5)]

money = 50
menu = ('buy', 'return', 'quit')
cartList = []

def buyProduct(product, price):
    global money
    money = money - price
    cartList.append(product)
    print(f"Your cart list = {cartList}")
    print(f"Your current money = {money}")

def returnProduct(product, price):
    global money
    money = money + price
    cartList.remove(product)
    print(f"Your cart list = {cartList}")
    print(f"Your current money = {money}")

while menu != 'quit':

    for product in products:
        product_name = product[0].capitalize()
        product_price = product[1]
        print(f"{product_name} = {product_price}")

    menu = input("Do you want to buy, return or quit? ")

    if menu == 'buy':
        item = input("What do you want to buy? ") # coffee
        for product in products:
            if product[0] == item:
                confirm = input(f"Are you sure want to buy {product[0]} for {product[1]}? (Y/N) ")
                if confirm == "y":
                    buyProduct(product,product[1])
                elif confirm == "n":
                    print("You can buy another product")

    elif menu == 'return':
        item = input("What do you want to return? ")
        for product in cartList:
            if product[0] == item:
                confirm = input(f"Are you sure want to return {product[0]}? (Y/N) ")
                if confirm == 'y':
                    returnProduct(product,product[1])

else:
    print("Thank you for shopping!")