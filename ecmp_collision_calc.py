import math

def calculate_collision_probability(ecmp_width, num_flows):
    """
    Calculates the probability of at least one hash collision 
    (two flows hashing to the same ECMP path) using the Birthday Paradox.
    """
    if num_flows > ecmp_width:
        return 100.0  # Pigeonhole principle: Guaranteed collision
    
    # Calculate probability of NO collisions
    prob_no_collision = 1.0
    for i in range(num_flows):
        prob_no_collision *= (ecmp_width - i) / ecmp_width
        
    # Probability of AT LEAST ONE collision
    prob_collision = (1.0 - prob_no_collision) * 100
    return round(prob_collision, 2)

def run_simulation():
    print("--- 🌿 SLP: ECMP Hash Collision Profiler ---")
    print("Scenario: Synchronized AI Elephant Flows entering a Leaf-Spine Fabric\n")
    
    # Common ECMP widths in modern data centers
    ecmp_widths = [8, 16, 32, 64]
    
    # Number of massive AI flows (e.g., GPU All-Reduce connections)
    test_flows = [4, 8, 12, 16]
    
    for width in ecmp_widths:
        print(f"🔹 Fabric ECMP Width: {width} parallel paths")
        for flows in test_flows:
            prob = calculate_collision_probability(width, flows)
            
            # Formatting for impact
            if prob > 50:
                alert = "⚠️ HIGH RISK (DLB/Packet Spraying Required)"
            elif prob > 20:
                alert = "🟡 WARNING (Tail latency spikes likely)"
            else:
                alert = "✅ SAFE"
                
            print(f"   -> Hashing {flows} Elephant Flows: {prob}% chance of collision. {alert}")
        print("-" * 50)

if __name__ == "__main__":
    run_simulation()
