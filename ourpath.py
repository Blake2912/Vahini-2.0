import osmnx as ox
import networkx as nx
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
import folium

def get_path(want_graph):



    ## Using boundbox
    north, south, east, west = 12.96768338736144,12.965518842636625,77.71393642911939,77.71046157295785
    # cmrit lat long bounds 0
    # north (float) – northern latitude of bounding box: 12.96768338736144
    # south (float) – southern latitude of bounding box: 12.965518842636625
    # east (float) – eastern longitude of bounding box: 77.71393642911939
    # west (float) – western longitude of bounding box: 77.71046157295785
    network_type = 'all_private' # "all_private", "all", "bike", "drive", "drive_service", "walk"

    G = ox.graph_from_bbox(
        north, south, east, west, 
        network_type=network_type, 
        simplify=True, 
        retain_all=False, 
        truncate_by_edge=False, 
        clean_periphery=True, 
        custom_filter=None)
    # Create a graph from OSM within some bounding box.
    def plot_graph(G):
        fig, ax = ox.plot_graph(G, show=False, close=False)
        return fig, ax

    # fig, ax = plot_graph(G)

    # Plot the graph and save it to a file
    # fig.savefig('graph1.png', dpi=300, bbox_inches='tight', pad_inches=0)


    # Renaming the existing nodes in the graph
    mapping = {3798918923:'cmrit_entrance',4159727902:'teacher_parking',4159727907:'volley_ball_court' }
    G = nx.relabel_nodes(G, mapping)


    # adding node basic_science and connecting it to the existing graph (from openstreet)
    # Basic Science Node
    G.add_node('basic_science',y= 12.96626, x=77.71211,street_count = 3) # we can add nodes like this..
    G.add_edge('teacher_parking','basic_science',length=300)

    # Ganesh statue node
    G.add_node('ganesha_statue',y=12.96598, x=77.71148, street_count=3)
    G.add_edge('basic_science','ganesha_statue',length=300)

    # Hostel Turn node
    G.add_node('hostel_turn',y=12.96696, x=77.71111, street_count=3)
    G.add_edge('ganesha_statue','hostel_turn',length=300)
    G.add_edge('volley_ball_court','hostel_turn',length=300)

    # NOTE:: After renaming of nodes use the relabled name and not the ID while creating new edges and nodes

    print([G.nodes[x] for x in G])

    fig, ax = plot_graph(G)

    # Plot the graph and save it to a file
    if want_graph:
        fig.savefig('graph.png', dpi=300, bbox_inches='tight', pad_inches=0)




    # finding shortest route
    # start_latlng = (12.9671086,77.7118638)
    # end_latlng = (12.966229089103756, 77.7121607793537)

    # start_latlng = G['cmrit_entrance']
    # end_latlng = G['basic_science']
    optimizer = 'length'
    # orig_node = ox.distance.nearest_nodes(G, start_latlng[1], start_latlng[0])
    # find the nearest node to the end location
    # dest_node = ox.distance.nearest_nodes(G, end_latlng[1], end_latlng[0])


    orig_node = 'volley_ball_court'
    dest_node = 'teacher_parking'

    #  find the shortest path
    shortest_route = nx.shortest_path(G, orig_node, dest_node, weight=optimizer)

    # print(shortest_route)
    shortest_route_map = ox.plot_route_folium(G, shortest_route)
    # shortest_route_map

    # # This saves it on html file to view it easily
    shortest_route_map.save('route.html')