class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n = min(nums)
        m = max(nums)
        ans = []
        for i in range(n,m+1):
            if i not in nums:
                ans.append(i)

        return ans