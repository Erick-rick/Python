#Fatorial


n = int(input('Digite um número :'))

def fatorial(n):
    if(n == 1):
        return n
    else:
        return n * fatorial (n-1)

print(fatorial(n))

