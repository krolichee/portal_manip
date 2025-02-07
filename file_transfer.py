import paramiko
from  ssh_params import *

def main(local_path = 'rainbow.py'):
    # Создание SSH-клиента
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Подключение к серверу
        ssh.connect(hostname, port, username, password)

        # Создание SFTP-сессии
        sftp = ssh.open_sftp()
        # Загрузка файла на сервер

        remote_path = '1/script.py'
        sftp.put(local_path, remote_path)

        # Скачивание файла с сервера
        sftp.get(remote_path, local_path)

        # Закрытие SFTP-сессии
        sftp.close()

    finally:
        # Закрытие SSH-соединения
        ssh.close()

