import requests

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)

data = response.json()

def show_all_todos():
    for datas in data:
        print("Title :",datas["title"],"|","Completed Task :",datas["completed"])

def show_completd_todos():
    for datas in data:
        if datas["completed"]==True:
            print("Title :",datas["title"],"|","Completed Task :",datas["completed"])
def show_pending_todos():
    for datas in data:
        if datas["completed"]==False:
            print("Title :",datas["title"],"|","Completed Task :",datas["completed"])
def total_completed_todos():
    total = 0
    for datas in data:
        if datas["completed"]==True:
            total= total +1
    print("Total TODOS Completed :",total)

def search_todo():
    user = input('Enter :')
    found = False
    for datas in data:
        if user  in datas['title']:
             print("Title :",datas["title"],"|","Completed Task :",datas["completed"])
             found=True
    if found==False:
        print("Invalid option try agian ")

def search_userid():
    user = int(input('Enter user ID :'))
    found = False
    for datas in data:
        if user  ==  datas["userId "]:
             print("Title :",datas["title"],"|","Completed Task :",datas["completed"])
             found=True
    if found==False:
        print("Invalid option try agian ")


while True :
    print("*****MENU*****")
    print("1.SHOW ALL TODOS")
    print("2.SHOW COMPLETED TODOS")
    print("3.SHOW PENDING TODOS")
    print("4.TOTAL COMPLETED TODOS")
    print("5.SEARCH TODO")
    print("6.SEARCH USERID")
    print("7.EXIT")
    user = int(input('Enter your options :'))
    if user == 1:
        show_all_todos()
    elif user ==2:
        show_completd_todos()
    elif user==3:
        show_pending_todos()
    elif user==4:
        total_completed_todos()
    elif user==5:
        search_todo()
    elif user==6:
        search_userid()
    elif user==7:
        break
    else:
        print('Invalid input Try agian')



            



            