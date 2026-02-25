import math

def task1():
    def is_perfect(n):
        if n <= 0:
            return False
        res = 0
        # перебор делителей
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                res += i
        return res == n

    def is_palin(n):
        if not (100 <= n <= 999):
            return False
        s = str(n)
        return s == s[::-1]

    print("Проверка чисел. Для выхода введите 'q'")

    while True:
        val = input("Введите число: ")
        if val == 'q' or val == 'й':
            break

        try:
            number = int(val)
        except:
            print("Нужно ввести целое число!")
            continue

        if is_perfect(number):
            print(f"{number} - совершенное")
        else:
            print(f"{number} - нет")

        if is_palin(number):
            print(f"{number} - палиндром из 3 цифр")
        else:
            print(f"{number} - не палиндром")
#3
def task2():
    def f(x):
        if x >= 0:
            return 2 * (x ** 2 - 5) - x
        else:
            return math.tan(x) - 10

    # тест:
    print(f"f(3) = {f(3):.4f}")
    print(f"f(-pi/4) = {f(-math.pi / 4)}")
    print(f"f(0) = {f(0)}")
    print(f"f(-2) = {f(-2)}")
#1
def task3():
    def decimal_to_bin(decimal_fract, lim=10):
        if decimal_fract == 0:
            return "0"

        # Разделяем на целую и дробную часть
        int_part = int(decimal_fract)
        fract_part = decimal_fract - int_part

        # Перевод целой части
        if int_part == 0:
            bin_int = "0"
        else:
            bin_int = ""
            temp_int = int_part
            while temp_int > 0:
                bin_int = str(temp_int % 2) + bin_int
                temp_int //= 2

        # Перевод дробной части
        if fract_part == 0:
            bin_fract = ""
        else:
            bin_fract = "."
            for _ in range(lim):
                fract_part *= 2
                bit = int(fract_part)
                bin_fract += str(bit)
                fract_part -= bit
                if fract_part == 0:
                    break

        return  bin_int + bin_fract

        # тестиинг:

    print(f"6.625 в двоичной: {decimal_to_bin(-6.625)}")
    print(f"0.5 в двоичной: {decimal_to_bin(0.5)}")
    print(f"3.14 в двоичной (точность 10): {decimal_to_bin(3.14)}")
#1
def task5():

    def calc(x):
        data = []

        # sin
        data.append((math.sin(x), 'sin(x)'))

        # cos/x
        if x != 0:
            val = math.cos(x) / x
            data.append((val, 'cos(x)/x'))

        # ln
        if x > 0:
            data.append((math.log(x), 'ln(x)'))

        # сортировка
        data.sort(key=lambda x: x[0], reverse=True)

        for v, name in data:
            print(f"{name} = {round(v, 4)}")

    while True:
        inp = input("x (или q): ")
        if inp == 'q': break
        try:
            calc(float(inp))
        except:
            print("ошибка в числе")
#1
def task6():
    cost = input("введите цену пк: ")
    zp=input("введите цену з\п: ")

    def months_to_buy(cost, zp,):
        COST_UP = 1.0315 #пк дорожает
        ZP_UP = 1.05 # зп увеличивается

        p = float(cost)
        s = float(zp)
        total = 0.0
        m = 0

        if total >= p:
            return 0

        while total < p:
            m += 1
            total += s
            if total >= p: break

            p = p * COST_UP  # дорожает
            if m % 3 == 0:
                s = s * ZP_UP  # прибавка раз в квартал
        return m
    print(f"Копить месяцев: {months_to_buy(cost, zp)}")
#1
def task7():
    def get_time(temp):
        # таблица из задания
        table_cold = (
            (13.0, 1), (14.0, 2), (15.0, 3), (16.0, 4), (17.0, 5), (18.0, 6), (19.0, 7),
        )
        table_hot = (
            (28.5, 7), (29.0, 6), (29.5, 5.5), (30.0, 5), (30.5, 4), (31.0, 3),
            (31.5, 2.5), (32.0, 2), (32.5, 1)
        )

        if table_cold[-1][0] < temp < table_hot[0][0]:
            return 8.0

        if temp <= table_cold[-1][0]:
            for t, h in table_cold:
                if temp <= t:
                    res = h
                    break
            if temp < table_cold[1][0]: res = table_cold[0][1]
        elif temp >= table_hot[0][0]:
            # смотрим с горячя
            for t, h in sorted(table_hot, reverse=True):
                if temp >= t:
                    res = h
                    break
            if temp > table_hot[-1][0]: res = table_hot[-1][1]

        return float(res)

    t_in = input("Градусы в офисе: ")
    try:
        t = float(t_in)
        print(f"Работать нужно: {get_time(t)} ч.")
    except:
        print("напишите число")
#1
def task8():
    def sum_series(x: float, n: int):

        current_sum = 0.0

        for k in range(n):
            term = (x + k) ** 2
            current_sum += term

        return current_sum

    while True:
        x_ = input("Введите начальное значение x (может быть дробным): ")
        try:
            x = float(x_)
            break
        except ValueError:
            print("Ошибка ввода: x должно быть числом.")

    while True:
        n_ = input("Введите количество членов n (целое число, n >= 1): ")
        try:
            n = int(n_)
            if n >= 1:
                break
            else:
                print("Ошибка ввода: n должно быть целым числом, большим или равным 1.")
        except ValueError:
            print("Ошибка ввода: n должно быть целым числом.")

    result = sum_series(x, n)
    print(f"Сумма первых {n} членов ряда S_n равна: {result}")
    
if __name__ == "__main__":
    #task1()
    #task2()
    #task3()
    #task5()
    #task6()
    #task7()
    task8()
