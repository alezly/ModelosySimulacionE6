import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parámetros del sistema
m = 2000  # Masa (población de presas)
k = 10    # Constante del resorte (población de depredadores)
b = 0.5   # Coeficiente de amortiguamiento (interacción)

# Condiciones iniciales
x0 = 1    # Posición inicial (población de presas)
v0 = 0    # Velocidad inicial (interacción)
y0 = [x0, v0]

# Tiempo de simulación
t_start = 0
t_end = 250
t = np.linspace(t_start, t_end, 1000)

# Definición de las ecuaciones
def mass_spring_damper(y, t, m, k, b):
    """
    Función que define la ecuación diferencial del sistema masa-resorte-amortiguador.
    
    Parámetros:
    y (numpy.ndarray): Vector de estado [posición, velocidad].
    t (float): Tiempo.
    m (float): Masa (población de presas).
    k (float): Constante del resorte (población de depredadores).
    b (float): Coeficiente de amortiguamiento (interacción).
    
    Retorna:
    numpy.ndarray: Derivada del vector de estado [velocidad, aceleración].
    """
    x, v = y
    dx_dt = v
    dv_dt = -(b/m) * v - (k/m) * x
    return np.array([dx_dt, dv_dt])

# Resolver el sistema de ecuaciones diferenciales
sol = odeint(mass_spring_damper, y0, t, args=(m, k, b))

# Graficar los resultados
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.plot(t, sol[:, 0], 'b', linewidth=2)
ax1.set_title('Posición de la masa (Población de presas)')
ax1.set_xlabel('Tiempo (s)')
ax1.set_ylabel('Posición (x)')
ax1.grid()

ax2.plot(t, sol[:, 1], 'r', linewidth=2)
ax2.set_title('Velocidad de la masa (Interacción)')
ax2.set_xlabel('Tiempo (s)')
ax2.set_ylabel('Velocidad (v)')
ax2.grid()

plt.tight_layout()
plt.show()
