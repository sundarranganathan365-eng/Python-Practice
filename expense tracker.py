
expense = []
def add_expense():
    title = input('Enter Title : ')
    amount = int(input("Enter the amount : "))
    category = input("Enter Category : ")
    month = input("Enter Month : ")
    dict_tracker = {
        "title":title,
        "amount":amount,
        "category":category,
        "month":month
    }
    expense.append(dict_tracker)

def show_expense():
    for expenses in expense
    print("Title:",expenses["title"],"|","Amount:",expenses["amount"],"|","Category:",expenses["category"],"|","Month:",expense["month"])


while True:
    print("*****MENU*****")
    print("1.ADD EXPENSES!")
    print("2.SHOW EXPENSES!")
    print("3.EXIT")
    user=int(input("CHOOSE OPTIONS:"))
    if user ==1:
        add_expense()
    elif user==2:
        show_expense()
    elif user ==3:
        break
    else:
        print("CHOOSE CORRECT OPTION/TRY AGAIN!!")
