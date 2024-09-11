% Parámetros
r1 = 0.1;
a1 = 0.005;
a2 = 0.00004;
r2 = 0.04;
% Función que define el sistema de ecuaciones
function dydt = lotka_volterra(t, d, r1, a1, a2, r2)
    presas = d(1);
    depredadores = d(2);
    dydt = [r1*presas - a1*presas*depredadores; a2*presas*depredadores - r2*depredadores];
end
% Condiciones iniciales
y0 = [2000; 10]; % Inicialmente 2000 conejos y 10 zorros
% Intervalo de tiempo
tspan = [0, 250];
% Resolver el sistema
[t, y] = ode45(@(t,y) lotka_volterra(t,y,r1,a1,a2,r2), tspan, y0);

% Calcular la razón de cambio
dCdt = r1*y(:,1) - a1*y(:,1).*y(:,2);
dZdt = a2*y(:,1).*y(:,2) - r2*y(:,2);
d2Cdt2 = r1*dCdt - a1*dCdt.*y(:,2) - a1*y(:,1).*dZdt;
d2Zdt2 = a2*dCdt.*y(:,2) + a2*y(:,1).*dZdt - r2*dZdt;

% Graficar los resultados
plot(t, y(:,1), 'b', t, y(:,2), 'r');
xlabel('Tiempo');
ylabel('Población');
legend('Presas', 'Depredadores');

% Graficar las primeras derivadas
figure;
plot(t, dCdt, 'b-', t, dZdt, 'r-');
xlabel('Tiempo (t)');
ylabel('Razón de Cambio');
legend('dC/dt', 'dZ/dt');

% Graficar las segundas derivadas
figure;
plot(t, d2Cdt2, 'b-', t, d2Zdt2, 'r-');
xlabel('Tiempo (t)');
ylabel('Segunda Derivada');
legend('d^2C/dt^2', 'd^2Z/dt^2');