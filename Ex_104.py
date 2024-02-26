import json
import requests

url = "https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=36bda7f634b745ba6b0ea53aced6728b"
response = requests.get(url)


if response.status_code == 200:

    data = response.json()

    # Записываем данные в файл pack.json
    with open('pack.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
else:
    print("Ошибка при получении данных:", response.status_code)
