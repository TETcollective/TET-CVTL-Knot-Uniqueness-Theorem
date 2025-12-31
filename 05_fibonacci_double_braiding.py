import numpy as np
import matplotlib.pyplot as plt

k = 2
double_braid_phase = np.exp(1j * 4 * np.pi / (k + 2))  # -1

angles = np.linspace(0, 2*np.pi, 360)
unit_circle = np.exp(1j * angles)
braided = double_braid_phase * unit_circle

plt.figure(figsize=(8,8))
plt.plot(np.real(unit_circle), np.imag(unit_circle), 'b-', label='Stato iniziale')
plt.plot(np.real(braided), np.imag(braided), 'r--', label='Dopo doppio braiding (fase -1)')
plt.scatter([1], [0], color='blue', s=100)
plt.scatter([-1], [0], color='red', s=100)
plt.title('Simulazione Doppio Braiding Fibonacci Anyons (k=2)')
plt.xlabel('Parte Reale')
plt.ylabel('Parte Immaginaria')
plt.axis('equal')
plt.grid(True, alpha=0.3)
plt.legend()
plt.savefig('05_fibonacci_double_braiding.png', dpi=300)
plt.show()
