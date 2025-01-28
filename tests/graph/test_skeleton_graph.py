"""Tests for the SkeletonGraph class."""

from skeleplex.graph.skeleton_graph import SkeletonGraph


def test_skeleton_graph_equality(simple_t_skeleton_graph):
    """Test the equality of two SkeletonGraph objects."""
    assert simple_t_skeleton_graph == simple_t_skeleton_graph

    # check that changing the nodes makes the graphs not equal
    modified_node_graph = simple_t_skeleton_graph.graph.copy()
    modified_node_graph.add_node(9000)
    new_skeleton_graph = SkeletonGraph(graph=modified_node_graph)
    assert simple_t_skeleton_graph != new_skeleton_graph

    # check that changing the edges makes the graphs not equal
    modified_edge_graph = simple_t_skeleton_graph.graph.copy()
    modified_edge_graph.add_edge(0, 15)
    new_skeleton_graph = SkeletonGraph(graph=modified_edge_graph)
    assert simple_t_skeleton_graph != new_skeleton_graph


def test_skeleton_graph_json_round_trip(simple_t_skeleton_graph, tmp_path):
    """Test writing and reading a SkeletonGraph object"""
    # write the graph to a file
    file_path = tmp_path / "test.json"
    simple_t_skeleton_graph.to_json_file(file_path)

    # read the graph from the file
    new_skeleton_graph = SkeletonGraph.from_json_file(file_path)

    # check that the graphs are equal
    assert simple_t_skeleton_graph == new_skeleton_graph
