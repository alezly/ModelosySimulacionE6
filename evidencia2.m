% Parámetros del sistema
m = 2000;      % Masa (población de presas)
k = 10;     % Constante del resorte (población de depredadores)
b = 0.5;    % Coeficiente de amortiguamiento (interacción)

% Condiciones iniciales
y0 = [1 0]; % [posición inicial, velocidad inicial]

% Tiempo de simulación
tspan = [0 250];

%Definiciön de las ecuaciones
ode = @(t,y) [y(2); -(b/m) * y(2) - (k/m) * y(1)];
% Resolver el sistema de ecuaciones diferenciales
[t, y] = ode45(ode, tspan, y0);

% Graficar los resultados
figure;
subplot(2,1,1);
plot(t, y(:,1), 'b', 'LineWidth', 2);
title('Posición de la masa (Población de presas)');
xlabel('Tiempo (s)');
ylabel('Posición (x)');
grid on;

subplot(2,1,2);
plot(t, y(:,2), 'r', 'LineWidth', 2);
title('Velocidad de la masa (Interacción)');
xlabel('Tiempo (s)');
ylabel('Velocidad (v)');
grid on;