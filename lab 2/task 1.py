from random import randint


def generate_random_ip():
    return '.'.join(str(randint(0, 255)) for _ in range(4))


def generate_n_random_unique_ips(n: int) -> set[str]:
    unique_ips = set()

    while len(unique_ips) < n:
        unique_ips.add(generate_random_ip())

    return unique_ips


def main():
    with open('lab 2/files/ip.log', mode='w+', encoding='utf-8') as file:
        file.write('\n'.join(generate_n_random_unique_ips(10_000)))


if __name__ == '__main__':
    main()
