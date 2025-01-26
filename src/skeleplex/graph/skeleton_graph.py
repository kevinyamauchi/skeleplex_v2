"""Data class for a skeleton graph."""


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
