# Сергей Подкорытов, 48-я когорта — Финальный проект. Инженер по тестированию плюс

# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

# Запрос на создание заказа
def create_new_order():
    # Сохранение результата запроса в переменную
    response = sender_stand_request.post_new_order(data.order_body)
    # Получение трек-номера
    track = response.json()["track"]
    return track

# Запрос на получение заказа по треку заказа
def get_data_order(track):
    # Сохранение результата запроса в переменную
    response = sender_stand_request.get_order_by_track(track)
    return response

# Проверяется, что по треку заказа можно получить данные о заказе.
def test_create_order_and_get_data_by_track():
    track = create_new_order()
    response = get_data_order(track)
    assert response.status_code == 200