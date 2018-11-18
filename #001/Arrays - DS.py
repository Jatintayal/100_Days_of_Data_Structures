def reverseArray(a):
    a.reverse()
    return a
    
if __name__ == '__main__':
    len = int(input())
    arr = [int(x) for x in input().split()]
    result = reverseArray(arr)
    for x in range(len):
        print(result[x], end = ' ')