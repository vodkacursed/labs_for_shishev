import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, shapiro, anderson

# Генерация двух выборок: случайная и нормальное распределение
sample_size_1 = np.random.randint(1000, 2001)
sample_1 = np.random.rand(sample_size_1)

sample_size_2 = np.random.randint(1000, 2001)
sample_2 = np.random.normal(loc=0, scale=1, size=sample_size_2)

# Вычисление статистических характеристик выборок
mean_1, std_dev_1 = np.mean(sample_1), np.std(sample_1)
mean_2, std_dev_2 = np.mean(sample_2), np.std(sample_2)

# Функция для вычисления плотности вероятности нормального распределения
def probability_density_function(x, mean, std_dev):
    return norm.pdf(x, loc=mean, scale=std_dev)

# Вычисление значений плотности вероятности для второй выборки
x = np.linspace(min(sample_2), max(sample_2), 1000)
pdf_values = probability_density_function(x, mean_2, std_dev_2)

# Построение гистограмм для обеих выборок
plt.figure(figsize=(10, 6))

plt.hist(sample_1, bins=30, alpha=0.5, label='Случайная выборка')
plt.hist(sample_2, bins=30, alpha=0.5, label='Нормальное распределение')

plt.plot(x, pdf_values, 'r--', label='Функция плотности вероятности для нормального распределения')

plt.title('Гистограммы распределений и функция плотности вероятности')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.legend()
plt.show()

# Тестирование выборок с помощью критериев Шапиро и Андерсена
shapiro_stat_1, shapiro_p_1 = shapiro(sample_1)
shapiro_stat_2, shapiro_p_2 = shapiro(sample_2)

anderson_stat_1, anderson_crit_1, anderson_lvl_1 = anderson(sample_1, dist='norm')
anderson_stat_2, anderson_crit_2, anderson_lvl_2 = anderson(sample_2, dist='norm')

# Вывод результатов тестирования
print("Результаты тестирования первой выборки:")
print(f"Критерий Шапиро p-value: {shapiro_p_1}, статистика: {shapiro_stat_1}")
print(f"Критерий Андерсена-Дарлинга: {anderson_stat_1}, критические значения: {anderson_crit_1}")
print()
print("Результаты тестирования второй выборки:")
print(f"Критерий Шапиро p-value: {shapiro_p_2}, статистика: {shapiro_stat_2}")
print(f"Критерий Андерсена-Дарлинга: {anderson_stat_2}, критические значения: {anderson_crit_2}")
