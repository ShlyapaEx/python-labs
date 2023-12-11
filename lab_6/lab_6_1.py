# Получите содержимое 10 сайтов. Выполните задание в одном и в нескольких потоках.
# Сравните результаты и время выполнения программы.

import threading
import requests
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        start = time()
        result = f(*args, *kwargs)
        end = time()
        print(
            f"func: {f.__name__} args:[{args}, {kwargs}] took: {end-start} sec")
        return result
    return wrap


sites = (
    "https://google.com",
    "https://yandex.ru",
    "https://orioks.miet.ru",
    "https://github.com",
    "https://codeberg.org",
    "https://wikipedia.org",
    "https://random.org",
    "https://github.com",
    "https://stackoverflow.com",
    "https://pypi.org",
)


def get_site_content(url):
    return requests.get(url).content


@timing
def one_thread_get():
    results = []
    for site in sites:
        results.append(get_site_content(site))
    return results


@timing
def threading_get():
    threads = []
    for site in sites:
        thread = threading.Thread(target=get_site_content, args=(site,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


@timing
def thread_pool_get():
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(get_site_content, sites)

    return list(results)


def main():
    one_thread_get()  # 3.2, 2.7, 3.4, 3.1, 3.3, 2.9 | 4
    thread_pool_get()  # 2.6, 2.7, 2.3, 2.5 | 2
    threading_get()


if __name__ == "__main__":
    main()
