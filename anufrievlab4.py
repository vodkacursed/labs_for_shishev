import numpy as np  # Подключение библиотеки для работы с массивами чисел
import matplotlib.pyplot as plt  # Подключение библиотеки для создания графиков
from scipy.optimize import curve_fit  # Подключение функции для аппроксимации кривой

# Уравнение сигмоиды
def sigmoid(x, a, b, c, d):
    return a * np.exp(-b * x) / (1 + np.exp(-c * (x - d)))  # Определение уравнения сигмоиды

# Генерация коэффициентов сигмоиды по экспоненциальному и псевдонормальному законам
a, c = np.random.exponential(size=2)  # Создание двух коэффициентов по экспоненциальному распределению
b, d = np.random.normal(size=2)  # Создание двух коэффициентов по нормальному распределению

# Создание идеальной кривой
x_ideal = np.linspace(-20, 20, 200)  # Создание 200 точек от -20 до 20
y_ideal = sigmoid(x_ideal, a, b, c, d)  # Создание идеальной кривой на основе сигмоиды и коэффициентов

# Генерация псевдоэкспериментальных данных с добавлением шума
x_experiment = np.linspace(-20, 20, np.random.randint(150, 251))  # Создание случайного количества точек от 150 до 250 в диапазоне от -20 до 20
noise = np.random.normal(size=len(x_experiment))  # Генерация случайного шума
y_experiment = sigmoid(x_experiment, a, b, c, d) + a * 0.2 * noise  # Создание данных с учетом шума

# Оценка параметров для линии тренда
params, covariance = curve_fit(sigmoid, x_experiment, y_experiment)  # Аппроксимация кривой по данным

# Получение значений для линии тренда
y_trend = sigmoid(x_experiment, *params)  # Получение значений линии тренда

# Построение графика
plt.figure(figsize=(10, 6))  # Создание графика размером 10 на 6

plt.plot(x_ideal, y_ideal, label='Идеальная кривая')  # Добавление идеальной кривой на график
plt.scatter(x_experiment, y_experiment, label='Псевдоэкспериментальные данные', alpha=0.7)  # Добавление псевдоэкспериментальных данных на график
plt.plot(x_experiment, y_trend, label='Линия тренда', linestyle='--')  # Добавление линии тренда на график

plt.title('Линия тренда на основе зашумленных данных')  # Заголовок графика
plt.xlabel('Значения x')  # Подпись оси x
plt.ylabel('Значения y')  # Подпись оси y
plt.legend()  # Добавление легенды
plt.show()  # Отображение графика

# Оценка распределения отклонений псевдоэкспериментальных значений от линии тренда
deviation = y_experiment - y_trend  # Вычисление отклонений
plt.hist(deviation, bins=20, alpha=0.7)  # Построение гистограммы отклонений
plt.title('Распределение отклонений от линии тренда')  # Заголовок гистограммы
plt.xlabel('Отклонение')  # Подпись оси x
plt.ylabel('Частота')  # Подпись оси y
plt.show()  # Отображение гистограммы
