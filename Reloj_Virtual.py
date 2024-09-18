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

def convertir_a_entero(decimal):
    if decimal < 1:  # Si el número es menor que 1
        return int(str(decimal)[2])  # Toma el primer decimal como entero
    else:
        return int(decimal)  # Toma la parte entera

# Inicialización
x0 = 0  # 200 conejos inicialmente
y0 = 1000  # zorros inicialmente
v0 = x0, y0

tspan = (0, 60)
t = np.linspace(*tspan, 2000)

# Resolviendo el sistema de ecuaciones
r = integ.solve_ivp(LotkaVolterra, tspan, v0, t_eval=t)

# Convertir a enteros usando la función definida
x = np.array([convertir_a_entero(val) for val in r.y[0]])
y = np.array([convertir_a_entero(val) for val in r.y[1]])

# Reloj virtual y lista de eventos
eventos = []

for i in range(len(t)):
    if x[i] > 0 and y[i] < 20 and y[i] > 0:  # Regla 1: Aumento de Presas con Pocos Depredadores
        eventos.append((t[i], "Aumento de Presas", x[i], y[i]))
    elif x[i] < 500 and y[i] > 15 and x[i] > 0:  # Regla 2: Disminución de Presas con Muchos Depredadores
        eventos.append((t[i], "Disminución de Presas", x[i], y[i]))
    elif y[i] > 0 and x[i] < 100 and x[i] > 0:  # Regla 3: Disminución de Depredadores con Pocas Presas
        eventos.append((t[i], "Disminución de Depredadores", x[i], y[i]))
    elif y[i] < 20 and x[i] > 1000 and y[i] > 0:  # Regla 4: Aumento de predadores con muchas presas
        eventos.append((t[i], "Aumento de Depredadores", x[i], y[i]))
    elif y[i] > 0 and x[i] == 0:  # Regla 5: Extinción de Depredadores sin Presas
        eventos.append((t[i], "Extinción de Depredadores", x[i], y[i]))
    elif x[i] > 0 and y[i] == 0:  # Regla 6: Crecimiento Exponencial de Presas sin Depredadores
        eventos.append((t[i], "Crecimiento Exponencial de Presas", x[i], y[i]))

# Filtrar el tiempo y las poblaciones donde hay cambios
tiempos_cambios = []
conejos_cambios = []
zorros_cambios = []
eventos_filtrados = []

for i in range(1, len(t)):
    if x[i] != x[i-1] or y[i] != y[i-1]:  # Si hay un cambio
        tiempos_cambios.append(t[i])
        conejos_cambios.append(x[i])
        zorros_cambios.append(y[i])
        # Filtrar eventos que coincidan con tiempos_cambios
        for evento in eventos:
            if abs(evento[0] - t[i]) < 1e-5:  # Comparar tiempos con una tolerancia
                eventos_filtrados.append(evento)

# Imprimir el listado de eventos filtrados
print("Listado de Eventos Filtrados:")
for evento in eventos_filtrados:
    print(f"Tiempo: {evento[0]:.2f}, Evento: {evento[1]}, Conejos: {evento[2]}, Zorros: {evento[3]}")

# Gráfica de la cantidad de conejos y zorros
plt.figure(figsize=(10, 5))
plt.plot(tiempos_cambios, conejos_cambios, label='Conejos', color='blue', marker='o')
plt.plot(tiempos_cambios, zorros_cambios, label='Zorros', color='red', marker='x')
plt.title('Modelo de Lotka-Volterra')
plt.xlabel('Tiempo')
plt.ylabel('Cantidad')
plt.legend()
plt.grid()
plt.show()
