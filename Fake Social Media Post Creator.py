import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

data = response.json()
print(data)


# def craete_post():
#     title = input('Enter Title : ')
#     body = input("Enter Body ; ")
#     userid = int(input("Enter UserID : "))
#     dict_post={
#         "title":title,
#         "body":body,
#         "userId":userid
#     }

#     response = requests.post(url,json=dict_post)
#     data = response.json()
#     print('POST CREATED !!')
#     print("Title: ",data["title"])
#     print("Body: ",data["body"])
#     print('User ID:',data["userId"])
#     print('Generated ID: ',data['id'])



# while True:
#     print('1.CREATE POST')
#     print('2.EXIT')
#     user = int(input('Enter option: '))
#     if user==1:
#         craete_post()
#     elif user==2:
#         break


