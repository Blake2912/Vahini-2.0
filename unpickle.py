import pickle
import osmnx as ox
import networkx as nx
filename = "output/geocode_tree.pkl"

with open(filename, "rb") as f:
    gt_loaded = pickle.load(f)

print(gt_loaded.nodes())
shortest_route = nx.shortest_path(
    gt_loaded, 't-1', 'volley_ball_court', weight='length')
print(shortest_route)
