def func(size,a,j):
    i=0
    if len(a)==0:
       return chr(96+size-j)
    else:
        n=len(a)//2+1
        return a[:n]+'-'+chr(size+96-j)+'-'+a[n-1:]

def print_rangoli(size):
    l=[chr(97+i) for i in range(0,size)]
    z=2*n-1+2*n-2
    for i in range(size):
        c=chr(size+96-i)
        a=''
        for j in range(i+1):
            a=func(size,a,j)
        print(a.center(z,'-'))
    for i in range(size-2,-1,-1):
        a=''
        for j in range(i+1):
            a=func(size,a,j)
        print(a.center(z,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)