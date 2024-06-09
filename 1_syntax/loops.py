import math

i = 1
while i < 10:
    print(i)
    i += 1
else:
    print("Loop is finished: last value of i =", i)

# for loop
nums = [21, 2, 4, 7, 5]

for num in nums:
    print("square root of ", num, math.sqrt(num))

text = "Hello World"
for char in text:
    print(char)
