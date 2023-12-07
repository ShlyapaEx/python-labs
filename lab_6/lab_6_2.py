# Выполните поиск содержимого текущей директории (включая поддиректории) и
# найдите все файлы с расширением txt в которых есть ключевое слово key.
# Выполните задание в одном и в нескольких потоках.

import os
from concurrent.futures import ThreadPoolExecutor
from lab_6_1 import timing


def file_has_key(filename: str):
    if filename.endswith(".txt"):
        with open(filename) as f:
            file_text = f.read()
            if "key" in file_text:
                return filename
    return None


@timing
def one_thread_search():
    found_files = []

    for root, dirs, files in os.walk('.'):
        for filename in files:
            result = file_has_key(os.path.join(root, filename))
            if result:
                found_files.append(result)
    return found_files


@timing
def many_thread_search():
    results = []
    transformed_filenames = []
    for root, dirs, files in os.walk('.'):
        for filename in files:
            transformed_filenames.append(os.path.join(root, filename))

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(file_has_key, transformed_filenames)
    return list(filter(lambda file: file is not None, results))


def main():
    one_thread_search()
    many_thread_search()


if __name__ == "__main__":
    main()
