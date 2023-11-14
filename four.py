import numpy as np

def pearson_correlation(x, y):
    # Проверка на одинаковую длину массивов
    if len(x) != len(y):
        raise ValueError("Массивы должны быть одинаковой длины")

    # Расчет средних значений массивов
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # Расчет суммы произведений отклонений от средних
    numerator = sum((x - x_mean) * (y - y_mean))

    # Расчет суммы квадратов отклонений от средних
    denominator = np.sqrt(sum((x - x_mean)**2) * sum((y - y_mean)**2))

    # Расчет корреляции Пирсона
    correlation = numerator / denominator
    return correlation

# Пример использования
x = np.array([1, 2, 3, 4, 5])
y = np.array([6, 7, 8, 9, 10])

correlation = pearson_correlation(x, y)
print(correlation)