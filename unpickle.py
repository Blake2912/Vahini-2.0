import pickle
filename = "output/geocode_tree.pkl"

with open(filename, "rb") as f:
    gt_loaded = pickle.load(f)

print(gt_loaded.nodes())
