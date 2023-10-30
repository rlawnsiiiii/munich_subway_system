import os
import csv

from Graph.Graph import Graph
from Graph.Node import Node
import Graph.notebook as nb

LINES = ["U1", "U2", "U3", "U4", "U5", "U6"]
PATH = os.path.join(os.getcwd(), "Data", "stops") + os.path.sep
U1 = []
U2 = []
U3 = []
U4 = []
U5 = []
U6 = []
LINES_DICT = {"U1": U1, "U2": U2, "U3": U3, "U4": U4, "U5": U5, "U6": U6}
nodes = set()
nodes_names = set()

# create nodes for every subway_line
for line in LINES:
    with open(PATH + f'{line}.csv', 'r', newline='', encoding="'utf-8-sig'") as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
        for row in rows:
            node_name = row[0]
            line_list = LINES_DICT.get(line)

            if node_name in nodes_names:  # Node already created
                node = nb.get_node_by_node_name(nodes, node_name)
                node.add_line(line)
                line_list.append(Node)
            else:
                node = Node(name=node_name)
                node.add_line(line)
                line_list.append(node)
                nodes.add(node)
                nodes_names.add(node_name)


# create graph out of nods
subway_graph = Graph(directed=False)

for line in LINES_DICT.values():
    for node in line:
        for i in range(len(line)):
            # create a connection aka edge to neighbouring stations
            if i < len(line) - 1:
                print(f"connecting from {line[i].name}")
                print(f"connecting to {line[i + 1].name}")
                subway_graph.connect(line[i], line[i + 1])


