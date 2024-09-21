import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parámetros
alpha = 1.0
beta = 0.1
gamma = 1.5
delta = 0.75

# Sistema de ecuaciones
def sistema(y, t):
    C, L_a, L_n = y
    dC = alpha*C - beta*(L_a/(L_a + L_n))*L_a*C
    dL_a = delta*beta*(L_a/(L_a + L_n))*L_a*C - gamma*L_a
    dL_n = delta*beta*(L_a/(L_a + L_n))*L_n*C - gamma*L_n
    return [dC, dL_a, dL_n]

# Condiciones iniciales
C0 = 40
L_a0 = 9
L_n0 = 5
y0 = [C0, L_a0, L_n0]

# Tiempo
t = np.linspace(0, 15, 1000)

# Resolver el sistema de ecuaciones
sol = odeint(sistema, y0, t)
print(sol[:, 1].tolist())
# Graficar los resultados
plt.figure(figsize=(8,6))
plt.plot(t, sol[:, 0], color='lightsalmon', label='Presas (C)')
plt.plot(t, sol[:, 1], color='mediumvioletred', label='Depredadores alfa (L_a)')
plt.plot(t, sol[:, 2], color='dodgerblue', label='Otros depredadores (L_n)')
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.legend(loc='best')
plt.grid()
plt.show()
