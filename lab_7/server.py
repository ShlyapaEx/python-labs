import json
import socket
from smtplib import SMTP, SMTP_SSL
from my_pass import mail_password


def send_mail(user_mail, message):

    username = 'musha147@yandex.ru'
    with SMTP_SSL("smtp.yandex.ru", 465, timeout=5) as smtp:
        smtp.set_debuglevel(1)
        smtp.login(username, mail_password)
        try:
            smtp.sendmail(username, user_mail, message)
        except Exception as err:
            return repr(err)
    return "ok"


def basic_server():
    HOST = '127.0.0.1'
    PORT = 50007
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    mail_data = json.loads(data)
                    response = send_mail(
                        mail_data["user_mail"], mail_data["message"])
                    conn.sendall(response.encode("utf-8"))


def main():
    basic_server()


if __name__ == "__main__":
    main()
