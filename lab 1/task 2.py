from itertools import groupby


def get_min_thing(numbers: list[int]):
    if len(numbers) == 0:
        return 0
    if len(numbers) == 1:
        return numbers[0]

    min_number = min(numbers)
    operations_count = min_number

    for index, num in enumerate(numbers):
        numbers[index] -= min_number

    numbers = [list(group) for key, group in
               groupby(numbers, key=lambda x:x != 0) if key]

    for num_list in numbers:
        operations_count += get_min_thing(num_list)

    return operations_count


def main(numbers: list[int]):
    return get_min_thing(numbers)


if __name__ == '__main__':
    numbers = list(map(int, input().split()))
    print(main(numbers))
