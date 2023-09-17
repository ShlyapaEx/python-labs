import re
from collections import Counter


BASE_PATH = 'lab 2/files'


def get_cyrillic_letters_frequencies(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        file_text = file.read().strip().lower()
    clean_text = re.sub('[^а-я]', '', file_text)

    all_letters_count = len(clean_text)
    count_by_letter = Counter(clean_text)

    with open(f'{BASE_PATH}/article_rus_solve.txt', mode='w',
              encoding='utf-8') as file:
        for letter, count in count_by_letter.most_common():
            current_letter_frequency = round(count/all_letters_count, 4)
            file.write(f'{letter}: {current_letter_frequency}\n')


def main():
    print(get_cyrillic_letters_frequencies(f'{BASE_PATH}/article_rus.txt'))


if __name__ == '__main__':
    main()
