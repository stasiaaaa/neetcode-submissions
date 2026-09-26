class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def sift_down(parent, heap_size):
            while True:
                biggest = parent
                left_child = 2*parent + 1
                right_child = 2*parent + 2

                if (left_child < heap_size and nums[left_child] > nums[biggest]):
                    biggest = left_child
                
                if (right_child < heap_size and nums[right_child] > nums[biggest]):
                    biggest = right_child

                if biggest == parent:
                    break
                
                nums[parent], nums[biggest] = (nums[biggest], nums[parent],)

                parent = biggest
        # Build max heap
        last_parent = n // 2 - 1

        for parent in range(last_parent, -1 , -1):
            sift_down(parent, n)
        
        # move largest value to end
        for end in range(n-1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]

            sift_down(0, end)

        return nums

        
                    
                    

                
                
            
                
        

