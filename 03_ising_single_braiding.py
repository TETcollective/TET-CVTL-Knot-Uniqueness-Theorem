import numpy as np
import matplotlib.pyplot as plt

k = 3
theta_sigma = np.pi / (k + 2)

angles = np.linspace(0, 2*np.pi, 200)
unit_circle = np.exp(1j * angles)
braided = np.exp(1j * theta_sigma) * unit_circle

plt.figure(figsize=(8,8))
plt.plot(np.real(unit_circle), np.imag(unit_circle), 'b-', label='Stato iniziale')
plt.plot(np.real(braided), np.imag(braided), 'r--', label=f'Dopo braiding singolo (θ = π/5)')
plt.scatter([1], [0], color='blue', s=100)
plt.scatter([np.cos(theta_sigma)], [np.sin(theta_sigma)], color='red', s=100)
plt.title('Simulazione Braiding Singolo Ising Anyons (k=3)')
plt.xlabel('Parte Reale')
plt.ylabel('Parte Immaginaria')
plt.axis('equal')
plt.grid(True, alpha=0.3)
plt.legend()
plt.savefig('03_ising_single_braiding.png', dpi=300)
plt.show()
