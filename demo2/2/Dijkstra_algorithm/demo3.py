import sys



items = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
# Function to find out which of the unvisited node 
# needs to be visited next
def to_be_visited():
  global visited_and_distance
  v = -10
  # Choosing the vertex with the minimum distance
  for index in range(number_of_vertices):
    if visited_and_distance[index][0] == 0 and (v < 0 or visited_and_distance[index][1] <= visited_and_distance[v][1]):
        v = index
  return v

# Creating the graph as an adjacency matrix 
# Creating topology
# vertices = [[0, 1, 1, 0],
#             [0, 0, 1, 0],
#             [0, 0, 0, 1],
#             [0, 0, 0, 0]]
# edges =  [[0, 3, 4, 0],
#           [0, 0, 0.5, 0],
#           [0, 0, 0, 1],
#           [0, 0, 0, 0]]

# vertices = [[0,1,0,1,0,0,0],
#             [0,0,1,0,1,0,0],
#             [0,0,0,0,0,1,1],
#             [0,0,0,0,1,0,0],
#             [0,0,0,0,0,1,0],
#             [0,0,0,0,0,0,1],
#             [0,0,0,0,0,0,0],]
# edges = [[0,2,0,3,0,0,0],
#          [0,0,5,0,4,0,0],
#          [0,0,0,0,0,4,3],
#          [0,0,0,0,5,0,0],
#          [0,0,0,0,0,2,0],
#          [0,0,0,0,0,0,1],
#          [0,0,0,0,0,0,0]]

# vertices = [[0,1,0,1,0,0,0],
#             [0,0,1,0,0,0,0],
#             [0,0,0,0,0,1,1],
#             [0,0,0,0,1,0,0],
#             [0,0,0,0,0,0,0],
#             [0,0,0,0,0,0,1],
#             [0,0,0,0,0,0,0],]
# edges = [[0,2,0,3,0,0,0],
#          [0,0,5,0,0,0,0],
#          [0,0,0,0,0,4,3],
#          [0,0,0,0,5,0,0],
#          [0,0,0,0,0,0,0],
#          [0,0,0,0,0,0,1],
#          [0,0,0,0,0,0,0]]

# vertices = [[0,1,1,1,1,0,0,0],
#             [1,0,1,0,1,0,0,0],
#             [1,1,0,1,0,0,0,1],
#             [1,0,1,0,0,1,0,0],
#             [1,1,0,0,0,0,1,1],
#             [0,0,0,1,0,0,0,1],
#             [0,0,0,0,1,0,0,1],
#             [0,0,1,0,1,1,1,0]
#           ]
# edges = [[0,4,5,2,12,0,0,0],
#          [4,0,3,0,1,0,0,0,0],
#          [5,3,0,1,0,0,0,13],
#          [2,0,1,0,0,11,0,0],
#          [12,1,0,0,0,0,6,9],
#          [0,0,0,11,0,0,0,8],
#          [0,0,0,0,6,0,0,7],
#          [0,0,13,0,9,8,7,0]]
vertices = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
edges = [[0, 7, 9999], [7, 0, 10], [9999, 10, 0]]
number_of_vertices = len(vertices[0])

# The first element of the lists inside visited_and_distance 
# denotes if the vertex has been visited.
# The second element of the lists inside the visited_and_distance 
# denotes the distance from the source.
visited_and_distance = [[0, 0]]
previous_node = [-1]
for i in range(number_of_vertices-1):
    visited_and_distance.append([0, sys.maxsize])
    previous_node.append(-1)


for vertex in range(number_of_vertices):
  # Finding the next vertex to be visited.
  to_visit = to_be_visited()
  for neighbor_index in range(number_of_vertices):
    # Calculating the new distance for all unvisited neighbors
    # of the chosen vertex.
    if vertices[to_visit][neighbor_index] == 1 and visited_and_distance[neighbor_index][0] == 0:
      new_distance = visited_and_distance[to_visit][1] + edges[to_visit][neighbor_index]
      # Updating the distance of the neighbor if its current distance
      # is greater than the distance that has just been calculated
      if visited_and_distance[neighbor_index][1] > new_distance:
        visited_and_distance[neighbor_index][1] = new_distance
        previous_node[neighbor_index] = to_visit
      # Visiting the vertex found earlier
      visited_and_distance[to_visit][0] = 1
      print(visited_and_distance)



i = 0 
# Printing out the shortest distance from the source to each vertex
print("Node  Cost  Previous")       
for distance in visited_and_distance:
  # print("The shortest distance of ",chr(ord('a') + i),\
  # " from the source vertex a is:",distance[1],",previous node is ",chr(ord('a') + previous_node[i]))
  print(items[i],"   ",distance[1],"   ",items[previous_node[i]])
  i = i + 1


for i in range(number_of_vertices):
  string = items[i]
  j = i
  temp = previous_node[i]
  while previous_node[j] != -1:
    j = previous_node[j]
    string =  items[j] + "->" + string
  print(i, string, visited_and_distance[i][1])