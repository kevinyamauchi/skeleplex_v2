"""Tests for the SkeletonGraph class."""

import networkx as nx

from skeleplex.graph.skeleton_graph import SkeletonGraph, get_next_node_key


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


def test_skeleton_graph_to_directed(simple_t_skeleton_graph):
    """Test converting a SkeletonGraph to a directed graph."""
    directed_graph = simple_t_skeleton_graph.to_directed(origin=0)
    assert directed_graph.is_directed()

    # check that the directed graph has the same nodes
    assert set(directed_graph.nodes) == set(simple_t_skeleton_graph.graph.nodes)

    # check if the origin node has no incoming edges
    assert len(list(directed_graph.in_edges(0))) == 0

    # check edge directionality
    for u, v in directed_graph.edges:
        assert all(
            edges in directed_graph.out_edges(u) for edges in directed_graph.in_edges(v)
        )


def test_get_next_node_id():
    """Test the get_next_node_id function."""
    # initialize an empty graph
    graph = nx.Graph()

    assert get_next_node_key(graph) == 0

    # add a node to the graph
    graph.add_node(0)
    assert get_next_node_key(graph) == 1

    # add multiple nodes to the graph
    graph.add_nodes_from([10, 23, 65])
    assert get_next_node_key(graph) == 66
