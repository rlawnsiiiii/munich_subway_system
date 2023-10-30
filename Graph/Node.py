class Node:
    """
    A node in a search tree.
    Containing:
    - priority (the smaller the better)
    - pointer to the parent
    - total path_cost to reach this node
    - global location (latitude, logitude)
    - the ubahn-line
    - depth of the current node
    """

    def __init__(self, name, priority=0, parent=None, path_cost=0, location=None):
        """Create a search tree Node, derived from a parent by an action"""
        self.name = name
        self.priority = priority
        self.parent = parent
        self.path_cost = path_cost
        self.location = location
        self.line = set()
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def add_line(self, line):
        self.line.add(line)

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        """Returns True if the state of this node is less than the state of other"""
        return self.priority < other.priority

    def expand(self, graphProblem):
        """Return List of reachable nodes in one step from this node"""
        return [neighbour for neighbour in graphProblem.actions(self)]

    def solution(self):
        """Return the path from initial_node to goal_node"""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))
