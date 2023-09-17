import os
import shutil

BASE_PATH = 'lab 2/files/example'


def generate_n_files(n):
    shutil.rmtree(BASE_PATH, ignore_errors=True)
    os.mkdir(BASE_PATH)

    for i in range(n):
        with open(f'{BASE_PATH}/file_{i + 1}', 'w'):
            pass


def main():
    print(generate_n_files(1000))


if __name__ == '__main__':
    main()
