class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = False
        hashy = {}
        for num in nums:
            hashy[num] = 1 + hashy.get(num, 0)

            if(hashy[num] > 1):
                result = True
                break         
        
        return result

        