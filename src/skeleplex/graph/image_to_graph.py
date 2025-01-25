"""Utilities to convert a skeleton image to a graph."""

import networkx as nx
import numpy as np
from skan.csr import Skeleton as SkanSkeleton
from skan.csr import summarize


def image_to_graph_skan(skeleton_image: np.ndarray):
    """Convert a skeleton image to a graph using skan."""
    # make the skeleton
    skeleton = SkanSkeleton(skeleton_image=skeleton_image)
    summary_table = summarize(skeleton, separator="_")

    # get all of the nodes
    # this might be slow - may need to speed up
    # source_nodes = set(summary_table["node_id_src"])
    # destination_nodes = set(summary_table["node_id_dst"])
    # all_nodes = source_nodes.union(destination_nodes)

    skeleton_graph = nx.MultiGraph(
        shape=skeleton.skeleton_shape, dtype=skeleton.skeleton_dtype
    )
    for row in summary_table.itertuples(name="Edge"):
        # Iterate over the rows in the table.
        # Each row is an edge in the graph
        index = row.Index
        i = row.node_id_src
        j = row.node_id_dst
        # Nodes are added if they don't exist so only need to add edges
        skeleton_graph.add_edge(
            i,
            j,
            **{
                "path": skeleton.path_coordinates(index),
            },
        )
    return skeleton_graph
