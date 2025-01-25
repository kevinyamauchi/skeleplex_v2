"""Script to view the simple T skeleton image."""

import napari

from skeleplex.data.skeleton_image import simple_t

# create the image
image = simple_t()

viewer = napari.Viewer()
viewer.add_image(image, name="simple T skeleton")

if __name__ == "__main__":
    napari.run()
