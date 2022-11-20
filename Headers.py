import requests

headers = {"some_header":"123"}
response = requests.post("https://playground.learnqa.ru/api/show_all_headers")

print(response.text)
print(response.headers)