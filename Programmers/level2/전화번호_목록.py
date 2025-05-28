def solution1(phone_book):
    # O(n*k) time
    # faster than solution2 because
    phone_book.sort(key=len)  # preprocessing, takes only O(n*log(k)) time
    numbers_by_len = {}
    for number in phone_book:
        for n, numbers in numbers_by_len.items():
            if number[:n] in numbers:
                return False
        if len(number) in numbers_by_len:
            numbers_by_len[len(number)].add(number)
        else:
            numbers_by_len[len(number)] = {number}

    return True


def solution2(phone_book):
    phone_book_set = set(phone_book)
    for number in phone_book:
        for i in range(1, len(number)):
            if number[:i] in phone_book_set:
                return False

    return True
