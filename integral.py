import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Метод Монте-Карло для обчислення інтеграла з різними N
N_values = [1000, 10000, 100000]
mc_results = []

for N in N_values:
    x_rand = np.random.uniform(a, b, N)
    y_rand = np.random.uniform(0, f(b), N)
    under_curve = y_rand < f(x_rand)
    integral_mc = (b - a) * f(b) * np.mean(under_curve)
    mc_results.append(integral_mc)
    print(f"Інтеграл методом Монте-Карло для N={N}: {integral_mc}")

print(f"Інтеграл методом Монте-Карло: {integral_mc}")

# Обчислення інтеграла за допомогою функції quad
result, error = spi.quad(f, a, b)

print(f"Інтеграл за допомогою функції quad: {result}")