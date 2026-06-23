carts=[]
def add_product():
    product_name = input('Enter Product Name : ')
    product_price = int(input("Enter Price : "))
    product_cato1 = input("Enter Category :  ")
    product_cato2 = input("Enter Category : ") 
    category=(product_cato1,product_cato2)
    store={
        "name":product_name,
        "price":product_price,
        "cato1":category
    }
    carts.append(store)


def show_product():
    for cart in carts:
        print("Product : ",cart["name"],"|","Price : ",cart["price"],"|","Category : ",cart["cato1"])

def total_price():
    total = 0
    for cart in carts:
        total =  total + cart["price"]
    print("Total Price :",total,"/-")
def expensive():
    for cart in carts:
        if cart["price"]>=1000: 
            print(cart["name"])

def unquie_cato():
    unquie=set()

    for cart in carts:
        for cato in cart["cato1"]:
            unquie.add(cato)
    print(unquie)


while True:
    print('*****MENU*****')
    print("1.ADD PRODUCT")
    print("2.SHOW PRODUCT")
    print("3.TOTAL PRICE")
    print("4.EXPENSIVE PRODUCTS")
    print("5.UNQUIE CATEGORY")
    print("6.EXITS")
    user = int(input("Enter Choices"))

    if user ==1:
        add_product()
    elif user==2:
        show_product()
    elif user ==3:
        total_price()
    elif user==4:
        expensive()
    elif user==5:
        unquie_cato()
    elif user == 6:
        break
    else:
        print("Invalid options")





