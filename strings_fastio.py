import sys
input = sys.stdin.read
output = sys.stdout.write

def main():
    data = input().splitlines()
    n = int(data[0])

    graph = {}
    strings = data[1:n + 1]  # Read strings from the input

    for i in range(n):
        graph[i] = i

    def find_botton(graph, i):
        if graph[i] == i:
            return i
        return find_botton(graph, graph[i])

    last_a = 0

    for i in range(n - 1):
        a, b = map(int, data[n + 1 + i].split())
        a -= 1
        b -= 1

        graph[find_botton(graph, a)] = b
        last_a = a

    response = strings[last_a]
    curr = last_a

    while graph[curr] != curr:
        curr = graph[curr]
        response += strings[curr]

    output(response + "\n")

if __name__ == "__main__":
    main()
