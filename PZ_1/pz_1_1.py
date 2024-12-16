# Задание 1:
# Определить какое равенство точнее

# Дано:

# Значения
a1 = 4.69  # корень(22)
a2 = 0.095  # 2/21

# Решение:

# Значения с большим числом десятичных знаков
precise_a1 = 4.6904
precise_a2 = 0.0952

# Вычисляем предельные абсолютные погрешности
delta_a1 = abs(precise_a1 - a1) + 0.0001
delta_a2 = abs(precise_a2 - a2) + 0.0001

# Вычисляем предельные относительные погрешности
relative_delta_a1 = delta_a1 / a1 * 100
relative_delta_a2 = delta_a2 / a2 * 100

# Вывод результатов
print(f"Предельная абсолютная погрешность для '4.69': {delta_a1:.4f}")
print(f"Предельная относительная погрешность для '4.69': {relative_delta_a1:.4f}%")
print(f"Предельная абсолютная погрешность для '0.095': {delta_a2:.4f}")
print(f"Предельная относительная погрешность для '0.095': {relative_delta_a2:.4f}%")

# Поиск более точного результата
if relative_delta_a1 < relative_delta_a2:
    print("\nПервое равенство (4.69) является более точным.")
else:
    print("\nВторое равенство (0.095) является более точным.")
