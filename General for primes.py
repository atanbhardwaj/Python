n=int(input("Enter the number of primes required \n"))
i = 2
print(i)
i = 3
c=1
while c<n:
    for j in range(2, i):
        if i%j==0:
            break
    if i == j+1:
        print(i)
        c=c+1
    i=i+1
