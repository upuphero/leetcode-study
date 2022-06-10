class Solution(object):
    nums=[1,1,1,2,2,3]
    k=2
    def topKFrequent(self, nums, k): 
        hashmap = {}
        for ans in nums:
            if ans not in hashmap:
                hashmap[ans] = 1
            else:
                hashmap[ans] += 1
        result = sorted(hashmap.items(),key=lambda hashmap:hashmap[1],reverse=True)
        res=[]
        for i in range(k):
            res.extend(result[i])
        return res