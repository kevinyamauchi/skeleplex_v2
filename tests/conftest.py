"""Fixtures for testing with Pytest."""

import pytest

from skeleplex.data.skeleton_image import simple_t
from skeleplex.graph.image_to_graph import image_to_graph_skan
from skeleplex.graph.skeleton_graph import SkeletonGraph


@pytest.fixture
def simple_t_skeleton_graph():
    """Return the simple T skeleton as a graph.

    Todo: replace with valid data rather than a processed object.
    """
    skeleton_image = simple_t()
    graph = image_to_graph_skan(skeleton_image=skeleton_image)

    return SkeletonGraph(graph=graph)
