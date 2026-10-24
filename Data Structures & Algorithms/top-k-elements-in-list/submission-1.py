class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       # Bucket sort
       # Time: O(n)
       # Space: O(n)

        counts = Counter(nums) #split array into dict with freq. 

        # Fill buckets
        buckets = [[]  for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)

        # Scan buckets, save top k elements
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result


    
        

        
