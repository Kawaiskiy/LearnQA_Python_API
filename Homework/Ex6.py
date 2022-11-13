import requests

response = requests.post("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

responseCount = len(response.history)


print(f"Кол-во редиректов: {responseCount}")
print(f"Конечный url:{response.url}")