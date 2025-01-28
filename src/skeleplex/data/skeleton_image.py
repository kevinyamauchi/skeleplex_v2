"""Example skeleton images."""

import numpy as np
from skimage.draw import line


def simple_t() -> np.ndarray:
    """Make an image with a simple T skeleton.

    Returns
    -------
    np.ndarray
        A binary image with a simple T skeleton.
        The image has shape (20, 20, 20)
    """
    # node coordinates for each branch
    branch_coordinates = [
        [(10, 5), (10, 10)],
        [(10, 10), (10, 15)],
        [(10, 10), (15, 10)],
    ]

    # draw the image
    image = np.zeros((20, 20, 20), dtype=bool)

    for branch in branch_coordinates:
        rr, cc = line(*branch[0], *branch[1])
        image[10, rr, cc] = 1

    return image
