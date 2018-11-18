def arrayManipulation(n, m, queries):
    list = [0] * n
    
    for i in range(m):
        for j in range(queries[i][0], queries[i][1]):
            list[j] += queries[i][2]
            
    return max(list)

if __name__ == '__main__':
    
    n, m = input().split()
    n, m = int(n), int(m)

    queries = []

    for i in range(m):
        queries.append(list(map(int, input().rstrip().split())))
        queries[i][0] -= 1
        
    result = arrayManipulation(n, m, queries)
    print(result)