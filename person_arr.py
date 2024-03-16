from person import Person
from range import get_5_range

# Пример строки в файле сохранения:
# Поляков: 0, 5
# После двоеточия сохраняются начальные значения оставшихся в мешке диапазонов

def read_arr(file):
    arr = []
    lst = file.readlines()
    for line in lst:
        name, bag = line.split(":")
        try:
            bag = [get_5_range(int(x)) for x in bag.split(",")]
        except Exception:
            bag = []
        arr.append(Person(name, bag))
    return arr

def write_arr(file, arr):
    for person in arr:
        person.print_person(file)

def reset_arr(arr):
    for p in arr:
        p.reset_bag()
    return arr
