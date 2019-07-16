# 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
#
# 示例:
#
# 输入: [4, 6, 7, 7]
# 输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
# 说明:
#
# 给定数组的长度不会超过15。
# 数组中的整数范围是 [-100,100]。
# 给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/increasing-subsequences
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 2:
            return []
        ans = set()

        def dfs(start: int, l: List[int]):
            if start == n and len(l) > 1:
                ans.add(tuple(l))
                return

            for i in range(start, n):
                if len(l) > 0 and nums[start] < l[-1]:
                    continue
                dfs(i + 1, l + [nums[start]])

        for i in range(n - 1):
            dfs(i, [])
        return list(ans)


if __name__ == '__main__':
    s = Solution()
    print(s.findSubsequences([4, 6, 7, 7]))
    print(s.findSubsequences([4, 6]))
    print(s.findSubsequences([]))
    print(s.findSubsequences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))