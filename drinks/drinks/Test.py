import requests
import json
# Get all method
response = requests.get('http://127.0.0.1:8000/drinks')
print(response.json())

#adding a new data into the database
# d={'name':'test1','description':'test description'}
# response = requests.post('http://127.0.0.1:8000/drinks/',data=d)
# print(response.json())

id = int(input())
# response=requests.get('http://127.0.0.1:8000/drinks/'+str(id))
# if response.status_code==200:
#     print(response.json())
# d={'name':'testput','description':'testput description'}
# response = requests.put('http://127.0.0.1:8000/drinks/'+str(id),data =d)
# if response.status_code==200:
#     print(response.json())


