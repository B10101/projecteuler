x = [1,2]
def fibo(n):
    y = x[n]+x[n-1]
    x.append(y)


for i in range(1,100):
    if x[i]<4000000:
        fibo(i)
    else:
        break
    
x.pop()
final = list(i for i in x if i%2==0)
print(sum(final))
