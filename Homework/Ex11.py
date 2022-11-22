import requests


class TestEX11:

    def test_cookie(self):
        response = requests.post(
            "https://playground.learnqa.ru/api/homework_cookie"
        )
        print(response.cookies)

        assert response.cookies['HomeWork'] == 'hw_value', \
            f"Incorrect response cookie: {response.cookies['HomeWork']}"