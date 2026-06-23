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

while True:


    user = int(input("Enter option"))
    if user==1:
        add_students()
    elif user==2:
        show_students()


    