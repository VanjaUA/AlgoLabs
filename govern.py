from collections import defaultdict
import os

def topological_sort(graph):
    edges = defaultdict(int)

    for node in graph:
        for neighbor in graph[node]:
            edges[neighbor] += 1

    stack = sorted([node for node in graph if edges[node] == 0])
    result = []

    while stack:
        current_node = stack.pop(0)

        for neighbor in graph[current_node]:
            edges[neighbor] -= 1
            if edges[neighbor] == 0:
                stack.insert(0,neighbor)

        result.append(current_node)

    return result

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        graph = defaultdict(list)

        for line in lines:
            parts = line.split()
            dependency, node = parts[1], parts[0]
            graph[dependency].append(node)

    return graph

def write_output(file_path, order):
    with open(file_path, 'w') as file:
        for node in order:
            file.write(node + '\n')

def main():
    input_file_path = os.path.abspath('govern.in')
    output_file_path = os.path.abspath('govern.out')

    try:
        graph = read_input(input_file_path)
        order = topological_sort(graph)
        write_output(output_file_path, order)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
