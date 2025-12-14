class Solution:
    def containsDuplicate(self, nums) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


if __name__ == "__main__":
    sol = Solution()

    assert sol.containsDuplicate([1, 2, 3, 1]) is True
    assert sol.containsDuplicate([1, 2, 3, 4]) is False
    assert sol.containsDuplicate([]) is False
    assert sol.containsDuplicate([1]) is False
    assert sol.containsDuplicate([2, 2]) is True

    print("All test cases passed ✅")
