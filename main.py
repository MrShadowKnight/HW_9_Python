# TASK №1

def multiply_elements(list):
    result = 1
    for num in list:
        result *= num
    return result

my_list_one = []
numbers = int(input("Введіть кількість чисел в списку: "))
while numbers > 0:
    numbers_for_list = int(input("Введіть число для списку: "))
    my_list_one.append(numbers_for_list)
    numbers -= 1
result = multiply_elements(my_list_one)
print("Добуток елементів списку:", result)

# TASK №2

def min_element(list):
    minimum = list[0]
    for num in list[1:]:
        if num < minimum:
            minimum = num
    
    return minimum

my_list_two = []
numbers = int(input("Введіть кількість чисел для списку: "))
while numbers > 0:
    numbers_for_list = int(input("Введіть число для списку: "))
    my_list_two.append(numbers_for_list)
    numbers -= 1
result = min_element(my_list_two)
print("Мінімум у списку:", result)  

# TASK №3

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(list):
    count = 0
    for num in list:
        if is_prime(num):
            count += 1
    return count

my_list_three = []
numbers = int(input("Введіть кількість чисел для списк: "))
while numbers > 0:
    numbers_for_list = int(input("Введіть число для списку: "))
    my_list_three.append(numbers_for_list)
    numbers -= 1
result = count_primes(my_list_three)
print("Кількість простих чисел у списку:", result)

# TASK №4

def remove_elements(list, number_to_remove):
    count_removed = 0
    i = 0
    while i < len(list):
        if list[i] == number_to_remove:
            list.pop(i)
            count_removed += 1
        else:
            i += 1
    return count_removed

my_list_four = []
numbers = int(input("Введіть кількість чисел для списк: "))
while numbers > 0:
    numbers_for_list = int(input("Введіть число для списку: "))
    my_list_four.append(numbers_for_list)
    numbers -= 1
print("Ваш список", my_list_four)
number_to_remove = int(input("Введіть число для видатення зі списку: "))
result = remove_elements(my_list_four, number_to_remove)
print("Кількість видалених елементів:", result)
print("Список після видалення:", my_list_four)

# TASK №5

def merge_sort(arr):
    def merge(left, right):
        merged = []
        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        merged += left[left_index:]
        merged += right[right_index:]

        return merged

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

input_list = []
numbers = int(input("Введіть кітькість чисел для списку: "))
while numbers > 0:
    number_fro_list = int(input("Введіть чтисло для списку: "))
    input_list.append(number_fro_list)
    numbers -= 1
sorted_list = merge_sort(input_list)
print(sorted_list)

# TASK №6

def power_of_elements(nums, power):
    powered_nums = list(map(lambda x: x ** power, nums))
    return powered_nums

input_list = []
numbers = int(input("Введіть кількість чисел для списк: "))
while numbers > 0:
    numbers_for_list = int(input("Введіть число для списку: "))
    input_list.append(numbers_for_list)
    numbers -= 1
exponent = int (input("Введіть степвнь для списку: "))
result = power_of_elements(input_list, exponent)
print(result)