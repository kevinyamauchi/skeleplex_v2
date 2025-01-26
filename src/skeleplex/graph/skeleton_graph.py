"""Data class for a skeleton graph."""

import numpy as np
from splinebox import Spline


def skeleton_graph_encoder(object_to_encode):
    """JSON encoder for the skeleton graph class.

    This function is to be used with the Python json.dump(s) functions
    as the `default` keyword argument.
    """
    if isinstance(object_to_encode, np.ndarray):
        return object_to_encode.tolist()
    elif isinstance(object_to_encode, Spline):
        spline_dict = object_to_encode._to_dict(version=2)
        if "__class__" in spline_dict:
            raise ValueError(
                "The Spline object to encode already has a '__class__' key."
            )
        spline_dict.update({"__class__": "splinebox.Spline"})
        return spline_dict
    raise TypeError(f"Object of type {type(object_to_encode)} is not JSON serializable")


class SkeletonGraph:
    """Data class for a skeleton graph.

    Attributes
    ----------
        nodes: A list of nodes in the graph.
        edges: A list of edges in the graph.
    """

    def __init__(self, graph):
        self.graph = graph

    @property
    def nodes(self):
        """Return a list of nodes."""
        pass

    @property
    def edges(self):
        """Return a list of edges."""
        pass

    @property
    def edge_splines(self):
        """Return a list of edge splines."""
        pass
