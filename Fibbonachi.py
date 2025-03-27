'''def F(x):
    if x > 1:
        temp = F(x - 1) + F(x - 2)
        print(temp, end = " ")
        return temp
    else:
        print(1, end = " ")
        return 1

print(F(10))'''

sl = 1
pr = 0
for i in range(1, 100):
    if i == 1:
        print("1", end = ' ')
    else:
        ans = pr + sl
        pr = sl
        sl = ans
        print(ans, end = ' ')