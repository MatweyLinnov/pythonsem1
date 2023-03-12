norm_a = [100,1000]
a = int(input("Введите трехзначное число число: "))
if a >= norm_a[0] and a <=norm_a[1]:
    summa = 0
    while a > 0:
        x = a % 10
        summa += x 
        a //= 10
    print(summa)
else:
    print("Попробуй еще раз")        
