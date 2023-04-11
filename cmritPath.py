import osmnx as ox
import networkx as nx
import folium


class CmritField:
    def __init__(self):
        # Using boundbox
        # cmrit lat long bounds
        # north (float) – northern latitude of bounding box: 12.96768338736144
        # south (float) – southern latitude of bounding box: 12.965518842636625
        # east (float) – eastern longitude of bounding box: 77.71393642911939
        # west (float) – western longitude of bounding box: 77.71046157295785
        north, south, east, west = 12.96768338736144, 12.965518842636625, 77.71393642911939, 77.71046157295785
        network_type = 'all_private'

        self.G = ox.graph_from_bbox(
            north, south, east, west,
            network_type=network_type,
            simplify=True,
            retain_all=False,
            truncate_by_edge=False,
            clean_periphery=True,
            custom_filter=None)

        # Renaming the existing nodes in the graph
        new_names = {3798918923: 'cmrit_entrance',
                     4159727902: 'teacher_parking', 4159727907: 'volley_ball_court'}
        self.G = nx.relabel_nodes(self.G, new_names)
        G = self.G

        # adding node basic_science and connecting it to the existing graph (from openstreet)
        # Basic Science Node
        G.add_node('basic_science', y=12.96626, x=77.71211, street_count=3)

        # Ganesh statue node
        G.add_node('ganesha_statue', y=12.96598, x=77.71148, street_count=3)

        # Hostel Turn node
        G.add_node('hostel_turn', y=12.96696, x=77.71111, street_count=3)
        G.remove_node('cmrit_entrance')

        # print(list(G.nodes))
        # print(G.nodes['volley_ball_court']['y'])

    def add_edges(self):
        self.G.add_edges_from([('teacher_parking', 'basic_science'),
                               ('basic_science', 'teacher_parking'),
                               ('basic_science', 'ganesha_statue'),
                               ('ganesha_statue', 'basic_science'),
                               ('ganesha_statue', 'hostel_turn'),
                               ('hostel_turn', 'ganesha_statue'),
                               ('volley_ball_court', 'hostel_turn'),
                               ('hostel_turn', 'volley_ball_court')], length=300)

    def graph(self):
        return self.G
        # Plot the graph and save it to a file  in output folder

    def save_graph(self):
        fig, ax = ox.plot_graph(self.G, show=False, close=False)
        fig.savefig('output/graph.png', dpi=300,
                    bbox_inches='tight', pad_inches=0)

    def find_shortest_route(self, orig_node='teacher_parking', dest_node='hostel_turn', optimizer='length'):

        # finding shortest route
        # start_latlng = (12.9671086,77.7118638)
        # end_latlng = (12.966229089103756, 77.7121607793537)
        # start_latlng = G['cmrit_entrance']
        # end_latlng = G['basic_science']
        # orig_node = ox.distance.nearest_nodes(G, start_latlng[1], start_latlng[0])
        # find the nearest node to the end location
        # dest_node = ox.distance.nearest_nodes(G, end_latlng[1], end_latlng[0])
        G = self.G
        shortest_route = nx.shortest_path(
            G, orig_node, dest_node, weight=optimizer)  # find the shortest path
        print(shortest_route)
        shortest_route_map = ox.plot_route_folium(G, shortest_route)
        # This saves it on html file in output folder
        shortest_route_map.save('output/route.html')

    def return_all_nodes(self):
        """
        This function returns all the nodes present in the graph
        Returns : List
        """
        return list(self.G)

    def return_adjacent_nodes(self, current_node):
        """
        Params: str - current_node
        Returns: List
        """
        self.add_edges()  # Calling this function to connect all the newly created nodes
        try:
            return [n for n in self.G.neighbors(current_node)]
        except nx.exception.NetworkXError:
            return "Node not Found!"


# cmritPath = CmritField()
# cmritPath.save_graph()
# cmritPath.find_shortest_route()
