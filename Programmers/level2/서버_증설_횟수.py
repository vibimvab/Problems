def solution(players, m, k):
    server_made_at = [0] * 24
    current_server_count = 1
    total_server_count = 0
    for time, player_count in enumerate(players):
        if time >= k:
            current_server_count -= server_made_at[time - k]

        if current_server_count * m <= player_count:
            new_server_count = (player_count - current_server_count * m + m) // m
            current_server_count += new_server_count
            total_server_count += new_server_count
            server_made_at[time] = new_server_count

    return total_server_count


if __name__ == '__main__':
    print(solution([0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5], 3, 5))
