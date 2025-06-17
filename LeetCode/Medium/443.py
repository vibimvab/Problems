from typing import List


class Solution:
    def update(self, update_idx: int, count: int, current_char: str, chars: List[str]):
        if count == 1:
            chars[update_idx] = current_char
            update_idx += 1
        else:
            chars[update_idx] = current_char
            update_idx += 1
            for i, n in enumerate(str(count)):
                chars[update_idx + i] = n
            update_idx += len(str(count))

        return update_idx

    def compress(self, chars: List[str]) -> int:
        current_char = chars[0]
        count = 1
        update_idx = 0
        for c in chars[1:]:
            if c != current_char:
                update_idx = self.update(update_idx, count, current_char, chars)
                current_char = c
                count = 1
            else:
                count += 1

        update_idx = self.update(update_idx, count, current_char, chars)

        return update_idx


if __name__ == "__main__":
    solution = Solution()
    print(solution.compress(["a","a","b","b","c","c","c"]))
