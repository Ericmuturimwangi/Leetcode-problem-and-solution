﻿Problem 1
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
