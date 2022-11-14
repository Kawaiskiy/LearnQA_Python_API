import requests

url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD']

for method in methods:
    for method_value in methods:
        if method == 'GET':
            response = requests.request(method, url, params={'method': method_value})
        else:
            response = requests.request(method, url, data={'method': method_value})
        print(f'Ответ на Ваш запрос {method}, с параметром {method_value}: {response.text}')