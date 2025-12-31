import numpy as np
import matplotlib.pyplot as plt

NUM_KNOTS = 200
WINDING_TARGET = 8

def generate_knot(max_winding=15):
    winding = np.random.randint(1, max_winding + 1)
    crossings = winding * 3
    return winding, crossings

def fibonacci_payoff(winding, crossings):
    fusion_bonus = winding**2 if winding >= 5 else 0
    crossing_penalty = (crossings - 3*winding)**2
    winding_dist = abs(winding - WINDING_TARGET)
    return fusion_bonus - 5 * crossing_penalty - 10 * winding_dist

knots = [generate_knot() for _ in range(NUM_KNOTS)]

for iter in range(800):
    changed = False
    for i in range(NUM_KNOTS):
        w, c = knots[i]
        current_pay = fibonacci_payoff(w, c)
        
        mutations = []
        mutations.append((w + 1, c + 3))
        if w > 1:
            mutations.append((w - 1, max(c - 3, 0)))
        mutations.append((w, c + 2))
        if c > 3:
            mutations.append((w, c - 3))
        
        best_pay = current_pay
        best_w, best_c = w, c
        for mw, mc in mutations:
            m_pay = fibonacci_payoff(mw, mc)
            if m_pay > best_pay:
                best_pay = m_pay
                best_w, best_c = mw, mc
        
        if (best_w, best_c) != (w, c):
            knots[i] = (best_w, best_c)
            changed = True
    
    if not changed:
        break

final_winding = [w for w, _ in knots]
final_cross = [c for _, c in knots]

unique_w, counts_w = np.unique(final_winding, return_counts=True)
unique_c, counts_c = np.unique(final_cross, return_counts=True)

fig, ax = plt.subplots(1, 2, figsize=(14, 6))
ax[0].bar(unique_w, counts_w, color='purple')
ax[0].axvline(WINDING_TARGET, color='gold', linestyle='--', label=f'Winding = {WINDING_TARGET}')
ax[0].set_title('Distribuzione Finale Winding Number')
ax[0].set_xlabel('Winding Number')
ax[0].legend()

ax[1].bar(unique_c, counts_c, color='teal')
ax[1].set_title('Distribuzione Finale Crossing Number')
ax[1].set_xlabel('Crossing Number')

plt.suptitle('Convergenza Game-Theoretic a Configurazioni Fibonacci-Stabili')
plt.tight_layout()
plt.savefig('06_fibonacci_winding_distribution.png', dpi=300)
plt.show()
