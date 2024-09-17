import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo
alpha = 0.1  # Tasa de crecimiento de conejos
beta = 0.02  # Tasa de depredación
delta = 0.01  # Tasa de crecimiento de zorros
gamma = 0.1  # Tasa de mortalidad de zorros

# Condiciones iniciales
R0 = 40  # Población inicial de conejos
F0 = 9   # Población inicial de zorros
time_steps = 200  # Número de pasos de tiempo

# Almacenamiento de resultados
R = np.zeros(time_steps)
F = np.zeros(time_steps)
R[0] = R0
F[0] = F0

# Simulación de Monte Carlo
for t in range(1, time_steps):
    R[t] = R[t-1] + (alpha * R[t-1] - beta * R[t-1] * F[t-1]) + np.random.normal(0, 2)
    F[t] = F[t-1] + (delta * R[t-1] * F[t-1] - gamma * F[t-1]) + np.random.normal(0, 1)
    
    # Asegurarse de que las poblaciones no sean negativas
    R[t] = max(R[t], 0)
    F[t] = max(F[t], 0)

# Visualización de los resultados
plt.figure(figsize=(12, 6))
plt.plot(R, label='Conejos (presas)', color='blue')
plt.plot(F, label='Zorros (depredadores)', color='red')
plt.title('Simulación de Zorros y Conejos usando Monte Carlo')
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.legend()
plt.grid()
plt.show()