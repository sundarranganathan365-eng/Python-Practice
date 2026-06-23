import requests

url = "https://jsonplaceholder.typicode.com/posts"
load = {
    "title": "Hello",
    "body": "My first post",
    "userId": 1
}

response = requests.post(url,json=load)


data = response.json()
print(data)

