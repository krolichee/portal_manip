import os
from time import sleep

import paramiko
import sys

# Параметры подключения
hostname = 'ev3dev'
port = 22
username = 'robot'
password = 'maker'

# Создание SSH-клиента
ssh = paramiko.SSHClient()

# Автоматическое добавление сервера в известные хосты
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Подключение к серверу
    ssh.connect(hostname, port, username, password)

    # Создание интерактивной shell-сессии
    channel = ssh.invoke_shell()



    print("Подключение установлено. Вводите команды (или 'exit' для выхода).")
    sleep(1)
    while True:
        if channel.recv_ready():  # Если есть данные для чтения
            output = channel.recv(1024).decode('utf-8')
            print(output, end='')
        else:
            break

    print("команда 1")

    channel.send("ls\n")
    while True:
        if channel.recv_ready():  # Если есть данные для чтения
            output = channel.recv(1024).decode('utf-8')
            print(output, end='')
        else:
            break
    channel.send("cd /..\n")
    channel.send("python3 /home/robot/1/script.py\n")
    while True:
        if channel.recv_ready():  # Если есть данные для чтения
            output = channel.recv(1024).decode('utf-8')
            print(output, end='')
        else:
            break
        command = input(f"{username}@{hostname}:~$ ")

        # Отправка команды на сервер
        channel.send(command + "\n")

        # Выход, если пользователь ввел 'exit'
        if command.strip() == 'exit':
            break

    output = channel.recv(1024).decode('utf-8')
    print(output, end='')

    channel.send("hohoho\n")
    sleep(5)
    while True:
        while True:
            if channel.recv_ready():  # Если есть данные для чтения
                output = channel.recv(1024).decode('utf-8')
                print(output, end='')
            else:
                break
        # Чтение ввода пользователя
        command = input(f"{username}@{hostname}:~$ ")

        # Отправка команды на сервер
        channel.send(command + "\n")

        # Выход, если пользователь ввел 'exit'
        if command.strip() == 'exit':
            break

        # Чтение вывода от сервера

finally:
    # Закрытие соединения
    ssh.close()
    print("\nСоединение закрыто.")