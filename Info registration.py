users = []

def add_user():
    name = input("Enter Name : ")
    city = input("Enter City : ")
    Skill1 = input("Enter skill1 : ")
    skill2 = input("Enter skill2 : ")
    skill = (Skill1,skill2)
   

  
    
    data ={
        "name":name,
        "city":city,
        "skills":skill,
       
    }
    users.append(data)
    

def show_user():
    for user in users:
        print("Name : ",user ["name"],"City : ",user["city"],"Skills : ",user["skills"])


def show_unique():
    skill1=set()
    for user in users:
        for skill in user["skills"]:
            skill1.add(skill)
    print(skill1)
  
        

    


while True:
    print("*****MENU*****")
    print("1.Add User")
    print("2.Show User")
    print("3.Show Unique Skils")
    print("4.Exit")
    user = int(input("Enter Your Choices : "))
    if user ==1:
        add_user()
    elif user == 2:
        show_user()
    elif user == 3:
        show_unique()
    elif user == 4:
        break
    else:
        print("invalid Input!!")
    
   