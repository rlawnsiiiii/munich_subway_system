import numpy as np


class GraphProblem:
    """
    The problem of searching a graph from one node to another
    Containing:
    - initial Node
    - goal Node
    - graph
    """

    def __init__(self, initial, goal, graph):
        """Creating a graph problem"""
        self.initial = initial
        self.goal = goal
        self.graph = graph

    def actions(self, start_node):
        """The actions at a graph node are its neighbours"""
        return list(self.graph.get(start_node).keys())

    def path_cost(self, cost_so_far, start_state, dest_state):
        return cost_so_far + (self.graph.get(start_state, dest_state) or np.inf)

    def h(self, node):
        """h function is straight-line distance from a node's state to goal"""


