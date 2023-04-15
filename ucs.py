import csv
import collections
edgeFile = 'edges.csv'


def ucs(start, end):
    # Begin your code (Part 3)
    """
    1.read the csv file using open function and csv reader and store them in the graph
    2.opend : store the nodes that are possible to be selected
      opend_dist : nodes that are possible to be selected with its distance from starting point
      clsoed : the nodes that have already been selected
      dist[x] = the distance from starting point to x
      pre[x] : to record the previous node of the traversal
    3.start UCS : 
      first we add start to 'opend'
      in each step,we choose the node with smallest dist. in 'opend' and remove it to 'closed'
      Then we calculate the dist. of its neighbors : 
      if the neighbor is not in both lists,we calculate its dist. and put it in the 'opend'
      else if the neighbor is in 'opend' and with a biggeer dist. value,we update the value.
    4.repeat 3. until we reach the destination
    5.recover the path using 'pre' list recursively
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
    
    opend = []
    opend_dist = []
    closed = []
    opend.append(start)
    opend_dist.append((0,start))
    dist = collections.defaultdict(float)
    dist[start] = 0.0
    pre = collections.defaultdict(list)
    num_visited = 0
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
            if (neighbor[0] not in opend) and (neighbor[0] not in closed):
                pre[neighbor[0]] = cur
                opend.append(neighbor[0])
                opend_dist.append((dist[cur]+neighbor[1],neighbor[0]))
                dist[neighbor[0]] = dist[cur] + neighbor[1]
            elif (neighbor[0] in opend):
                if(dist[neighbor[0]] > (dist[cur] + neighbor[1])):
                    dist[neighbor[0]] = (dist[cur] + neighbor[1])
                    pre[neighbor[0]] = cur
    cur = end  
    path = []
    while True:
        path.append(cur)
        if cur == start:
            break
        cur = pre[cur]
    path.reverse()
    return path,dist[end],num_visited
    # End your code (Part 3)


if __name__ == '__main__':
    path, dist, num_visited = ucs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
