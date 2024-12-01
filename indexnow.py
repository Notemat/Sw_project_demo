import requests


# Данные для IndexNow
data = {
    'host': 'yuzhnyjveter-sochi.ru',
    'key': '1234567890abcdef1234567890abcdef',
    'keyLocation': 'https://yuzhnyjveter-sochi.ru/indexnow-key.txt',
    'urlList': [
        'https://yuzhnyjveter-sochi.ru',
        'https://yuzhnyjveter-sochi.ru/grocery/eggs',
        'https://yuzhnyjveter-sochi.ru/grocery/flour',
        'https://yuzhnyjveter-sochi.ru/grocery/sugar',
        'https://yuzhnyjveter-sochi.ru/grocery/salt',
        'https://yuzhnyjveter-sochi.ru/grocery/canned',
        'https://yuzhnyjveter-sochi.ru/grocery/cereal',
        'https://yuzhnyjveter-sochi.ru/grocery/pasta',
        'https://yuzhnyjveter-sochi.ru/grocery/oil',
    ]
}

try:
    # Отправка POST-запроса
    response = requests.post('https://yandex.com/indexnow', json=data)

    # Проверка результата
    if response.status_code == 200 or response.status_code == 202:
        print('Запрос успешно отправлен!')
        print('Ответ от сервера:', response.json())
    else:
        print(f'Ошибка: Код {response.status_code}')
        print(response.text)

except Exception as e:
    print('Произошла ошибка:', str(e))
