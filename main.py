# Строки
# Исключения
# Модули и их применение
# Форматирование строки
# %s - строка, %f - дробь, %d - целое

name = 'Дмитрий'
age = 19
height = 141.99

f_string = '%15s,\nвозраст: %2d лет,\nрост: %6.1f см.' % (name, age, height)
print(f_string)
