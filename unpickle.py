import pickle
import osmnx as ox
import networkx as nx
filename = "output/geocode_tree.pkl"

with open(filename, "rb") as f:
    gt_loaded = pickle.load(f)

print(gt_loaded.nodes())
shortest_route = nx.shortest_path(
    gt_loaded, 'volley_ball_court', 'teacher_parking', weight='length')
print(shortest_route)

fig, ax = ox.plot_graph(gt_loaded, show=False, close=False)
fig.savefig('output/graph.png', dpi=300,
            bbox_inches='tight', pad_inches=0)
