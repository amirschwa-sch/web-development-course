import requests

BASE_URL = "http://127.0.0.1:5000/students"
res = requests.delete(BASE_URL+"/6")

print(res.status_code)
print(res.reason)
print(res.json())
