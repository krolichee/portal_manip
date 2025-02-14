import json
import tkinter as tk
import requests



def send_value_to_server(value):
    # URL сервера, на который отправляется запрос
    url = "http://localhost:8000/"

    # Параметры запроса (в данном случае передаем значение ползунка)
    payload = {'y': str(value)}

    try:
        # Отправляем POST-запрос на сервер
        response = requests.post(url, data=json.dumps(payload))

        # Проверяем статус ответа
        if response.status_code == 200:
            print(f"Значение {value} успешно отправлено на сервер.")
        else:
            print(f"Ошибка при отправке значения: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка соединения с сервером: {e}")


def on_scale_move(value):
    # Функция, которая вызывается при перемещении ползунка
    send_value_to_server(value)


# Создаем главное окно
root = tk.Tk()
root.title("Ползунок с отправкой значения на сервер")

# Создаем ползунок (Scale)
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=on_scale_move)
scale.pack(pady=20, padx=20)

# Запускаем главный цикл обработки событий
root.mainloop()