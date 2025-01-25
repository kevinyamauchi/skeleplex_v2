"""Script to view the simple T skeleton image."""

import napari

from skeleplex.data.skeleton_image import simple_t
from skeleplex.graph.image_to_graph import image_to_graph_skan

# create the image
image = simple_t()

# make the graph
summary_table = image_to_graph_skan(image)
print(summary_table)

viewer = napari.Viewer()
viewer.add_image(image, name="simple T skeleton")

if __name__ == "__main__":
    napari.run()
