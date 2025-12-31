import numpy as np
import matplotlib.pyplot as plt

NUM_KNOTS = 200
MAX_ITER = 800

def generate_multi_knot():
    knot_type = np.random.choice(['ising', 'fib'], p=[0.7, 0.3])
    if knot_type == 'ising':
        winding = np.random.randint(1, 6)
    else:
        winding = np.random.randint(5, 12)
    crossings = winding * 3 + np.random.randint(-2, 3)
    crossings = max(3, crossings)
    return knot_type, winding, crossings

def payoff(knot_type, winding, crossings):
    if knot_type == 'ising':
        target = 3
        bonus = 20 if crossings == 3 else 0
    else:
        target = 8
        bonus = winding**2 if winding >= 5 else 0
    energy = crossings**2 + abs(winding - target)*10
    return bonus - energy

knots = [generate_multi_knot() for _ in range(NUM_KNOTS)]
history = []

for iter in range(MAX_ITER):
    changed = False
    for i in range(NUM_KNOTS):
        current = knots[i]
        current_pay = payoff(*current)
        
        mutations = []
        t, w, c = current
        mutations.append(('fib' if t == 'ising' else 'ising', w, c))
        for dw in [-1, 1]:
            new_w = max(1, w + dw)
            mutations.append((t, new_w, c))
        for dc in [-3, 3]:
            new_c = max(3, c + dc)
            mutations.append((t, w, new_c))
        
        best_pay = current_pay
        best_state = current
        for mut in mutations:
            mut_pay = payoff(*mut)
            if mut_pay > best_pay:
                best_pay = mut_pay
                best_state = mut
                changed = True
        
        knots[i] = best_state
    
    ising_count = sum(1 for t, _, c in knots if t == 'ising' and c == 3)
    fib_count = sum(1 for t, w, _ in knots if t == 'fib' and w >= 5)
    history.append((ising_count, fib_count))
    
    if not changed:
        print(f"Equilibrio raggiunto dopo {iter + 1} iterazioni")
        break

iters = np.arange(len(history))
ising_evo = [h[0] for h in history]
fib_evo = [h[1] for h in history]

plt.figure(figsize=(12,6))
plt.plot(iters, ising_evo, 'b-', label='Ising trefoil knots (crossing=3)')
plt.plot(iters, fib_evo, 'r--', label='Fibonacci high-winding knots (w≥5)')
plt.title('Evoluzione Multi-Knot: Ising + Fibonacci Anyons')
plt.xlabel('Iterazioni')
plt.ylabel('Numero Nodi')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('02_multi_knot_evolution.png', dpi=300)
plt.show()
