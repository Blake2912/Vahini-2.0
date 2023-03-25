import cmritPath as cp
import osmnx as ox
import networkx as nx
import pickle

cf = cp.CmritField()


class GeocodeTree:
    def __init__(self):
        self.G = cf.graph()
        self.tree_count = 0

    def add_tree(self, coord):
        self.tree_count += 1
        tree_name = f"t-{self.tree_count}"
        nearest_node = ox.nearest_nodes(self.G, coord[0], coord[1])
        self.G.add_node(tree_name, x=coord[1], y=coord[0], street_count=3)
        self.G.add_edge(tree_name, nearest_node)
        print(self.G.nodes)
        return self.G

    def save_and_return(self):
        with open("output/geocode_tree.pkl", "wb") as f:
            pickle.dump(self.G, f)
        return self.G
