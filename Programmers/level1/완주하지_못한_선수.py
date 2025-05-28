def solution(participant, completion):
    completed = {}
    for c in completion:
        completed[c] = completed.get(c, 0) + 1

    for p in participant:
        if completed.get(p, 0) == 0:
            return p
        else:
            completed[p] -= 1

    raise RuntimeError("unfinished participant not found")
