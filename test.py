import requests
import base64

Base_url="http://127.0.0.1:5000/"

data={"email":"demo@gmail.com","password":"demo@1234"}

response=requests.get(Base_url+"Login",data=data)
print(response.json())

