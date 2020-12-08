if __name__ == '__main__':
    n, m, s, d = map(int, input().split())
    slots = [int(x) for x in input().split()]

    solution_slots = [0 for x in slots]
    used_indices = set()

    solved = True
    
    cold_remaining = sum(slots)
    for on_slot in sorted(slots):
        
        cold_remaining -= on_slot
        
        if cold_remaining < m:
            print("impossible")
            solved = False
            break
        
        placed = d - on_slot
        if placed < n:
            possible_positions = [idx for idx, x in enumerate(slots) if x == on_slot and idx not in used_indices]
            
            solution_slots[possible_positions[0]] = placed
            
            used_indices.add(possible_positions[0])
            n -= placed
        else:
            possible_positions = [idx for idx, x in enumerate(slots) if x == on_slot and idx not in used_indices]
            
            solution_slots[possible_positions[0]] = n
            break
    
    if solved:
        print(" ".join([str(x) for x in solution_slots]))
            