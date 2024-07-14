Problem 1
There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:
arrivali is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
Timei is the time needed to prepare the order of the ith customer.
When a customer arrives, he gives the chef his order,and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input.
Return the average waiting time of all customers. Solutions within 10­-5 from the actual answer are considered as accepted.
Solution:
There is a list with 2 elements.
each list represents customer where first element- time of customer arrival and the second is how much time needed to cook the order.
Approach of Greedy simulation.

steps is solving the problem include:

- tracking the chef’s idle time and ready to take the next order.
  -calculate the waiting time for each customer. The time the customer waits is based on when the chef starts preparing the order.
- update the chef’s idle time. After finishing the customer’s order, update the time when the chef will be idle next.
  CHeck on the Average_waiting_time.py

Problem 2.
The Leetcode filesystem keeps a log each time some user performs a change folder operation.
THe operations are "../" move t parent folder of the current folder.
"./" remain in the same folder
"x/" move to child folder named x
example 1: input logs = ["d1/","d2/","../","d21/","./"]
solution: 1+1-1+1 = 2
e
Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
Output: 3
Input: logs = ["d1/","../","../","../"]
Output: 0
Code:
it is imp to note that the dir_level should be decremented when
encountering "../" and should not change when encountering "./" but should increment for other cases that signifify up surge.

Problem 3
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Solution:
Use of a hash map or dictionary in python.

Problem 4
You are given a string s that consists of ower case English letters and brackets. Reverse the strings in each pair of matching parentheses, starting from the innermost one. The result should not contain brackets.
Example 1:
input: s = "(abcd)"
output: "dcba"
Example 2:
input: s = "(u(love)i)"
output: "iloveu
Example 3:
Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Solution:
In solving this problem, I will use a stack in helping to keep track of the characters and reverse the substrings. the steps:
-initialize empty stack.
-traverse each character in the string.(if char is an opening parentheses push it on to the stack., if char is a closing parentheses, pop characters from hte stack until the opening parentheses. reverse the popped characers and push them back to the stack and if character is a letter, push it onto the stack.)
Code:
class Solution:
def reverseParentheses (self, s: str) -> str:
if (S= str):

Problem 5 1717. Maximum Score From Removing Substrings
You are given a string s and two integers x and y. YOu can perform two types of operations any number of times. Remove substring "ab" and gain x points. eg, when removinf "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points. For exmaple, when removing "ba" from "cabxbae" it becomes "cabxe". Return the mx points you can gain after applying the operations.
Solution:
Using greddy approach. If x>=y, then consider removing "ab" first and removing "ba" next. Otherwise, consider removing "ba" first and removing "ab" next.

Problem 6
2751 Robot Collisions
There are n 1-indexed robots, each having a position on a line, health, and movement direction. You are given 0-indexed integer arrays positions, healthsm and a string directins (directions[i] is either 'L' for left or 'R' for right.) ALl integers in positions are unique.
ALl robotsstart to move in line simultaneously at the same speed in their given directions. If 2 robots ever share the same position while moving , they collide. IN case the two robots collide, the robot with lower health is removed from the lince and the health of the other robot decreases by one. THe survivign robot continues in the same direction it was going. If both robots have the sam ehealth, they are both removed from the line. Task ahead is to determine the health of the robots that survive the collision, in the same order that the robots were given. Return an array to contain the health of the remaining robots.
SOLUTION:
The first step should be to sort the robots by positions. This helps in simulating the
collisions by movements on the line.

We can use stakc to simualte the movements and the collisions:
-iterate through the robots in order of their positions.
-if a robot is moving right (R) push it into the stack.
-if a robot is moving (L) check for collisions with robots in the stack moving right.
incase the stack is empty or the top robot in the stack is movingleft, push the current robot onto the stack.

-Otherwise, simulate the collision:Compare the health of the current robot and the top robot in the stack, adjust the healths based on the collisiion rules andremove robots as necessary.
