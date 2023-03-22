import cmritPath as cp
import osmnx as ox
import networkx as nx

cf = cp.CmritField()


class GeocodeTree:
    def __init__(self):
        self.G = cf.graph()

    def add_tree(self, coord):
        self.G.add_node('t-01', x=coord[0], y=coord[1], street_count=3)
        print(self.G.nodes)
