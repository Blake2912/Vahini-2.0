import cmritPath as cp
import osmnx as ox
import networkx as nx
import pickle

cf = cp.CmritField()


class GeocodeTree:
    def __init__(self):
        self.G = cf.graph()
        self.tree_count = 0
        self.tree_list = []

    def add_tree(self, coord, start_node, end_node):
        self.start_node = start_node
        self.end_node = end_node
        self.tree_count += 1
        tree_name = f"t-{self.tree_count}"
        self.tree_list.append(tree_name)
        self.G.add_node(tree_name, x=coord[1], y=coord[0], street_count=3)
        # self.G.add_edge(tree_name, nearest_node)

        print(self.G.nodes)
        return self.G

    def save_and_return(self):
        for i in range(len(self.tree_list)-1):
            self.G.add_edge(self.tree_list[i], self.tree_list[i+1],length=200)
            self.G.add_edge(self.tree_list[i+1], self.tree_list[i],length=200)

        self.G.add_edge(self.tree_list[0], self.start_node,length=200)
        self.G.add_edge(self.start_node, self.tree_list[0],length=200)
        self.G.add_edge(self.tree_list[-1], self.end_node,length=200)
        self.G.add_edge(self.end_node, self.tree_list[-1],length=200)
        with open("output/geocode_tree.pkl", "wb") as f:
            pickle.dump(self.G, f)
        self.tree_list = []
        cf.save_graph()
        return self.G
