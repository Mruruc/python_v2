import math

# while loop
i = 1
while i < 10:
    print(i, sep=",", end=" ")
    i += 1
else:
    print("\nLoop is finished: last value of i =", i)

# for loop
nums = [21, 2, 4, 7, 5]

for num in nums:
    print(num, math.sqrt(num), sep=" => ", end=" | ")
print()

for i in range(5):
    print(nums[i], end=" ")
print()

text = "Hello World"
for char in text:
    print(char, sep=",", end=" ")
print()

# range() function => range(start, stop, step)
print(list(range(10)))        # 0 to 9
print(list(range(1, 11)))     # 1 to 10
print(list(range(1, 11, 2)))  # 1 to 10 with step 2
print(list(range(10, 0, -1))) # 10 to 1 with step -1



# enumerate() function
userIds = ["user1", "user2", "user3"]

for index, userId in enumerate(userIds):
    print(index, userId, sep=" => ", end=" | ")
print()