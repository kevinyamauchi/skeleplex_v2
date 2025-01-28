"""Data class for a skeleton graph."""

import json

import networkx as nx
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

    Parameters
    ----------
    graph : nx.Graph
        The skeleton graph.
    """

    _backend = "networkx"

    def __init__(self, graph: nx.Graph):
        self.graph = graph

    @property
    def backend(self) -> str:
        """Return the backend used to store the graph."""
        return self._backend

    @property
    def nodes(self):
        """Return a list of nodes."""
        return self.graph.nodes()

    @property
    def edges(self):
        """Return a list of edges."""
        return self.graph.edges()

    @property
    def edge_splines(self):
        """Return a list of edge splines."""
        edge_splines = {}
        for edge_start, edge_end, edge_data in self.graph.edges(data=True):
            edge_splines[(edge_start, edge_end)] = edge_data["spline"]
        return edge_splines

    def to_json_file(self, file_path: str):
        """Return a JSON representation of the graph."""
        graph_dict = nx.node_link_data(self.graph, edges="edges")
        object_dict = {"graph": graph_dict}

        with open(file_path, "w") as file:
            json.dump(object_dict, file, indent=2, default=skeleton_graph_encoder)

    @classmethod
    def from_json_file(cls, file_path: str):
        """Return a SkeletonGraph from a JSON file."""
        with open(file_path) as file:
            object_dict = json.load(file, object_hook=skeleton_graph_decoder)
        graph = nx.node_link_graph(object_dict["graph"], edges="edges")
        return cls(graph=graph)

    def __eq__(self, other: "SkeletonGraph"):
        """Check if two SkeletonGraph objects are equal."""
        if set(self.nodes) != set(other.nodes):
            # check if the nodes are the same
            return False
        elif set(self.edges) != set(other.edges):
            # check if the edges are the same
            return False
        else:
            return True
