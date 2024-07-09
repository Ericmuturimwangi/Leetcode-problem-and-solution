class Solution:
    def averageWaitingTime(self, customers):
        current_time = 0 # keeps track of the time the chef takes to start the next order
        total_waiting_time = 0 # waiting time for all customers
        
        for arrival, time in customers:
            if current_time < arrival:
                current_time = arrival
            waiting_time = current_time + time - arrival
            total_waiting_time += waiting_time
            current_time += time
        
        average_waiting_time = total_waiting_time / len(customers)
        return average_waiting_time
