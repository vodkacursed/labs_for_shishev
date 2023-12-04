import numpy as np  # Подключение библиотеки для работы с массивами чисел
import matplotlib.pyplot as plt  # Подключение библиотеки для создания графиков
from scipy import stats  # Подключение модуля для статистических вычислений

# Уравнение функции
def equation(x):
    return 0.01 * x**3 + 0.02 * x**2 + 0.03 * x + 0.04  # Определение уравнения

# Создание "идеальной кривой"
x_ideal = np.linspace(-20, 20, 20)  # Создание 20 точек от -20 до 20
y_ideal = equation(x_ideal)  # Создание идеальной кривой на основе уравнения

# Генерация псевдоэкспериментальных данных с добавлением шума
num_datasets = 5  # Количество наборов данных
datasets = []
for _ in range(num_datasets):
    noise_multiplier = np.random.normal(size=len(x_ideal))
    noise = y_ideal + 10 * noise_multiplier * np.random.normal(size=len(x_ideal))
    datasets.append(noise)

# Визуализация псевдоэкспериментальных данных
plt.figure(figsize=(10, 6))  # Создание графика размером 10 на 6
for i, data in enumerate(datasets):
    plt.scatter(x_ideal, data, label=f'Dataset {i+1}')  # Добавление точек на график

plt.title('Псевдоэкспериментальные данные')  # Заголовок графика
plt.xlabel('Значения x')  # Подпись оси x
plt.ylabel('Значения y')  # Подпись оси y
plt.legend()  # Добавление легенды
plt.show()  # Отображение графика

# Проверка на наличие выбросов и исключение их
filtered_datasets = []
for data in datasets:
    z_scores = np.abs(stats.zscore(data))  # Вычисление Z-оценок
    threshold = 3  # Порог для определения выбросов
    filtered_data = data[z_scores < threshold]  # Исключение выбросов
    filtered_datasets.append(filtered_data)

# Вычисление доверительных интервалов
confidence_intervals = []
for data in filtered_datasets:
    confidence_interval = stats.t.interval(0.95, len(data)-1, loc=np.mean(data), scale=stats.sem(data))  # Вычисление доверительного интервала
    confidence_intervals.append(confidence_interval)

# Вывод доверительных интервалов на консоль
for i, interval in enumerate(confidence_intervals):
    print(f"Доверительный интервал для Dataset {i+1}: {interval}")

# Вычисление средних значений и их тренда
means = [np.mean(data) for data in filtered_datasets]  # Вычисление средних значений
trend = np.polyfit(x_ideal, means, 1)  # Вычисление линейного тренда
trend_line = np.poly1d(trend)  # Создание уравнения тренда

# Построение графика средних значений и доверительных интервалов
plt.figure(figsize=(10, 6))  # Создание графика размером 10 на 6
plt.scatter(x_ideal, means, label='Средние значения')  # Добавление точек на график
plt.plot(x_ideal, trend_line(x_ideal), label='Тренд средних значений', linestyle='--')  # Добавление линии тренда

for i, interval in enumerate(confidence_intervals):
    plt.errorbar(x_ideal[i], means[i], yerr=np.abs(np.diff(interval
