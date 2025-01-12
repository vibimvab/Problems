from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        longest_key = keysPressed[0]
        longest_dur = releaseTimes[0]

        for i in range(1, len(releaseTimes)):
            dur = releaseTimes[i] - releaseTimes[i - 1]
            if dur > longest_dur or (dur == longest_dur and keysPressed[i] > longest_key):
                longest_key = keysPressed[i]
                longest_dur = dur

        return longest_key


if __name__ == '__main__':
    s = Solution()
    print(s.slowestKey([9,29,49,50], "cbcd"))
    print(s.slowestKey([12,23,36,46,62], "spuda"))
