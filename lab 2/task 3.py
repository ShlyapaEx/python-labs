import csv


def process_places(sorted_results: list[dict]):

    for place, sportsman in enumerate(sorted_results):
        sportsman['Место'] = place + 1
        if place > 0:
            current_victory_count = sportsman['Количество побед']
            current_additional_value = sportsman['Доп. показатель']

            if current_victory_count == prev_victory_count \
                    and current_additional_value == prev_additional_value:
                sportsman['Место'] = prev_place + 1

        prev_victory_count = sportsman['Количество побед']
        prev_additional_value = sportsman['Доп. показатель']
        prev_place = sportsman['Место'] - 1


def get_tournament_results():
    sportsmen = []
    with open('lab 2/files/players.csv', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            sportsmen.append(row)

    sorted_results = sorted(sportsmen, reverse=True,
                            key=lambda x: (x['Количество побед'],
                                           x['Доп. показатель']))

    process_places(sorted_results)

    with open('lab 2/files/results.csv', mode='w+',
              newline='', encoding='utf-8') as file:

        writer = csv.DictWriter(file, delimiter=';', extrasaction='ignore',
                                fieldnames=["Спортсмен", "Место"])
        writer.writeheader()
        writer.writerows(sorted_results)


def main():
    get_tournament_results()


if __name__ == '__main__':
    main()
