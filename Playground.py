# fruits = ["apple", "banana", "cherry"]

# #print (fruits[2])

# for m in range(10):
#     for i in range(len(fruits)):
#         print(fruits[i])


#fruits = [
  #  ["apple", "banana", "cherry"],
   # ["mango", "pineapple", "watermellon"],
   # ["orange", "kiwi", "pear"],
NUM_COLUMNS = 7
NUM_ROWS = 6

test = [1, 1, 1, 1, 2, 0, 1]
#       0  1  2  3  4  5  6

    
  
    #(test[col_i])
    #(test[col_i + 1])
    #(test[col_i + 2])  
    #(test[col_i + 3])
for col_i in range(4):
  print (test[col_i])
  print (test[col_i + 1])
  print (test[col_i + 2])  
  print (test[col_i + 3])
  
  if  test[col_i] == test[col_i + 1] == test[col_i + 2] == test[col_i + 3]:
      print("equal!")
    
  print()