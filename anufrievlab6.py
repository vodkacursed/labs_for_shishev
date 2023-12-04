import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline

# Определение уравнения функции
def equation(x, a, b, c):
    return a * np.abs(x) ** np.abs(b) - c

# Установка значений для x и параметров a, b, c
x_values = np.linspace(-1, 4, 10)
a, b, c = 2, 3, 4

# Вычисление значений функции для установленных x и параметров
y_values = equation(x_values, a, b, c)

# Генерация псевдоэкспериментальных данных с добавлением шума
n = 10  # Количество точек
np.random.seed(42)  # Установка зерна для воспроизводимости
x_experiment = np.linspace(-1, 4, n)
noise = y_values + 2 * a * np.random.normal(size=len(x_values))
y_experiment = equation(x_experiment, a, b, c) + 2 * a * np.random.normal(size=len(x_experiment))

# Интерполяция каноническим полиномом степени n
poly_coeffs = np.polyfit(x_experiment, y_experiment, n - 1)
poly_function = np.poly1d(poly_coeffs)

# Использование метода Лагранжа для интерполяции
lagrange_poly = lagrange(x_experiment, y_experiment)

# Применение кубического сплайна для интерполяции
cubic_spline = CubicSpline(x_experiment, y_experiment)

# Тестовые данные для проверки интерполяции
x_test = np.linspace(-1, 4, 3 * n)

# Вычисление значений интерполяционных полиномов и сплайна для тестовых данных
y_poly = poly_function(x_test)
y_lagrange = lagrange_poly(x_test)
y_spline = cubic_spline(x_test)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(x_test, y_poly, label='Канонический полином')
plt.plot(x_test, y_lagrange, label='Метод Лагранжа')
plt.plot(x_test, y_spline, label='Кубический сплайн')
plt.scatter(x_experiment, y_experiment, label='Экспериментальные данные', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Интерполяция и экспериментальные данные')
plt.legend()
plt.show()
