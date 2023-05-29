import httpx

payload = {'email': 'shisastore@protonmail.com', 'password': 'Grzesio1'}

res = httpx.post('http://comp-api:8000/api/users/token/', data=payload)
print(res.text)