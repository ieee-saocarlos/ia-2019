def fun_a(n, i=1):
    if(i>n):
        return 0
    else:
        for c in range(i):
            print(f'{c+1}',end=' ')
        print('')
        return fun_a(n,i+1)


def fun_b(n, i=1):
    if(i>n):
        return 0
    else:
        for c in range(i):
            print(f'{i}',end=' ')
        print('')
        return fun_b(n,i+1)


def fun_c(n, i=1):
    if(i>n):
        return 0
    else:
        for c in range(n):
            if(i-c>0):
                print(f'{i-c}',end=' ')
            else:
                print(f'{c-i+2}', end=' ')
        print('')
        return fun_c(n,i+1)


n=int(input("Digite um número:"))
fun_a(n)
print('')
fun_b(n)
print('')
fun_c(n)
