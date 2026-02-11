import math
from operator import truediv


def task1():
    """
    Вычислить значения α и b по формулам:
    α = (sqrt(x) -
    b = tan(sqrt(x) - 1) - sqrt(2) - sqrt(y + x)
    """

    x = float(input("Введите значение x: "))
    y = float(input("Введите значение y: "))
    z = float(input("Введите значение z: "))

    # Проверка входных данных
    if y <= 0:
        y = float(input("Введите значение y: "))

    if x < 0:
        x = float(input("Введите значение x: "))

    # Вычисление a
    a = (math.sqrt(x)- math.pow(abs(y),1/4)) / (x - math.log2(y))

    # Вычисление b
    b = math.tan(math.sqrt(x - 1)) - math.pow(z,1/3) - math.pow(y,1/6) + x

    print(f"a = {a:.4f}")
    print(f"b = {b:.4f}")


#if __name__ == "__main__":task1()

def task2():
    x = float(input("Введите значение x: "))
    a,b,c=5,2,-5
    f=math.pow(x,b) + math.sqrt(c*x) / (b*x + a)

    print(f"b = {f:.4f}")

#if __name__ == "__main__":task2()

def task3():
    x = float(input("Введите значение x: "))
    f=math.pow(math.cos(math.sin(1/math.pow(x,2))),2)

    print(f"b = {f:.4f}")

#if __name__ == "__main__":task3()

def task4():
    a = float(input("Введите значение a: "))
    b = float(input("Введите значение b: "))
    alpha = float(input("Введите значение alpha: "))
    beta = float(input("Введите значение beta: "))

    alpha_d=math.degrees(alpha)
    beta_d = math.degrees(beta)
    s1=(a*b*math.sin(alpha_d))/2
    s2=(a*a*math.sin(alpha_d)*math.sin(beta_d)) / 2*math.sin(alpha_d + beta_d)

    print(f"s1 = {s1:.4f}")
    print(f"s2 = {s2:.4f}")

#if __name__ == "__main__":task4()

def task5():
    v1 = float(input("Введите значение v1: "))
    v2 = float(input("Введите значение v2: "))
    T = float(input("Введите значение T: "))
    S = float(input("Введите значение S: "))
    if (v1 or v2 or T or S) < 0:
        print('Ошибка в данных')
        return None


    total_speed = v1 + v2
    total_dist = total_speed * T
    dist = abs(S - total_dist)
    #return dist


    print(f"Расстояние между автомобилями через {T} часов: {dist} км")
#if __name__ == "__main__":task5()

def task6():
    # Ввод координат вершин треугольника
    x1 = float(input("Введите x1: "))
    y1 = float(input("Введите y1: "))

    x2 = float(input("Введите x2: "))
    y2 = float(input("Введите y2: "))

    x3 = float(input("Введите x3: "))
    y3 = float(input("Введите y3: "))

    # Длины сторон треугольника
    a = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    b = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    c = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # Проверка существования треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        print("Треугольник не существует.")
        return

    # Полупериметр
    p = (a + b + c) / 2

    # Площадь треугольника
    S = 0.5 * abs(
        x1 * (y2 - y3) +
        x2 * (y3 - y1) +
        x3 * (y1 - y2)
    )

    # Радиус вписанной окружности
    r = S / p

    # Вывод результата
    print(f"Радиус вписанной окружности r = {r:.4f}")

# Вызов функции
task6()

#r_example = task6(0, 0, 7, 0, 0, 3)
#print(f"Радиус вписанной окружности: {r_example}")  # Вывод: 1.0