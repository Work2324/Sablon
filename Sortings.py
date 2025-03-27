import random
#import os

#Вставка, по возрастанию
def Insert(s):
    for i in range(len(s) - 1):
        t = -52
        minn = s[i]
        for k in range(i, len(s)):
            if s[k] < minn:
                minn = s[k]
                t = k
        if t != -52:
            s[t], s[i] = s[i], s[t]
    return s


#пузырек, по возрастанию
def Bouble(s):
    t = True
    i = 0
    while t == True and i < len(s):
        t = False
        for k in range(len(s) - 1, i, - 1):
            if s[k] < s[k - 1]:
                s[k], s[k - 1] = s[k - 1], s[k]
                t = True
        i += 1
    return s


print('1 - Проверка', '2 - Меню', sep = '\n')
temp = int(input())
if temp == 1:
    #проверка
    true, false = 0, 0
    for i in range(100000):
        n = random.randint(10, 100)
        s = []
        for i in range(n):
            s.append(random.randint(-1000, 1000) + random.random())
        if Bouble(s) == sorted(s):
            true += 1
        else:
            false += 1

    print(f'true - {true} | false - {false}')
if temp == 2:
#Меню выбора
    temp = 1
    while temp != 0:
        print('0 - Выход', '1 - Вставка', '2 - Пузырек', sep='\n')
        temp = int(input())
        if temp != 0:
            #список, рандом
            n = random.randint(10, 30)
            s = []
            for i in range(n):
                s.append(random.randint(0, 100))
            print(*s)

            if temp == 1: print(*Insert(s))
            if temp == 2: print(*Bouble(s))