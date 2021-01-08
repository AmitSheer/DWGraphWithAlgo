# Graph Algorithms and Visualization

This repo is to load, save, manipulate, view and get data on graphs.
This repo was made for OOP course, assaignment 3.

## Usage 
To use this repo just:
1.  `git clone https://github.com/AmitSheer/DWGraphWithAlgo.git`
2. import the GraphAlgo class
3. two options:
  * if you have a graph ready to load: `algo = GraphAlgo({your graph})`
  * if you don't have a graph ready to load: 
    * `algo = GraphAlgo()`
    * `algo.load({path to graph})`
3. You are ready to start your journey in graph visualiztion and algorithms

## The problem
There was a need to do four things:
1. find the shortest path from one node to the other
2. find strongly connected component of a specific node
3. find all strongly connected components in graph
4. visualize graph

## Solution
The solution to the four problems respectively:
1. shortest path - implement  [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) was implemented\
![Dijkstra_Animation](https://user-images.githubusercontent.com/26150015/104007154-2d3d0600-51b0-11eb-8810-f781918ff473.gif)\
2+3. strongly connected component and strongly connected components - implement and use [Tarjan's strongly connected components algorithm](https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm)\
![Tarjan's_Algorithm_Animation](https://user-images.githubusercontent.com/26150015/104006689-7fc9f280-51af-11eb-8ed0-85d8c7c79bde.gif)
4. visualize graph - implement drawing method using [Marplotlib](https://matplotlib.org/index.html)
