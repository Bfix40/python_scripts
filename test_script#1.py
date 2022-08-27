from urllib import response
import requests

login = 'http://127.0.0.1:8000/v1/login'
list_of_users = requests.get('http://127.0.0.1:8000/v1/users')
current_user = requests.get('http://127.0.0.1:8000/v1/user')

data = {'email': 'bfix07@gmail.com','password':'4038'}

post = requests.post(url= login, data= data)
req = post.json()

print(req)
print(list_of_users.json())
print(current_user.json())