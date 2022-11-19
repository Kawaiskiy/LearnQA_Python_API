import requests
import time

url = 'https://playground.learnqa.ru/ajax/api/longtime_job'

tokenValue = ['']

responseFirst = requests.get(url)
data = responseFirst.json()
tokenValue = data['token']
seconds = data['seconds']

responseSecond = requests.get(url, params={'token': tokenValue})
dataSecond = responseSecond.json()
status = dataSecond['status']

if status == 'Job is NOT ready':
    time.sleep(seconds)
    responseWaiting = requests.get(url, params={'token': tokenValue})
    dataWaiting = responseWaiting.json()
    result = dataWaiting['result']
    status = dataWaiting['status']
    print(f'Статус обработки Вашего запроса "{status}", Ваш результат:{result}')
else:
    print(f'Текущий статус {status}, не доступен для обработки')

