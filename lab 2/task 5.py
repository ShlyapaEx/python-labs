import os


BASE_PATH = 'lab 2/files/example'


def find_in_names(filter: str):
    counter = 0
    file_names = os.listdir(BASE_PATH)

    for file_name in file_names:
        if filter in file_name:
            counter += 1

    return counter


def main():
    filter = 'il'
    print(find_in_names(filter))


if __name__ == '__main__':
    main()
