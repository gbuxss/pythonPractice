# write a program to generate fibonacci series

initial_num = 0
second_num = 1
for num in range ( 10 ) :
    third_num = initial_num + second_num
    initial_num = second_num
    second_num = third_num
    print()
