numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
elements_1 = numbers[0:4]
elements_2 = numbers[5:20]
sum_numbers = sum(elements_1)+sum(elements_2)
len_numbers = len(numbers)
numbers[4] = sum_numbers/len_numbers
print("Измененный список:", numbers)
