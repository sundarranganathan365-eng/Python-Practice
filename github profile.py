import requests
def enter_name():

    username = input("Enter Github Username : ")

    url ="https://api.github.com/users/" + username

    response = requests.get(url)

    data = response.json()
    
    print("Name : ",data["name"])
    print("Followers : ",data["followers"])
    print("Company : ",data["company"])
    print('Repos :',data["public_repos"])
    print("BIO : ",data["bio"])
    print('Account Type ; ',data["type"])



enter_name()





