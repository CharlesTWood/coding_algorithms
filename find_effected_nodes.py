nodes = [1,2,3,4,5,6,7,8,9]
edges = [0,0,4,5,6,7,0,0,0]

def find_impacted_downstream_nodes(nodes, edges, impacted_node):
    impacted_nodes = []

    for i, node in enumerate(nodes):
        if node == impacted_node:
            impacted_nodes.append(edges[i] if edges[i] != 0 else None)
            impacted_nodes.extend(find_impacted_downstream_nodes(nodes, edges, edges[i]))
    return impacted_nodes

print(find_impacted_downstream_nodes(nodes, edges, 3))