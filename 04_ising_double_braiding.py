import numpy as np
import matplotlib.pyplot as plt

k = 3
theta_double = 4 * np.pi / (k + 2)

angles = np.linspace(0, 2*np.pi, 500)
unit_circle = np.exp(1j * angles)
braided_double = np.exp(1j * theta_double) * unit_circle

plt.figure(figsize=(10,10))
plt.plot(np.real(unit_circle), np.imag(unit_circle), 'b-', linewidth=2, label='Stato iniziale')
plt.plot(np.real(braided_double), np.imag(braided_double), 'r:', linewidth=3, label=f'Dopo doppio braiding (θ = 4π/5)')
plt.scatter([1], [0], color='blue', s=100)
plt.scatter([np.cos(theta_double)], [np.sin(theta_double)], color='red', s=100)
plt.title('Simulazione Doppio Braiding Ising Anyons (k=3)')
plt.xlabel('Parte Reale')
plt.ylabel('Parte Immaginaria')
plt.axis('equal')
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)
plt.savefig('04_ising_double_braiding.png', dpi=300)
plt.show()
