import numpy as np
import scipy.integrate as integ
import matplotlib.pyplot as plt 

alpha = 0.1  # tasa de crecimiento de conejos por mes por conejo
beta = 0.005  # éxito en la caza del depredador por producto presa depredador
gamma = 0.04  # tasa de crecimiento de zorros por zorro
delta = 0.00004  # éxito en la caza y cuánto alimenta cazar una presa al depredador

def LotkaVolterra(t, v):
    x, y = v
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return dxdt, dydt 

# Inicialización
x0 = 200  # 2000 conejos inicialmente
y0 = 100  # zorros inicialmente
v0 = x0, y0

tspan = (0, 60)
t = np.linspace(*tspan, 2000)

# Resolviendo el sistema de ecuaciones
r = integ.solve_ivp(LotkaVolterra, tspan, v0, t_eval=t)
x, y = r.y

# Reloj virtual y lista de eventos
eventos = []

for i in range(len(t)):
    if x[i] > 0 and y[i] < 20:  # Regla 1: Aumento de Presas con Pocos Depredadores
        eventos.append((t[i], "Aumento de Presas", x[i], y[i]))
    elif x[i] < 500 and y[i] > 15:  # Regla 2: Disminución de Presas con Muchos Depredadores
        eventos.append((t[i], "Disminución de Presas", x[i], y[i]))
    elif y[i] > 0 and x[i] < 100:  # Regla 3: Disminución de Depredadores con Pocas Presas
        eventos.append((t[i], "Disminución de Depredadores", x[i], y[i]))
    elif y[i] < 20 and x[i] > 1000:  # Regla 4: Aumento de predadores con muchas presas
        eventos.append((t[i], "Aumento de Depredadores", x[i], y[i]))
    elif y[i] == 0 and x[i] > 0:  # Regla 5: Extinción de Depredadores sin Presas
        eventos.append((t[i], "Extinción de Depredadores", x[i], y[i]))
    elif x[i] > 5000 and y[i] == 0:  # Regla 6: Crecimiento Exponencial de Presas sin Depredadores
        eventos.append((t[i], "Crecimiento Exponencial de Presas", x[i], y[i]))

# Imprimir el listado de eventos
print("Listado de Eventos:")
for evento in eventos:
    print(f"Tiempo: {evento[0]:.2f}, Evento: {evento[1]}, Conejos: {evento[2]}, Zorros: {evento[3]}")

# Gráfica de la cantidad de conejos y zorros
plt.figure(figsize=(10, 5))
plt.plot(t, x, label='Conejos', color='blue')
plt.plot(t, y, label='Zorros', color='red')
plt.title('Modelo de Lotka-Volterra')
plt.xlabel('Tiempo')
plt.ylabel('Cantidad')
plt.legend()
plt.grid()
plt.show()
