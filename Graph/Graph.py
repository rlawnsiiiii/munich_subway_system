class Graph:
    """
    A graph consisting of nodes and edges with specified lengths.
    ex)
        g = Graph({'A': {'B': 1, 'C': 2})
    constructs a graph with 3 nodes, A, B, and C, with an edge of length 1 from
    A to B, and an edge of length 2 from A to C.
    keys := start nodes of edges
    values := destination nodes of edges
    """

    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    def make_undirected(self):
        """Transforming a digraph into an undirected graph by adding symmetric edges"""
        for start_node in list(self.graph_dict.keys()):
            for (dest_node, length) in self.graph_dict[start_node].items():
                self.connect_single(dest_node, start_node, length)

    def connect_single(self, start_node, dest_node, length=1):
        """Add an edge from start_node to dest_node"""
        self.graph_dict.setdefault(start_node, {})[dest_node] = length
        pass

    def connect(self, start_node, dest_node, length=1):
        """Add an edge from start_node to dest_node.
         If the graph is directed, add an edge in the inverse direction too"""
        self.connect_single(start_node, dest_node, length)
        if not self.directed:
            self.connect_single(dest_node, start_node, length)

    def get(self, start_node, dest_node=None):
        f"""
        .get(start_node_dest_node) returns the length of the edge or None
        .get(start_node) returns a dictionary of entries (dest_node : length), possibly empty dict.
        """
        edges = self.graph_dict.setdefault(start_node, {})
        if dest_node is None:
            return edges
        else:
            return edges.get(dest_node)

    def nodes(self):
        """Return a list of all nodes in the graph"""
        start_nodes = set([start_node for start_node in self.graph_dict.keys()])
        dest_nodes = set([dest_node
                          for dest_entry in self.graph_dict.values()
                          for dest_node, length in dest_entry.items()])
        nodes = start_nodes.union(dest_nodes)
        return list(nodes)
