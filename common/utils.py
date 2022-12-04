import json
import sys

sys.path.append('../')
from common.decos import log
from common.variables import *

'''
Функция приёма сообщений от удалённых компьютеров.
Принимает сообщения JSON, декодирует полученное сообщение
и проверяет что получен словарь.
:param client: сокет для передачи данных.
:return: словарь - сообщение.
'''


@log
def get_message(client):
    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    # if isinstance(encoded_response, bytes):
    json_response = encoded_response.decode(ENCODING)
    response = json.loads(json_response)
    if isinstance(response, dict):
        return response
    else:
        raise TypeError
    # else:
    #     raise IncorrectDataRecivedError

    '''
    Функция отправки словарей через сокет.
    Кодирует словарь в формат JSON и отправляет через сокет.
    :param sock: сокет для передачи
    :param message: словарь для передачи
    :return: ничего не возвращает
    '''


@log
def send_message(sock, message):
    # if not isinstance(message, dict):
    #     raise NonDictInputError
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)
