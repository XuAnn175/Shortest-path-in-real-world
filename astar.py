import csv
import collections
edgeFile = 'edges.csv'
heuristicFile = 'heuristic.csv'


def astar(start, end):
    # Begin your code (Part 4)
    """
    1.read the edge file using open function and csv reader and store them in the graph
    2.read the heuristic file using open function and csv reader and store them in 'h'.  
      with 3 diffent destination,we store different heuristic dist. in h1,h2,h3,respectively
      later we assign the value to h according to the destination
    3.h[x] = y : the heuristic dist. from x to end is y
      g[x] : the dist. from starting point to x
      f[x] = g[x] + h[x] for every node x
    4.start A* Search:
      first we add start to 'opend' with its f equals 0
      in each step,we choose the node with smallest f value in 'opend' and remove it to 'closed'
      Then we calculate the f value of its neighbors : 
      if the neighbor is not in both lists,we calculate its g and f and put it in the 'opend'
      else : 
            the neighbor is in 'opend'  with a biggeer f(g) value : we update the value.
            the neighbor is in 'closed' with a biggeer f(g) value : we update the value and move it to 'opend'
    5.repeat 4. until we reach the destination
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
    h = collections.defaultdict(float)
    h1 = collections.defaultdict(float)
    h2 = collections.defaultdict(float)
    h3 = collections.defaultdict(float)
    with open(heuristicFile,newline='') as file:
        rows = csv.reader(file)
        cont = 1
        for row in rows:
            if(cont):
                cont = 0
                continue
            h1[row[0]] = row[1]
            h2[row[0]] = row[2]
            h3[row[0]] = row[3]   
    if end == 1079387396:
        h = h1
    elif end == 1737223506:
        h = h2
    elif end == 8513026827:
        h = h3
    opend = []
    opend_dist = []
    closed = []
    opend.append(start)
    opend_dist.append((0,start))
    f = collections.defaultdict(float) # f = g + h
    g = collections.defaultdict(float) # dist from start to the node
    pre = collections.defaultdict(int) 
    num_visited = 0
    f[start] = g[start] = 0
    while True:
        num_visited += 1
        selected_pair = min(opend_dist)
        opend_dist.remove(selected_pair)
        cur = selected_pair[1]
        opend.remove(cur)
        closed.append(cur)
        if cur == end:       
            break
        for neighbor in graph[cur]:
            tar = neighbor[0]
            if (tar not in opend) and (tar not in closed):
                opend.append(tar)
                g[tar] = g[cur] + neighbor[1]
                f[tar] = g[tar] + h[tar]
                pre[tar] = cur
                opend_dist.append((f[tar],tar))
            else:
                if (g[tar] > g[cur] + neighbor[1]) : 
                    g[tar] = g[cur] + neighbor[1]
                    f[tar] = g[tar] + h[tar]
                    pre[tar] = cur
                    if tar in closed:
                        closed.remove(tar)
                        opend.append(tar)
                        opend_dist.append((f[tar],tar))
    cur = end
    path = []
    while True: 
        path.append(cur)
        cur = pre[cur]
        if cur == start:
            break
    path.reverse()
    return path,f[end],num_visited
    # End your code (Part 4)


if __name__ == '__main__':
    path, dist, num_visited = astar(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
