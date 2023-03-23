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

        self.G.add_node(tree_name, x=coord[0], y=coord[1], street_count=3)

        print(self.G.nodes)

    def save_and_return(self):
        with open("output/geocode_tree.pkl", "wb") as f:
            pickle.dump(self.G, f)
        return self.G
