class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) ->List[str]:
        height_to_name = {} #create a hashmap to map the heights ot their respective names
        for h, n in zip(heights, names): #iterate over both arrays.
            height_to_name[h] = n
        
        res = [] #output the result

        for h in reversed(sorted(heights)):
            res.append(height_to_name[h])

        return res
    