import numpy as np
import random
import matplotlib.pyplot as plt

NUM_KNOTS = 100
MAX_ITER = 2000

def generate_knot(max_crossings=12):
    crossings = np.random.randint(0, max_crossings + 1)
    signs = np.random.choice([-1, 1], size=crossings)
    return crossings, signs

def cs_energy(crossings, signs, k=5):
    writhe = np.sum(signs)
    return abs(k * writhe) + crossings**2

def payoff(crossings, signs):
    energy = cs_energy(crossings, signs)
    lk = np.sum(signs)
    lk_dist = abs(lk - 6)
    stability = 0 if crossings % 2 == 1 else 5
    return - (energy + 10 * lk_dist + stability)

knots = [generate_knot() for _ in range(NUM_KNOTS)]

for iter in range(MAX_ITER):
    changed = False
    for i in range(NUM_KNOTS):
        cross, signs = knots[i]
        current_pay = payoff(cross, signs)
        
        mutations = []
        new_signs_add = np.append(signs, random.choice([-1, 1]))
        mutations.append((cross + 1, new_signs_add))
        if cross > 0:
            idx = random.randint(0, cross - 1)
            new_signs_rem = np.delete(signs, idx)
            mutations.append((cross - 1, new_signs_rem))
        if cross > 0:
            idx = random.randint(0, cross - 1)
            new_signs_flip = signs.copy()
            new_signs_flip[idx] *= -1
            mutations.append((cross, new_signs_flip))
        
        best_pay = current_pay
        best_cross = cross
        best_signs = signs.copy()
        for m_cross, m_signs in mutations:
            m_pay = payoff(m_cross, m_signs)
            if m_pay > best_pay:
                best_pay = m_pay
                best_cross = m_cross
                best_signs = m_signs.copy()
        
        if (best_cross != cross) or not np.array_equal(best_signs, signs):
            knots[i] = (best_cross, best_signs)
            changed = True
    
    if not changed:
        print(f"Equilibrio raggiunto dopo {iter + 1} iterazioni")
        break

final_crossings = [c for c, _ in knots]
final_lk = [np.sum(s) for _, s in knots]

fig, ax = plt.subplots(1, 2, figsize=(14, 6))
unique_cross, counts_cross = np.unique(final_crossings, return_counts=True)
ax[0].bar(unique_cross, counts_cross, color='teal', alpha=0.8)
ax[0].axvline(3, color='red', linestyle='--', linewidth=2, label='Crossing = 3')
ax[0].set_title('Distribuzione Finale Crossing Number')
ax[0].set_xlabel('Crossing Number')
ax[0].set_ylabel('Numero Nodi')
ax[0].legend()

unique_lk, counts_lk = np.unique(final_lk, return_counts=True)
ax[1].bar(unique_lk, counts_lk, color='orange', alpha=0.8)
ax[1].axvline(6, color='red', linestyle='--', linewidth=2, label='L_k = 6')
ax[1].set_title('Distribuzione Finale Linking Number')
ax[1].set_xlabel('Linking Number')
ax[1].legend()

plt.suptitle('Convergenza Game-Theoretic al Three-Leaf Clover Knot')
plt.tight_layout()
plt.savefig('01_convergence_crossing_lk.png', dpi=300)
plt.show()
