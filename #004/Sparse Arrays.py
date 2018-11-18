def matchingStrings(strings, queries):
    res = []
    for i in range(len(queries)):
        res.append(0)
        for j in range(len(strings)):
            if strings[j] == queries[i]:
                res[i] += 1
    return res

if __name__ == '__main__':
    
    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)
    for i in range(len(res)):
        print(res[i])
