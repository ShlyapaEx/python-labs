def main(tickets: list[str]):
    tickets_per_place = dict()

    for ticket_data in tickets:
        row, seat, cost = map(int, ticket_data.split())
        if (row, seat) not in tickets_per_place:
            tickets_per_place[(row, seat)] = {cost}
        tickets_per_place[(row, seat)].add(cost)
    return tickets_per_place


if __name__ == '__main__':
    input_count = int(input())
    tickets = []
    for _ in range(input_count):
        tickets.append(input())
    result = main(tickets)

    for row, seat in result.keys():
        print(f'{row} {seat} – {len(result[(row, seat)])}')
