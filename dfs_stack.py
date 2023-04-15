import csv
import collections
edgeFile = 'edges.csv'


def dfs(start, end):
    # Begin your code (Part 2)
    """
    1.read the csv file using open function and csv reader and store them in the graph
    2.graph[x] = (y,z) means that the dist. between x and y is z
    3.stack : for DFS processing
      vis : to store visited nodes
      pre : to record the previous node of the traversal
    4.start DFS : in each step we choose the node at the top of stack,call it 'cur'.
      Then we traverse through the neighbors of cur,if it hasn't been visited,add it to stack.
    5.repeat 4. until the stack is empty
    6.recover the path using 'pre' list recursively
    """
    graph = collections.defaultdict(list)
    with open(edgeFile, newline='') as file:
        rows = csv.reader(file)
        cont = 1
        for row in rows:
            if(cont):
                cont = 0
                continue
            graph[int(row[0])].append([int(row[1]), float(row[2])])
    stack = []
    
    num_visited = 0
    vis = set()
    vis.add(start)
    stack.append(start)
    pre = collections.defaultdict(list)
    while (len(stack) > 0) :
        cur = stack.pop()
        num_visited += 1
        if cur == end:
            break
        for to in graph[cur]:
            if to[0] not in vis:
                vis.add(to[0])
                stack.append(to[0])
                pre[to[0]] = [cur,to[1]]
    dist = 0.0
    cur = end
    path = []
    while True:
        if cur == start:
            path.append(cur)
            break
        dist += pre[cur][1]
        cur = pre[cur][0]
        path.append(cur)
    path.reverse()
    return path,dist,num_visited
    # End your code (Part 2)


if __name__ == '__main__':
    path, dist, num_visited = dfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
