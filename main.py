from typing import List
def twoSum(nums : List[int], target: int) -> List[int]:
    ans = []
    leng = len(nums)
    l = 0
    r = leng-1
    while(l < r):
        tar = nums[l] + nums[r]
        if tar == target:
            ans.append(l)
            ans.append(r)
            break
        elif tar > target:
            l += 1
        else :
            r -= 1
    return ans

