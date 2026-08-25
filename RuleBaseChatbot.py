
import datetime
import time
name = input("Enter your name ")

presentHour = datetime.datetime.now().hour
if 5<= presentHour <= 11:
    print("Good Moring",name)
elif  11<= presentHour <= 17:
    print("Good afternoon",name )
elif 17<= presentHour <= 20:
    print("Good evening",name)
else:
    print("Good Night ",name )



print ("Namste!! form your Rule Based Chatbot ")
print("You can ask me basic question,Type 'bye 'to exit form bot")

#chatbot memory

responses = {
    "hello":"Hii welcome .How can I help you !!",
    "how are you ": "I am very fine .Thankyou !",
    "who are you ": "I am samrt AI Chatbot!!",
    "motivate me ": "keep going .every bug of your project makes you a become a better Developers",
    "happy":"Greate to hear that",
}


# function to get response of chatbot 
def getresponseofbot(userQuestion):
    userQuestion= userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
        
    return " Not availabe i will learn that soon "

#take input
while True:
    user_input = input("Please ask your Quetsion ! ")

    reply = getresponseofbot(user_input)
    print('Bot response :',reply)
    if "bye" in user_input.lower():
        break
