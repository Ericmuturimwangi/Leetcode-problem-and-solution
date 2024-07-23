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

Problem 7 726. Number of Atoms

Given a string formula representing a chemical formula, return the count of each atom.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.

    For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.

Two formulas are concatenated together to produce another formula.

    For example, "H2O2He3Mg4" is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula.

    For example, "(H2O2)" and "(H2O2)3" are formulas.

Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

The test cases are generated so that all the values in the output fit in a 32-bit integer.

Example 1:

Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.

Example 2:

Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.

Example 3:

Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.

Solution

Problem 8 2196. Create BInary Tree From Description

You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, islefti] indicates that parenti is the parent of childi, ina binary tree of unique values. Furthermore:

- If isLefti == 1, then childi is the left child of parenti
- If isleft== 0, then childi is the right hand of the parenti.
  COnstruct a binary tree described by the descriptiuions adn return its root.
  Example1:
  Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]
  Output: [50,20,80,15,17,19]
  Explanation: THe first node in every para is the parent, the second is the child the third is either a 1 or 0 to represent if the child is going left or right.

Problem 9 2096. Step-By-Step DIrections From a Binary Tree Node to Another
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startvalue representing the value of the start node s, and a different int destValue representing the value of the destination node t. FInd the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L, 'R', and 'U'. Each letter indicates a specific direction:
L- means going from a node to the left child node.
R- means going from a node to the right child node.
U- means going from a node to the parent node.

Solution:

Problem 10 1380. Lucky Numbers in A Matrix
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.

Problem 11:
You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.

Example 1:

Input: rowSum = [3,8], colSum = [4,7]
Output: [[3,0],
         [1,7]]
Explanation:
0th row: 3 + 0 = 3 == rowSum[0]
1st row: 1 + 7 = 8 == rowSum[1]
0th column: 3 + 1 = 4 == colSum[0]
1st column: 0 + 7 = 7 == colSum[1]
The row and column sums match, and all matrix elements are non-negative.
Another possible matrix is: [[1,2],
                             [3,5]]

Example 2:

Input: rowSum = [5,7,10], colSum = [8,6,8]
Output: [[0,5,0],
[6,1,0],
[2,0,8]

Problem 12
Sort the People
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.

Example 2:

Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

Problem 13:
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]
