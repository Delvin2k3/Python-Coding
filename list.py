my_list = [9, 2, 3, 4, 5]
del my_list [1]
print(my_list)

your_list = [10, 2, 3, 4, 5]
your_list.remove(3)
print(your_list)

combo_list = my_list + your_list
print(combo_list)

nested_list = [my_list, your_list]
print(nested_list)

my_list.sort()
print(my_list)

for i in range(1,4):
    my_list += []
print(my_list)    