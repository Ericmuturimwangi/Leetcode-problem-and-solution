
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time = 0
        total_waiting_time = 0
        
        for arrival_time, preparation_time in customers:
            if current_time < arrival_time:
                current_time = arrival_time
            current_time += preparation_time
            total_waiting_time += (current_time - arrival_time)
        
        return total_waiting_time / len(customers)
