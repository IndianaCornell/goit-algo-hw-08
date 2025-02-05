import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)
    total_cost = 0
    
    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        cost = first + second
        total_cost += cost
        
        heapq.heappush(cables, cost)
    
    return total_cost


cables = [8, 5, 3, 6]
print(f"Мінімальні витрати на об'єднання кабелів: {min_cost_to_connect_cables(cables)}")   
