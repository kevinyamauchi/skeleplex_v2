"""Data class for a skeleton graph."""

import numpy as np
from splinebox import Spline
from splinebox.spline_curves import _prepared_dict_for_constructor


def skeleton_graph_encoder(object_to_encode):
    """JSON encoder for the networkx skeleton graph.

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


def skeleton_graph_decoder(json_object):
    """JSON decoder for the networkx skeleton graph.

    This function is to be used with the Python json.load(s) functions
    as the `object_hook` keyword argument.
    """
    if "__class__" in json_object:
        # all custom classes are identified by the __class__ key
        if json_object["__class__"] == "splinebox.Spline":
            json_object.pop("__class__")
            spline_kwargs = _prepared_dict_for_constructor(json_object)
            return Spline(**spline_kwargs)
    return json_object


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
