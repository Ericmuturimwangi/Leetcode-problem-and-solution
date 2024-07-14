from typing import List # importing list from typing module.

class Solution:
    def survivedRobotHealths(self, positions:List[int], healths:list[int], directions: str) -> List[int]: # clss solution with a method survivedRobotHealths taking 3 parameters positions integers, healths integers and directions as a string. 
        robots = sorted(zip(positions, health, directions, range(leng(positions)))) # zip is used to combine the positions, health, directions and range. then sort tuples by positions. 
        stack = [] #used to simulate the collision process. 

        for pos, health, direction, idx in robots:
            if direction == 'R':
                stack.append((pos, health, direction, idx))
            else:
                    while stack and stack[-1][2] == 'R': 
                        prev_pos, prev_health, prev_direction, prev_idx = stack.pop()
                        if prev_health > health:
                            stack.append((prev_pos, prev_health -1, prev_direction, prev_idx))
                            health = 0
                            break
                        elif prev_health < health:
                            health -=1
                        else:
                            health = 0
                            break
                        if health > 0:
                            stack.append((pos, health, direction, idx))

        survivors = sprted(stack, key=lambda x:x[3])
        return [health for _, health, _, _ in survivors] 

