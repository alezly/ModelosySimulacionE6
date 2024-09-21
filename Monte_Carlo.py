import numpy as np  
import matplotlib.pyplot as plt  

# Parámetros del modelo Lotka-Volterra  
alpha = 0.1  # Tasa de crecimiento de presas  
beta = 0.02  # Tasa de depredación  
gamma = 0.1  # Tasa de muerte de depredadores  
delta = 0.01 # Tasa de crecimiento de depredadores  

# Cantidad de simulaciones y condiciones iniciales  
simulations = 1000  
time_steps = 100  
dt = 0.1  

# Arrays para almacenar resultados  
final_presas = []  
final_depredadores = []  

# Simulación  
for _ in range(simulations):  
    # Condiciones iniciales aleatorias  
    X0 = np.random.uniform(20, 100)  # Población inicial de presas  
    Y0 = np.random.uniform(5, 20)     # Población inicial de depredadores  
    
    # Inicializar la población  
    X = X0  
    Y = Y0  

    # Simular el comportamiento a lo largo del tiempo  
    for t in np.arange(0, time_steps, dt):  
        dX = (alpha * X - beta * X * Y) * dt  
        dY = (delta * X * Y - gamma * Y) * dt  
        X += dX  
        Y += dY  
    
    # Guardar resultados finales  
    final_presas.append(X)  
    final_depredadores.append(Y)  

# Calcular medias de las poblaciones finales  
mean_presas = np.mean(final_presas)  
mean_depredadores = np.mean(final_depredadores)  

# Graficar resultados en un gráfico de barras  
labels = ['Población de Presas', 'Población de Depredadores']  
mean_values = [mean_presas, mean_depredadores]  

plt.bar(labels, mean_values, color=['skyblue', 'salmon'])  
plt.title('Población Media de Presas y Depredadores')  
plt.ylabel('Número de Individuos')  
plt.grid(axis='y', linestyle='--')  
plt.ylim(0, max(mean_values) + 10)  # Extender el eje y para mejor visibilidad  
plt.show()  

# Impresión de resultados  
print(f"Población media final de presas: {mean_presas:.2f}")  
print(f"Población media final de depredadores: {mean_depredadores:.2f}")