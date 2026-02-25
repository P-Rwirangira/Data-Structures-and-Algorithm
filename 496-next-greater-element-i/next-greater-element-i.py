class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = defaultdict(lambda: -1)
        stack = []
        for n in nums2:
            while stack and n > stack[-1]:
                freq[stack.pop()] = n
            stack.append(n)
        
        return [freq[n] for n in nums1]
        