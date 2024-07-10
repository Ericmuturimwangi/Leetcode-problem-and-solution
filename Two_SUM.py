from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the index of the numbers
        num_to_index = {}
        
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            print(f"Index: {i}, Number: {num}, Complement: {complement}, Num_to_index: {num_to_index}")

            # Check if the complement is already in the dictionary
            if complement in num_to_index:
               
                return [num_to_index[complement], i]
            
            # Store the index of the current number
            num_to_index[num] = i
            
        

        return []