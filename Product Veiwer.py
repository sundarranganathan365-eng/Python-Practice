import requests

url = "https://fakestoreapi.com/products"

response = requests.get(url)

data = response.json()



def show_products():
    for products in data:
        print("Name :",products["title"],"|","Price : ",products["price"])

def expensive_products():
    print("***EXPENSIVE PRODUCTS***")
    for products in data :
        if products["price"]>500:
            
            print("Name :",products["title"],"|","Price : ",products["price"])

def range_products():
    user = int(input("Starting Price Range : "))
    user1=int(input("Ending Price Range : "))
    for products in data:
        if products["price"]>user and products["price"]<user1:
            print("Name :",products["title"],"|","Price : ",products["price"])
    
def avg_products():
    total=0
    for products in data:
        total = total + int(products["price"])
        
    avrage = total /len(data)
    print(avrage)


def serach_products():
    user = input("SERACH : ")
    cap = user.capitalize
    found = False
    for products in data:
        if user in products["title"]:
            print("Name :",products["title"],"|","Price : ",products["price"])
            found= True
    if found==False:
        print("out of stock")
            


while True:
    print("*****MENU*****")
    print("1.SHOW PRODUCTS")
    print("2.SHOW EXPENSIVE PRODUCT")
    print("3.PRICE RANGE")
    print("4.AVERAGE PRICE OF PRODUCT")
    print("5.SEARCH PRODUCTS")
    print("6.EXIT")
    user  = int(input("Enter Options; "))
    if user==1:
        show_products()
    elif user == 2:
        expensive_products()
    elif user == 3:
        range_products()
    elif user ==4:
        avg_products()
    elif user ==5:
        serach_products()
    elif user==6:
        break
    else:
        print("Invalid options")



