from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        dir_level = 0 #keeps track of the current directory level


        for logs in logs:
            if log == "../":
                if dir_level > 0:
                    dir_level -= 1

            elif  log!= "./":
                dir_level += 1

        return dir_level
