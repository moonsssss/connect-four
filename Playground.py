# fruits = ["apple", "banana", "cherry"]

# #print (fruits[2])

# for m in range(10):
#     for i in range(len(fruits)):
#         print(fruits[i])


fruits = [
    ["apple", "banana", "cherry"],
    ["mango", "pineapple", "watermellon"],
    ["orange", "kiwi", "pear"],
    ["plum", "grapes", "blueberry"],
    ]

fruits[1][2] = "orange"
fruits[2][0] = "watermellon"
print (fruits)