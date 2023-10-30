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
                line_list.append(node)
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

# save locations of each station
PATH = os.path.join(os.getcwd(), "Data") + os.path.sep
with open(PATH + "stops.csv", 'r', newline='', encoding="'utf-8-sig'") as file:
    csv_reader = csv.reader(file)
    rows = list(csv_reader)

    for node in nodes:
        for row in rows[1:]:
            information = row[0].split(";")
            if node.name == information[1] and information[4] == "1":
                print(f"location of {node.name} = {information[2], information[3]}")
                node.location = (float(information[2]), float(information[3]))
                break

    for node in nodes:
        if node.location is None:
            print(f"no location for {node.name}")

# visualize subway_graph
node_colors = {node: "white" for node in nodes}
node_positions = {node: node.location for node in nodes}
node_label_pos = {node: [node.location[0], node.location[1] - 3] for node in nodes}
edge_weights = {(start_node, dest_node): length for start_node, dest_info in subway_graph.graph_dict.items()
                for dest_node, length in dest_info.items()}
subway_graph_data = {"graph_dict": subway_graph.graph_dict,
                     "node_colors": node_colors,
                     "node_positions": node_positions,
                     "node_label_positions": node_label_pos,
                     "edge_weights": edge_weights
                     }
nb.show_map(subway_graph_data)
