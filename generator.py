import json
import sys
from graphviz import Digraph

def validate_graph(data):
    nodes = data.get('nodes', {})
    edges = data.get('edges', [])
    
    if not nodes:
        raise ValueError("Input JSON must contain 'nodes' dictionary.")
    if not edges:
        raise ValueError("Input JSON must contain 'edges' list.")
    
    for edge in edges:
        if 'from' not in edge or 'to' not in edge:
            raise ValueError(f"Each edge must have 'from' and 'to' keys. Problematic edge: {edge}")
        if edge['from'] not in nodes or edge['to'] not in nodes:
            raise ValueError(f"Edge references undefined nodes: {edge}")
    
    # Optional: check for cycles or unreachable nodes here
    
def generate_flowchart(data, output_file='flowchart.png'):
    validate_graph(data)
    dot = Digraph(format='png')
    dot.attr(rankdir='TB', size='8,5')

    # Add nodes
    for node_id, attrs in data['nodes'].items():
        label = attrs.get('label', node_id)
        shape = attrs.get('shape', 'box')
        dot.node(node_id, label, shape=shape)

    # Add edges
    for edge in data['edges']:
        label = edge.get('label', '')
        dot.edge(edge['from'], edge['to'], label=label, fontsize='10' if label else None)

    dot.render(output_file, cleanup=True)
    print(f'Flowchart saved as {output_file}')


def main():
    if len(sys.argv) != 3:
        print("Usage: python flowchart_tool.py input.json output.png")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file) as f:
            data = json.load(f)
        generate_flowchart(data, output_file)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
