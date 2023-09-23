import configuration
import requests
import data

#POST-запрос на создание нового заказа
def post_new_order(body_order):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body_order,
                         headers=data.headers)

#Получение трека номера заказа
def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                         params={"t":track},
                         headers=data.headers)