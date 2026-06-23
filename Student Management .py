students = []

def add_students():
    print("ADD STUDENT DETAIL!!")
    name = input("Enter Name :")
    marks = int(input("Enter Marks :"))
    dict_students ={
        "name":name,
        "mark":marks
    }
    students.append(dict_students)


def show_students():
    print("STUDENT DETAILS!!")
    for student in students :
        if student["mark"]>=90:
             print("Name :",student["name"],"|","Marks :",student["mark"],"|","Grade: A")
        elif student["mark"]>=70:
             print("Name :",student["name"],"|","Marks :",student["mark"],"|","Grade: B")
        elif student["mark"]>=35:
             print("Name :",student["name"],"|","Marks :",student["mark"],"|","Grade: C")
        else:
              print("Name :",student["name"],"|","Marks :",student["mark"],"|","Grade: Failed")


def search_student():
     user = input('Enter Student Name :')
     found = False
     for student in students :
          if student['name']== user:
                print("Name :",student["name"],"|","Marks :",student["mark"])
                found = True
            
     if found == False:
           print("After checking ALL students!! We DIDN'T FOUND !!!")
                
                        
def delete_students():
     user = input('Enter Student Name :')
     found = False
     for student in students :
          if student['name']== user:
                students.remove(student)
                print("Student Deleted !!")
                found = True
                break
            
     if found == False:
           print("After checking ALL students!! We DIDN'T FOUND !!!")            
               

def update_students():
     user = input('Enter Name :')
     update_mark = int(input('Enter new marks :'))
     found = False
     for student in students:
          if student["name"]== user:
              student["mark"] = update_mark
              print('Marks Updated!!')
              found = True
              break
     if found == False:
           print("After checking ALL students!! We DIDN'T FOUND !!!")   
          
         

while True:
     print("*****MENU*****")
     print("1.Add Students")
     print("2.Show Students")
     print("3.Search Student")
     print("4.Delete Student")
     print("5.Update Student")
     print("6.Exit")
     user = int(input("Enter Number :"))

     if user==1:
          add_students()
     elif user ==2:
          if len(students)==0:
               print("Noo Student Found !!")
          show_students()
     elif user == 3:
          search_student()
     elif user == 4:
          delete_students()
     elif user == 5:
          update_students()
    
     elif user ==6:
          
          print('thankyou')
          break
     else:
          print("invalid Input")




