# write a program to display
"""
*
**
***
****
*****
****
***
**
*
"""
n= 5
for num in range(n):
    for x in range(num):
        print("*", end="")
    print("")
for num in range(n, 0, -1):
    for x in range(num):
        print("*", end="")
    print('')

