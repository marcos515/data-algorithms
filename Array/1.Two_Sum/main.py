class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = { v : i  for i, v in enumerate(nums) }
        
        for i, num in enumerate(nums):
            target_num = target - num
            
            if target_num in hash_map:
                index_sec = hash_map[target_num]
                if index_sec == i:
                    continue
                return [i, index_sec]
        
        return []
    
if __name__ == "__main__":
    s = Solution()

    print(s.twoSum([2, 7, 11, 15], 9)) # [0, 1]