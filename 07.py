student = []
def add_stud():
    name = input("Enter Name : ")
    mark = int(input("Enter Marks : "))
    dict_student ={
        "name":name,
        "marks":mark
    }
    student.append(dict_student)

def show_stud():
    for students in student:
        print('STUDENT DEATILS !!')
        print("Name : ",students["name"])
        print("Marks : ",students["marks"])
        if students["marks"] >= 90 :
            print("Student Grade : A ")
        elif students["marks"] >=70 :
            print("Student Grade : B ")
        elif students["marks"] >=50 :
            print("Student Grade : C ")
        elif students["marks"]>=35 :
            print("Student Grade : D")
        elif students["marks"] < 35:
            print("Student Grade : Failed!")
        print("-------------------")

def serach_stud():
    user = input("Enter Student Name : ")
    found = False
    for students in student :
        if students["name"] == user :
             found = True
             print("STUDENT FOUND !! ")
             print("Name : ",students["name"])
             print("Marks : ",students["marks"])
             if students["marks"] >= 90 :
                print("Student Grade : A ")
             elif students["marks"] >=70 :
                print("Student Grade : B ")
             elif students["marks"] >=50 :
                print("Student Grade : C ")
             elif students["marks"]>=35 :
                print("Student Grade : D")
             elif students["marks"] < 35:
                print("Student Grade : Failed!")
    if found == False :
         print("User Not Found")
             
                
            
    print("-------------------")

def update_stud():
    user = input("Enter Student Name : ")
    found = False 
    for students in student :
        if user == students["name"]:
            found = True 
            print("STUDENT FOUND")
            update_marks = int(input("Enter Updated Marks : "))
            students["marks"] = update_marks
            print("Marks Updated")
        
    if found == False:
        print("User Not Found ")

def delete_stud():
    user = input('Enter Student Name ; ')
    found = False
    for students in student :
        if user ==  students["name"]:
            found = True 
            print("Student Found and Deleted ! ")
            student.remove(students)
    if found == False:
        print("User Not found!")


while True :
    print('STUDENT MANAGEMENT SYSTEM !!')
    print("1.ADD STUDENTS")
    print('2.SHOW STUDENTS')
    print("3,SERACH STUDENT")
    print("4.UPDATE MARKS")
    print("5.DELETE STUDENT")
    print("6.EXIT")
    print('CHOOSE THE OPTION !')
    user = int(input('Enter option ; '))
    if user == 1:
        add_stud()
    elif user == 2: 
        show_stud()
    elif user ==3:
        serach_stud()
    elif user == 4:
        update_stud()
    elif user == 5:
        delete_stud()
    elif user == 6:
        break
    else:
        print("CHOOSE CORRECT OPTION!!")
    



