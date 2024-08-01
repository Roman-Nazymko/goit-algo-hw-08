import heapq

def min_cost_to_connect_cables(cable_lengths):
    heapq.heapify(cable_lengths)
    
    total_cost = 0
    
    # Злиття кабелів до тих пір, поки не залишиться лише один кабель
    while len(cable_lengths) > 1:
        # Витягти два найменші елементи з кучі
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        
        # Вартість з'єднання цих кабелів
        cost = first + second
        total_cost += cost
        
        # Додати новий кабель назад у купу
        heapq.heappush(cable_lengths, cost)

        print(
            f"Об'єднання кабелів {first} та {second} з витратами {cost}. Загальні витрати: {total_cost}"
        )
        print(f"Поточний стан купи: {cable_lengths}")
        
    return total_cost

# Приклад довжин кабелів
cable_lengths = [4, 3, 2, 6]
print("Мінімальні витрати на з'єднання кабелів: ", min_cost_to_connect_cables(cable_lengths)) 

