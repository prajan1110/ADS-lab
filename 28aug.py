#print the octal number system numbers from 00-77.
def octalno():
    for i in range(8): 
        for j in range(8):  
            print(i,j)
            
octalno()

#print the octal number system numbers from 000-777.
def octalno():
    for i in range(8): 
        for j in range(8):
            for k in range(8):  
                print(i,j,k)
            
octalno()

#print binary numbers from 0000 - 1111
def binary():
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    print(i,j,k,l)

binary()       