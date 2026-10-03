# Импортируем модуль configuration, он содержит настройки подключения и путь к документации
import configuration
# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
import requests
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

# Создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
                         json=body,
                         headers=data.headers)

# Получение данных о заказе по трек-номеру
def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_DATA_ORDER,
                        params={"t":track})