import ipaddress


def solve_ips(mask):
    with open('lab 2/files/ip.log', mode='r', encoding='utf-8') as file:
        file_lines = file.read().splitlines()

    network_addresses = []
    for ip_address in file_lines:
        network_addresses.append(str(ipaddress.IPv4Network(
            f'{ip_address}/{mask}', strict=False).network_address))

    with open('lab 2/files/ip_solve.log', 'w+', encoding='utf-8') as file:
        file.write('\n'.join(network_addresses))


def main():
    mask = input()
    solve_ips(mask)


if __name__ == '__main__':
    main()
