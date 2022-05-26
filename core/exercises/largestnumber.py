# write a program to find the largest number from given list

def largest_number():
    num = [2, 3, 6, 10, 7, 8]
    largest = num[0]
    for x in num:
        if x > largest:
            largest = x
    print(largest)


largest_number()
