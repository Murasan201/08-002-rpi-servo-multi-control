# Raspberry Pi Multi-Servo Control

Sample application for Python programming textbook

## Overview

This project is a Python application for controlling multiple servo motors using Raspberry Pi.
It is designed as educational material for Python beginners.

## Features

- Simultaneous control of multiple servo motors
- Position control by angle specification
- Sequential motion support

## Requirements

- Raspberry Pi (Recommended: Raspberry Pi 3 or later)
- Python 3.7 or higher
- Servo motors
- Jumper wires

## Directory Structure

```
.
├── src/           # Source code
├── examples/      # Sample scripts
├── docs/          # Documentation
└── tests/         # Test code
```

## Installation

### 1. Create a virtual environment

To avoid conflicts with system packages, we recommend using a Python virtual environment:

```bash
# Create a virtual environment
python3 -m venv venv
```

### 2. Activate the virtual environment

```bash
# Activate the virtual environment
source venv/bin/activate
```

After activation, you should see `(venv)` at the beginning of your command prompt.

### 3. Install dependencies

```bash
# Install dependencies
pip install -r requirements.txt
```

### Notes

- To deactivate the virtual environment, run: `deactivate`
- You need to activate the virtual environment each time you start a new terminal session before running the scripts

## Usage

Before running any scripts, make sure to activate the virtual environment:

```bash
source venv/bin/activate
```

Please refer to the documentation in the `docs/` directory for details.

## Troubleshooting

If you encounter any issues during installation or execution, please refer to [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) for common problems and their solutions.

## License

See the LICENSE file.

## Author

Kodansha Python Textbook Project
