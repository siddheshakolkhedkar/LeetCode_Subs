class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n = min(nums)
        m = max(nums)
        set_1 = set(nums)
        set_2 = set(i for i in range(n,m+1))

        set_3 = set_2 - set_1

        return sorted(list(set_3))