graph = {}

graph['start'] = {
    'a': 6,
    'b': 2
}

graph['a'] = {
    'fin': 1
}

graph['b'] = {
    'a': 3,
    'fin': 5
}

graph['fin'] = {}

# print(graph)

infinity = float('inf')
costs = {
    'a': 6,
    'b': 2,
    'fin': infinity
}

# print(costs)

parents = {
    'a': 'start',
    'b': 'start',
    'fin': None
}

# print(parents)

processed = []


def find_lowed_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowed_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowed_cost_node(costs)
    print(graph)
    print(costs)
    print(parents)
    print(processed)

# O(V*V+E) = O(V^2)
