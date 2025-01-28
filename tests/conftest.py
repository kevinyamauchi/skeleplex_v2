"""Fixtures for testing with Pytest."""

import numpy as np
import pytest

from skeleplex.data.skeleton_image import simple_t
from skeleplex.graph.image_to_graph import image_to_graph_skan
from skeleplex.graph.skeleton_graph import SkeletonGraph
from skeleplex.graph.spline import B3Spline


@pytest.fixture
def simple_t_skeleton_graph():
    """Return the simple T skeleton as a graph.

    Todo: replace with valid data rather than a processed object.
    """
    skeleton_image = simple_t()
    graph = image_to_graph_skan(skeleton_image=skeleton_image)

    return SkeletonGraph(graph=graph)


@pytest.fixture
def simple_spline():
    """Return a simple B3 spline.

    The spline goes in straight line from (0, 0, 0) to (1, 0, 0).
    """
    # make three points that go from x=0 to x=1
    points = np.array(
        [
            [0, 0, 0],
            [0.25, 0, 0],
            [0.5, 0, 0],
            [0.75, 0, 0],
            [1, 0, 0],
        ]
    )

    # fit a spline to the points
    return B3Spline.from_points(points)
