#program for the follwing pattern: 
# 1
# 1 1
# 1 1 1
# 1 1 1 1 
def pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print(1,end=" ")
        print(" ")
n=4
pattern(n)
        
#Print the following pattern
# 2
# 2 2
# 2 2 2
# 2 2 2 2
# 2 2 2 2 2
def pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print(2,end=" ")
        print(" ")
n=5
pattern(n)
        
# Print the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
def pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i,end=" ")
        print(" ")
n=4
pattern(n)
        
# Print the following pattern
# 111111111
# 222222222
# 333333333
# 444444444
# 555555555
def pattern(n):
    for i in range(1,6):
        for j in range(1,9):
            print(i,end=" ")
        print(" ")
n=5
pattern(n)