# Write python programs to print the following patterns
# See YouTube playlist -
# https://www.youtube.com/playlist?list=PL7ersPsTyYt3VGSO8E-XL3dPNg17LK0yk

# Question: 1

"""

*
* *
* * *
* * * *

"""

for i in range(1, 5):
    for j in range(1, 5):
        if j <= i:
            print("*", end=" ")
        else:
            print(" ", end="")
    print()

# Question: 2

"""

      *
    * *
  * * *
* * * *

"""

for i in range(1, 5):
    for j in range(1, 5):
        if j >= 5 - i:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()

# Question: 3

"""

* * * *
* * *
* *
*

"""

for i in range(1, 5):
    for j in range(1, 5):
        if j <= 5 - i:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()

# Question: 4

"""

* * * *
  * * *
    * *
      *

"""
for i in range(1, 5):
    for j in range(1, 5):
        if j >= i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# Question: 5

"""
   *
  ***
 *****
*******
    

"""
for i in range(1, 5):
    for j in range(1, 8):
        if j >= (5 - i) and j <= (3 + i):
            print("*", end='')
        else:
            print(" ", end='')
    print()

# Question: 6

"""   

* * * * * * *
  * * * * *
    * * *
      *

"""
for i in range(1, 5):
    for j in range(1, 8):
        if j >= i and j <= (8 - i):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
# Question: 7

"""

* * * * * * * * 
* * *     * * *
* *         * *
*             *

"""
for i in range(1, 5):
    for j in range(1, 8):
        if j <= (5 - i) or j >= (3 + i):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()

# Question: 8

"""

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""
for i in range(1, 6):
    for j in range(1, 6):
        if j <= i:
            print(j, end=" ")
        else:
            print(" ", end="")
    print()

# Question: 9

"""

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

"""
for i in range(1, 6):
    k = 6 - i
    for j in range(1, 6):
        if j <= 6 - i:
            print(k, end=' ')
            k = k - 1
        else:
            print(" ", end=' ')
    print()
