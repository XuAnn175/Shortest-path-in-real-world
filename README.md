# Shortest-path-in-real-world  
In this project,we find the shortest path between 2 places in real world.  
We locate real world positions using [OpenStreetMap](https://www.openstreetmap.org/).  
Algorithm we use in this project : **BFS**, **DFS**, **Uniform Cost Search**, **A star Search**.  
Record the route and distance of the path found by each algorithm,and present the result using *Folium* package in python.  
## Result
- BFS  
![](https://imgur.com/oVB9zpp.jpg)  
- DFS  
![](https://imgur.com/QndvFHl.jpg)
- UCS  
![](https://imgur.com/SnB4531.jpg)
- A* Search  
![](https://imgur.com/55CEpAc.jpg)  
## Analysis  
1.In each test case,BFS takes the least number of nodes in the path.  
2.The distance,path,and # of nodes in the path found by UCS and A* are the same.  
3.The result of DFS is even worse when the roads on the map are complicated  
4.Compared with other 3 searches,DFS passes through the most # of nodes,and therefore takes the
longest distance.
