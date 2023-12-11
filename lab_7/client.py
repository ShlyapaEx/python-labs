import socket
import json


def send_message_to_server(user_mail, message):
    HOST = '127.0.0.1'
    PORT = 50007
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(json.dumps({"user_mail": user_mail,
                  "message": message}, indent=2).encode('utf-8'))
        data = s.recv(1024)
        return data


def main():
    while True:
        user_mail = input("Введите E-mail получателя: ")
        message = input("Введите сообщение: ")
        # user_mail = "musha742@gmail.com"
        # message = "test"
        response = send_message_to_server(user_mail, message).decode("utf-8")
        if response == "ok":
            break
        else:
            print(f"Ошибка: {response}")


if __name__ == "__main__":
    main()
