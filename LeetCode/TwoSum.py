def tentativa01(self, nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (i != j and nums[i] + nums[j] == target):
                return [i, j]
    return []

def tentativa02(self, nums, target):
    map = {}
    for i, num in enumerate(nums):
        diferenca = target - num
        if diferenca in map:
            return [i, map[diferenca]]
        map[num] = i
    return []

def tentativa03(self, nums, target):
    map = {}
    for i in range(len(nums)):
        if target - nums[i] in map:
            return i,map[target - nums[i]]
        map[nums[i]] = i  