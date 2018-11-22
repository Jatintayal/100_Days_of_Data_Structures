if __name__ == '__main__':
    q = int(input())
    queue = []
    for _ in range(q):
        query = list(map(int, input().rstrip().split()))
        if query[0] == 1:
            queue.append(query[1])
        elif query[0] == 2:
            queue.pop(0)
        elif query[0] == 3:
            print(queue[0])