
import requests

a = requests.get ('https://gorest.co.in/public/v1/users')
print (a.jason())

headers = (
        "Content-Type" : "application/json",
        "Authorization" : "Bearer5b950a5d5f91434c46612d15777b9ce7ebe9ab55876dd71c4ae08abab8b49c7a"
        )

data = '["name":"Fidaim", "gender":"male", "email":"fidaimahmeti1@gmail.com, "status":"active"]'

response = requests.post('https://gorest.co.in/public/v1/users', headers=headers, data=data)
print (response)

data = '["name":"ibaaa", "gender":"male", "email":"test.ib@gmail.com, "status":"active"]'

response = requests.post('https://gorest.co.in/public/v1/users', headers=headers, data=data)
print (response)

response = requests.delete ('https://gorest.co.in/public/v1/users', headers=headers, data=data)


