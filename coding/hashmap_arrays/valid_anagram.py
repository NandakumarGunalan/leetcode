class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] == 0:
                del count[ch]

        return not count

if __name__ == "__main__":
    sol = Solution()

    # Basic cases
    assert sol.isAnagram("anagram", "nagaram") is True
    assert sol.isAnagram("rat", "car") is False

    # Edge cases
    assert sol.isAnagram("", "") is True
    assert sol.isAnagram("a", "a") is True
    assert sol.isAnagram("a", "ab") is False
    assert sol.isAnagram("ab", "ba") is True

    print("All test cases passed ✅")