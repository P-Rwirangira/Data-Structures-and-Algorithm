class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hMap = defaultdict(lambda: -1)
        stack = []
        for n in nums2:
            while stack and n > stack[-1]:
                hMap[stack.pop()] = n
            stack.append(n)
        
        return [hMap[n] for n in nums1]
        