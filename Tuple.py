data = (4, 6, 5, 3, 2, True, "hello")
print(data.count(6))
data2 = (5)
data3 = (input(), 5)
print(type(data2), type(data3), data3)
print(data[1:5])

datee = (4, 5, 2)
nums = [4, 5, "ee", False, 4.3, datee]
new_data = tuple(nums)

word = 'Hello world'
data4 = tuple(word)
print(data4)
print(new_data)