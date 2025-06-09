# Simple Flowchart Generator Script

A Python CLI tool to generate flowcharts from structured JSON input, supporting linear and branching workflows. Outputs PNG images using Graphviz.

## Features

- Define nodes and edges in JSON format  
- Supports common flowchart shapes: oval (start/end), rectangle (process), diamond (decision), parallelogram (input/output)  
- Edge labels for conditional branches  
- Input validation and error handling  
- Command-line interface for easy usage

## Requirements

- Python 3.6+  
- [Graphviz](https://graphviz.org/download/) system package installed and in your PATH  
- Python `graphviz` package:  
  ```bash
  pip3 install graphviz

## Usage

### 1. Create a JSON file describing your flowchart, e.g. flow.json:

  <pre>{
  "nodes": {
    "start": {"label": "Start", "shape": "oval"},
    "load": {"label": "Select Dataset & Load Data", "shape": "parallelogram"},
    "train": {"label": "Train and Save Model", "shape": "rectangle"},
    "test": {"label": "Load Model & Test Data (by prefix)", "shape": "rectangle"},
    "predict": {"label": "Predict & Explain (LIME + SHAP)", "shape": "rectangle"},
    "display": {"label": "Display Results & Save Plots", "shape": "parallelogram"},
    "end": {"label": "End", "shape": "oval"}
  },
  "edges": [
    {"from": "start", "to": "load"},
    {"from": "load", "to": "train"},
    {"from": "train", "to": "test"},
    {"from": "test", "to": "predict"},
    {"from": "predict", "to": "display"},
    {"from": "display", "to": "end"}
  ]
}
</pre>

### 2. Run the tool:
```bash
python flowchart_tool.py flow.json output.png
```

### 3. Find the generated flowchart in output.png

## Error Handling
The tool validates the JSON structure and node references. Errors will be reported if the input is invalid.

## Extending
You can customize node shapes and add edge labels for branching logic in the JSON input.

## License
MIT License
