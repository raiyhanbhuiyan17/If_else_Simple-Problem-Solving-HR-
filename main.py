import math
import os
import random
import re
import sys



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Code is working')



# num = input("What's your name?")
# print(num)

#SOLUTION 1

# n = int(input("give a number: ").strip())

# if n % 2 == 1:
#     print("Weird")
# elif n % 2 == 0 and 2 <= n <= 5:
#     print("Not Weird")
# elif n % 2 == 0 and 6 <= n <= 20:
#     print("Weird")
# else:
#     print("Not Weird")


#SOLUTION 02

n = int(input("Give a number : ").strip())

if (n%2!=0):
    print("Weird");
elif((n%2==0) and (n in range(2, 5))):
    print("Not Weird");
elif ((n%2==0) and (n in range(6,20))):
    print("Weird");
else:
    print("Not Weird");

