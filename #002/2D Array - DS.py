def hourglassSum(arr):
    sum = []
    for y in range(4):
        for x in range(4):
            sum.append(arr[x][y] + arr[x + 1][y] + arr[x + 2][y] + arr[x + 1][y + 1] + arr[x][y + 2] + arr[x + 1][y + 2] + arr[x + 2][y + 2])
    return max(sum)
            

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    arr = list(map(list, zip(*arr)))

    sum = hourglassSum(arr)
    print(sum)