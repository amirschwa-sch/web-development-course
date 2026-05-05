import requests

BASE_URL = "http://127.0.0.1:5000/students"
student = {"id": 3, "name": "Eldar Bakshi" , "age": 42}
res = requests.put(BASE_URL, json=student)

print(res.status_code)
print(res.reason)
print(res.json())
