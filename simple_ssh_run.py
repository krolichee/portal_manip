import os
from time import sleep

import paramiko

from  ssh_params import *

import sys

from pycparser.c_ast import While


def main():
    # Создание SSH-клиента
    ssh = paramiko.SSHClient()

    # Автоматическое добавление сервера в известные хосты
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def check_and_print_recv(channel):
        while True:
            if channel.recv_ready():  # Если есть данные для чтения
                output = channel.recv(1024).decode('utf-8')
                print(output, end='')
            else:
                break

    try:
        # Подключение к серверу
        ssh.connect(hostname, port, username, password)

        # Создание интерактивной shell-сессии
        channel = ssh.invoke_shell()



        print("Подключение установлено. Вводите команды (или 'exit' для выхода).")
        sleep(1)
        check_and_print_recv(channel)

        #channel.send("cd /..\n")
        channel.send("python3 1/script.py\n")
        sleep(1)
        check_and_print_recv(channel)
        # Чтение ввода пользователя
        while True:
            # Чтение ввода пользователя
            # command = input(f"{username}@{hostname}:\\~$ ")
            #
            # # Отправка команды на сервер
            # channel.send(command + "\n")
            #
            # # Выход, если пользователь ввел 'exit'
            # if command.strip() == 'exit':
            #     break

            # Чтение вывода от сервера
            sleep(1)
            check_and_print_recv(channel)


    finally:
        # Закрытие соединения
        ssh.close()
        print("\nСоединение закрыто.")
