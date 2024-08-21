import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    with open("posts.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    print("Данные успешно сохранены в файл 'posts.json'.")
else:
    print(f"Ошибка получения данных: {response.status_code}")