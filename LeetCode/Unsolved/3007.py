class Solution:
    def findMaximumNumber_string(self, k: int, x: int) -> int:
        accumulated = 0
        num = 1
        while True:
            s = bin(num)[2:]
            new_price = s[-x::-x].count('1')

            accumulated += new_price
            if accumulated > k:
                return num - 1

            num += 1

    def findMaximumNumber_naive(self, k: int, x: int) -> int:
        accumulated = 0
        i = 1
        while True:
            num = i
            price = 0
            num >>= x-1
            while num > 0:
                price += num & 1
                num >>= x

            accumulated += price
            if accumulated > k:
                return i - 1

            i += 1

    def findMaximumNumber_dict(self, k: int, x: int) -> int:
        price = {0: 0}
        accumulated = 0
        i = 1
        while True:
            num = i
            try:
                accumulated += price[num >> (x-1)]
                if accumulated > k:
                    return num - 1
            except KeyError:
                num >>= x - 1
                new_price = price[num & int((2 ** (num.bit_length() - 1) - 1))] \
                    + bool(i & (1 << ((i.bit_length()+x-1)//x*x-1)))

                price[num] = new_price
                continue

            i += 1

        return -1

    def findMaximumNumber_binary_search(self, k: int, x: int) -> int:
        digit = 1
        while True:
            if digit * (1 << digit-1) <= k:
                break
            digit += 1





        # if k <= 1 << (2*x-2):
        #     return (k+1) // (1 << x-1) * (1 << x-1) + k
        #
        # accumulated_lower = 1 << 2*x-2
        # digit = 1
        # while True:
        #     digit += 1
        #     accumulated_higher = accumulated_lower * 2  # number of 1s in the following digit
        #     accumulated_higher += 1 << digit-1 << 2*x-2  # number of 1s in the leading digit
        #     if accumulated_higher > k:
        #         break
        #     accumulated_lower = accumulated_higher
        #
        # target = 1 << digit-1
        # while digit > 1:
        #     count = accumulated_lower + (1 << digit + 2*x - 4) + (digit-2)**2 << (2*x-2)
        #     # if count <= k:
        #     #     digit -= 1
        #     if count > k:
        #         target +=
        #         accumulated_lower = count
        #     digit -= 1



    def findMaximumNumber(self, k: int, x: int) -> int:
        return self.findMaximumNumber_binary_search(k, x)


if __name__ == '__main__':
    # print(1 + bool(1237846))
    # x = 2
    # for i in range(1, 100):
    #     print(i,  bool(i & (1 << ((i.bit_length()+1)//x*x-1))))

    solution = Solution()
    # print(solution.findMaximumNumber(1, 2))
    # print(solution.findMaximumNumber(2, 2))
    # print(solution.findMaximumNumber(3, 2))
    # print(solution.findMaximumNumber(4, 2))
    # print(solution.findMaximumNumber(9, 1))
    print(solution.findMaximumNumber(100, 3))
    print(solution.findMaximumNumber(19, 6))
