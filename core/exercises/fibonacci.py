# write a program to generate fibonacci series
def fibonacci():
    initial_num, second_num = 0, 1
    # verify that n is greater than zero
    n = int(input("Enter term to generate fibonacci series\n"))
    if n <= 0:
        print("Enter positive number!!")
    elif n == 1:
        print(initial_num)
    else:
        for num in range(n):
            print(f"{initial_num}\t", end="")
            third_num = initial_num + second_num
            initial_num = second_num
            second_num = third_num


fibonacci()
