def add_students():
    stud_name = input("Enter Student Name: ")
    stud_mark = int(input("Enter Marks: "))
    file = open("student.txt","a")
    file.write(stud_name +","+ str(stud_mark) +"\n" )
    file.close()
    

def show_students():
    file = open("student.txt","r")
    data = file.readlines()
    for line in data :
        parts = line.strip().split(",")
        print("Name :",parts[0],"|","Marks :",parts[1])
    file.close()

def serach_student():
    user = input('Enter Name ; ')
    file = open("student.txt","r")
    data = file.readlines()
    found = False
    for line in data :
        parts = line.strip().split(",")
        if user == parts[0]:
            print("Name :",parts[0],"|","Marks :",parts[1])
            found= True
    if found == False:
                print("Invalid input")
    file.close()


def top_marks():
    file = open("student.txt","r")
    data = file.readlines()
    for line in data :
        parts = line.strip().split(",")
        if int(parts[1])>90 and int(parts[1])<100:
              print("Topper","|","Name :",parts[0],"|","Marks :",parts[1])
    file.close()

     
while True:


    user = int(input("Enter option"))
    if user==1:
        add_students()
    elif user==2:
        show_students()
    elif user ==3:
        serach_student()
    elif user ==4:
         top_marks()

    