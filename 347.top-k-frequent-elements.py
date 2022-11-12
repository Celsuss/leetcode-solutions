#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        unique = {}
        for i in nums:
            if i in unique:
                unique[i] += 1
            else:
                unique[i] = 1

        return self.getTopKElements(unique, k)

    def getTopKElements(self, unique, k):
        def getTopElement(unique):
            best_val = -1
            best_element = None
            for key in unique:
                if unique[key] > best_val:
                    best_val = unique[key]
                    best_element = key

            return best_element

        out = []
        for i in range(k):
            out.append(getTopElement(unique))
            unique.pop(out[-1])

        return out
        
# @lc code=end

def main():
    s = Solution()

    nums = [1,1,1,2,2,3]
    k = 2
    res = s.topKFrequent(nums, k)
    assert(res == [1,2])

    nums = [1]
    k = 1
    res = s.topKFrequent(nums, k)
    assert(res == [1])

    return 0

if __name__ == '__main__':
    main()