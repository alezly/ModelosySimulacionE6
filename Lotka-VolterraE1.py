import numpy as np
import scipy.integrate as integ
import matplotlib.pyplot as plt 

alpha=0.1 # tasa de crecimiento de conejos por mes por conejo
beta=0.005 #  éxito en la caza del depredador por producto presa depredador
gamma=0.04 # tasa de crecimiento de zorros por zorro
delta=0.00004 #  éxito en la caza y cuánto alimenta cazar una presa al depredador

def LotkaVolterra(t, v):
    x,y = v
    dxdt = alpha*x-beta*x*y
    dydt = delta*x*y - gamma*y
    return dxdt, dydt 

x0 = 2000 #2000 conejos inicialmente
y0 = 10 #zorros inicialmente
v0 = x0,y0

tspan = (0, 250)
t = np.linspace(*tspan, 2000)

r = integ.solve_ivp(LotkaVolterra, tspan, v0, t_eval=t)
x,y=r.y

# Figura
fig, ax1 = plt.subplots(figsize=(12,4))
ax2 = ax1.twinx()
ax1.plot(t, x, 'g-')
ax2.plot(t, y, 'b-')
ax1.set_xlabel('Tiempo [meses]')
ax1.set_ylabel('Conejos', color='g')
ax1.set_ylim([0,3000])
for label in ax1.get_yticklabels():
    label.set_color("green")
ax1.spines["left"].set_color("green")

ax2.set_ylabel('Zorros', color='b')
ax2.set_xlim([0,250])
ax2.set_ylim([0,250])
for label in ax2.get_yticklabels():
    label.set_color("blue")
ax1.spines["right"].set_color("blue")

ax1.grid()
ax2.grid()
plt.show()