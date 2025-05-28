def solution(points, routes):
    num_robots = len(routes)
    num_collisions = 0
    positions = {i: points[route[0]-1].copy() for i, route in enumerate(routes)}
    destinations = [1 for _ in range(num_robots)]

    def find_collisions() -> int:
        position_count = {}
        collisions = 0
        for x, y in positions.values():
            position_count[(x, y)] = position_count.get((x, y), 0) + 1
            if position_count[(x, y)] == 2:
                collisions += 1

        # return the number of collisions found
        return collisions

    def move_robots():
        finished = []
        for i, position in positions.items():
            # if the robot reached to the last destination
            if destinations[i] >= len(routes[i]):
                finished.append(i)
                continue

            robot_dest = points[routes[i][destinations[i]] - 1]
            if position[0] != robot_dest[0]:  # if row position is different
                positions[i][0] += 1 if position[0] < robot_dest[0] else -1
            else:
                positions[i][1] += 1 if position[1] < robot_dest[1] else -1

            # if the robot reached to the destination, change destination to next one
            if robot_dest[0] == position[0] and robot_dest[1] == position[1]:
                destinations[i] += 1

        # remove the robots finished moving
        for i in finished:
            positions.pop(i)

    # len(positions) == robots remaining to move
    # no more collisions when there is only one robot left moving
    while len(positions) > 1:
        num_collisions += find_collisions()
        move_robots()

    return num_collisions


if __name__ == '__main__':
    print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]]))
    print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]]))
