if __name__ == '__main__':
    
    n, d = input().split()
    n, d = int(n), int(d)
    a = list(map(int, input().rstrip().split()))
    
    for i in range(d):
        b = a[1:n]
        b.append(a[0])
        a = b
        
    for i in range(n):
        print(a[i], end = ' ')