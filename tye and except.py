
    
try:
        user = int(input('Enter the marks: '))
        
        if user>=90 and user<100:
            print("Grade : A")
        elif user<=89 and user>=75:
            print('Grade : B')
        elif user<=74 and user>=60:
            print("Grade : C")
        elif user>=36 and user<=59 and user>0:
            print("Grade : D")
        elif user>100:
            print("Marks cannot be above 100")
        elif user<0:
            print("Marks cannot be negative")
        else:
            print("Fail")
except TypeError:
        print("Invaild Number Entered")
except ValueError:
     print("invaild number ")
    
