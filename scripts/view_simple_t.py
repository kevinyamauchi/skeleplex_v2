"""Script to view the simple T skeleton image."""

import json
from pprint import pprint

import napari
import networkx as nx

from skeleplex.data.skeleton_image import simple_t
from skeleplex.graph.image_to_graph import image_to_graph_skan
from skeleplex.graph.skeleton_graph import skeleton_graph_encoder

# create the image
image = simple_t()

# make the graph
skeleton_graph = image_to_graph_skan(image)
# print(skeleton_graph)

json_data = nx.node_link_data(skeleton_graph, edges="edges")
pprint(json_data)
pprint(json.dumps(json_data, indent=4, default=skeleton_graph_encoder))

viewer = napari.Viewer()
viewer.add_image(image, name="simple T skeleton")

if __name__ == "__main__":
    napari.run()
