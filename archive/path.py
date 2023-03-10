import osmnx as ox
import networkx as nx

# define the start and end locations in latlng
# start_latlng = (37.78497,-122.43327)
start_latlng = (12.966841, 77.711988)
# end_latlng = (37.78071,-122.41445)
end_latlng = (12.967419, 77.713700)
# location where you want to find your route
place = 'Bengaluru, Karnataka India'
# find shortest route based on the mode of travel
mode = 'walk'        # 'drive', 'bike', 'walk'
# find shortest path based on distance or time
optimizer = 'time'        # 'length','time'
# create graph from OSM within the boundaries of some 
# geocodable place(s)
graph = ox.graph_from_place(place, network_type = mode)
# find the nearest node to the start location
orig_node = ox.distance.nearest_nodes(graph, start_latlng[1], start_latlng[0])
# find the nearest node to the end location
dest_node = ox.distance.nearest_nodes(graph, end_latlng[1], end_latlng[0])
#  find the shortest path
shortest_route = nx.shortest_path(graph, orig_node, dest_node, weight=optimizer)

print(shortest_route)
shortest_route_map = ox.plot_route_folium(graph, shortest_route)
# This saves it on html file to view it easily
shortest_route_map.save('route.html')
