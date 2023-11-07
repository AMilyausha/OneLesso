def multiply_table(n):
    table = []
    for i in range(1, n+1):
        for j in range(1, n+1):
             print(i,'*',j,'=',i*j)     
 

n = int(input("Введите число n: "))
table = multiply_table(n)

