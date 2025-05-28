def solution(today, terms, privacies):
    today = [int(n) for n in today.split('.')]
    privacy_types = {}
    for term in terms:
        privacy_types[term[0]] = int(term.split()[-1])

    expired = []
    for i, privacy in enumerate(privacies):
        expiry, privacy_type = privacy.split()
        expiry = [int(n) for n in expiry.split('.')]
        expiry[1] += privacy_types[privacy_type]
        expiry[0] += (expiry[1] - 1) // 12
        expiry[1] = (expiry[1] - 1) % 12 + 1

        if expiry <= today:
            expired.append(i + 1)

    return expired

if __name__ == '__main__':
    print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
