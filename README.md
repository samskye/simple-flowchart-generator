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
