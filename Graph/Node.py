class Node:
    """
    A node in a search tree.
    Containing:
    - state of the node (regarding priority)
    - pointer to the parent
    - total path_cost to reach this node
    - global location (latitude, logitude)
    - depth of the current node
    """

    def __init__(self, state, parent=None, path_cost=0, location=None):
        """Create a search tree Node, derived from a parent by an action"""
        self.state = state
        self.parent = parent
        self.path_cost = path_cost
        self.location = location
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __lt__(self, other):
        """Returns True if the state of this node is less than the state of other"""
        return self.state < self.other

    def expand(self, graphProblem):
        """Return List of reachable nodes in one step from this node"""
        return [neighbour for neighbour in graphProblem.actions(self)]

    def solution(self):
        """Return the path from start_node to goal_node"""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

