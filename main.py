import functions_framework
from flask import jsonify

# Функція для перевірки, чи є число простим
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Точка входу для обробки HTTP запиту
@functions_framework.http
def check_number(request):
    # Заготовлені значення для перевірки
    numbers = [7, 10, 15, 20, 23]

    # Результати перевірок для кожного числа
    results = []

    for number in numbers:
        result = {
            "number": number,
            "is_even": number % 2 == 0,
            "is_odd": number % 2 != 0,
            "is_prime": is_prime(number)
        }
        results.append(result)

    return jsonify(results)
