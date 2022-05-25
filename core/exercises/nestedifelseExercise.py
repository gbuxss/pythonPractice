# write a program to find those numbers which are divisible by 7 and multiple of 5 betn 1500 and 2700
def factor():


    numlist = []
    for num in range(1500, 2701):
        if (num % 7 == 0) and (num % 5 == 0):
            numlist.append(num)
    print(numlist)

factor()
