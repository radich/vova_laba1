from random import randint
from datetime import datetime


def bub_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(0, length-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


def nask(amin=20, amax=1000):
    input_value = 0
    if amin < 20:
        amin = 20
    if amax > 1000:
        amax = 1000
    while True:
        try:
            input_value = int(input("Введите цисловые значения от " + str(amin) + " до " + str(amax) + ": "))
        except ValueError:
            print("это не число, повторите ввод")
            continue
        if amin <= input_value <= amax:
            break
    return input_value


if __name__ == '__main__':
    src_arr = []
    array_length = nask()
    for i in range(array_length):
        src_arr.append(randint(10000, 99999))
    start_time = datetime.now()
    bub_sort(src_arr)
    print("Время выполнения: %.3f" % (datetime.now() - start_time).total_seconds())
    print("Длинна массива: " + str(array_length))
    print("Сумма первых 10ти: " + str(sum(src_arr[:10])))
    print("Сумма последних 10ти: " + str(sum(src_arr[-10:])))
