for num in range(100,1000):
     bai = num // 100
     shi = num // 10 % 10
     ge = num % 10
     if(bai**3+shi**3+ge**3==num):
       print(num,end=' ')
