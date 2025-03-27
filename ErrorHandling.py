def f():
    try:
        n = int(input('Введите число: '))
        print(n**2)
    except ValueError:
        print("Число!")
        f()

f()