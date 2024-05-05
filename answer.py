def find_common_divisors(numbers):
   # Находим минимальное число из входного массива
   min_num = min(numbers)
   # Создаем список для хранения общих делителей
   common_divisors = []


   # Перебираем числа от 1 до минимального числа
   for i in range(1, min_num + 1):
       is_common_divisor = True
       # Проверяем, является ли текущее число делителем для всех чисел из входного массива
       for num in numbers:
           if num % i != 0:
               is_common_divisor = False
               break
       # Если текущее число является делителем для всех чисел, добавляем его в список общих делителей
       if is_common_divisor:
           common_divisors.append(i)

   return common_divisors
