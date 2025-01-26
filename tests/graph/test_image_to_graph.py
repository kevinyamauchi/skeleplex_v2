""" "Tests for the skeleplex.graph.image_to_graph module."""

import networkx as nx

from skeleplex.data import simple_t
from skeleplex.graph.constants import NODE_COORDINATE_KEY
from skeleplex.graph.image_to_graph import image_to_graph_skan


def test_image_to_graph_skan():
    """Test converting a skeleton image to graph using skan."""
    skeleton_image = simple_t()
    graph = image_to_graph_skan(skeleton_image=skeleton_image)

    expected_node_coordinates = {(10, 10, 5), (10, 10, 10), (10, 10, 15), (10, 15, 10)}
    # make sure the node coordinates are correct
    node_attributes = nx.get_node_attributes(graph, name=NODE_COORDINATE_KEY)
    node_coordinates = {tuple(coordinate) for coordinate in node_attributes.values()}
    assert node_coordinates == expected_node_coordinates

    # make sure there is the correct number of edges
    assert graph.number_of_edges() == 3
