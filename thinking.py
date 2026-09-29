for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}",end=" ")
    print()



a = 0
for b in range(1,101):
    a = a + b
print(a)


for m in range(2,101):
    is_prime= True
    for n in range(2,m):
        if m%n == 0:
            is_prime = False
            break
    if is_prime:
        print(m)
   