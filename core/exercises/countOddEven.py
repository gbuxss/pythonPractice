# write a program count odd/ even number in a list
def count(number_list) :
    odd = 0
    even = 0
    for num in numbers_list :
        if num % 2 == 0 :
            even += 1
        else :
            odd += 1
    print ( f"odd count :{odd}" )
    print ( f"even count :{even}" )


numbers_list = [5 , 3 , 5 , 3 , 7 , 8 , 9 , 4 , 6 ]

count (numbers_list)
