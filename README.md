[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/s20ss-mcp-rdkit-badge.png)](https://mseep.ai/app/s20ss-mcp-rdkit)

# MCP RDKit Project

## Overview

The `mcp_rdkit` project integrates the RDKit library with the MCP (Model Context Protocol) framework to provide advanced chemical informatics tools. It includes functionalities for molecular visualization, descriptor calculation, and interaction with an MCP server.

## Features

- **Molecular Visualization**: Generate images of molecules using RDKit.
- **Descriptor Calculation**: Compute molecular descriptors such as molecular weight, logP, and more.
- **MCP Server Integration**: Communicate with an MCP server for advanced chemical informatics tasks.

## Project Structure

- `mcp_rdkit/`
  - `__main__.py`: Entry point for the application. It initializes the MCP server and runs it in "stdio" mode.
  - `rdkit_helper.py`: Contains helper functions for RDKit operations, including:
    - Converting PIL images to base64.
    - Interfacing with the MCP server.
    - Utilizing RDKit for chemical computations.



- `setup.py`: Configuration for packaging and distribution.

## Requirements

- Python 3.8 or higher
- RDKit library
- MCP framework

## Installation

1. Install the package using pip:
   ```bash
   pip install mcp-rdkit
   ```

2. Run the application:
   ```bash
   python -m mcp_rdkit
   ```

## Demo

You can integrate this directly into Claude App:

![Demo 1](https://github.com/s20ss/mcp_rdkit/blob/main/uploads/image.png?raw=true)
![Demo 2](https://github.com/s20ss/mcp_rdkit/blob/main/uploads/image%20(1).png?raw=true)
![Demo 3](https://github.com/s20ss/mcp_rdkit/blob/main/uploads/image%20(2).png?raw=true)

## Usage

- **Run the MCP server**:
  The application starts an MCP server that can process chemical informatics tasks.

- **Generate molecular images**:
  Use the RDKit helper functions to visualize molecules.

- **Calculate descriptors**:
  Leverage RDKit's descriptor calculation tools for chemical analysis.

## MCP Configuration Example

To use the RDKit server with MCP, add the following configuration to your `mcp` config file:

```json
"rdkit-server": {
  "type": "stdio",
  "command": "python",
  "args": [
    "-m",
    "mcp_rdkit"
  ]
}
```



RDKIT MCP is certified and indexed by [MCP Review](https://mcpreview.com/mcp-servers/s20ss/mcp_rdkit)
[![Verified on MseeP](https://mseep.ai/badge.svg)](https://mseep.ai/app/e504ca84-1db0-4bb5-be6d-1a20e0d96293)
