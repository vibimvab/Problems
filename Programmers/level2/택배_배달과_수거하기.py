def solution(cap, n, deliveries, pickups):
    def update(houses):
        delivery_count = 0
        while delivery_count < cap and houses:
            if houses[-1] <= cap - delivery_count:
                delivery_count += houses[-1]
                houses.pop()
            else:
                houses[-1] -= cap - delivery_count
                return

    total_distance = 0
    while deliveries or pickups:
        while deliveries and deliveries[-1] == 0:
            deliveries.pop()
        while pickups and pickups[-1] == 0:
            pickups.pop()
        total_distance += 2 * max(len(deliveries), len(pickups))

        update(deliveries)
        update(pickups)

    return total_distance


if __name__ == '__main__':
    print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
    print(solution(	2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
