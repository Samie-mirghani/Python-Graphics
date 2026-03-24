# Python Graphics — Interactive Triangle Comparator

## Overview

A lightweight, interactive desktop application that lets users draw two triangles on a graphical canvas, automatically computes their areas using **Heron's formula**, and visually highlights the larger triangle. Built with Python's `graphics.py` library, it demonstrates core computational geometry concepts through an intuitive point-and-click interface.

## Key Features

- **Interactive Drawing** — Click to place vertices directly on a coordinate-based canvas; triangles render in real time.
- **Automated Area Calculation** — Computes side lengths via the Euclidean distance formula and derives area using Heron's formula.
- **Visual Comparison** — Automatically identifies the larger triangle and recolors it red for instant visual feedback.
- **Dynamic Labels** — Displays the computed area (to two decimal places) beneath each triangle, positioned relative to the shape's bounding box.
- **Self-Contained GUI** — Runs as a standalone `.pyw` window application with no external dependencies beyond the `graphics` module.

## Tech Stack

| Layer        | Technology                                                                 |
|------------- |--------------------------------------------------------------------------- |
| Language     | Python 3                                                                   |
| GUI Library  | [Zelle Graphics (`graphics.py`)](https://mcsp.wartburg.edu/zelle/python/)  |
| Math         | `math` standard library (square root for distance & Heron's formula)       |

## System Architecture

```
User Click Events
       │
       ▼
┌──────────────┐     ┌───────────────────┐     ┌──────────────────┐
│  GraphWin    │────▶│  distance(p1, p2) │────▶│  area(s1, s2, s3)│
│  (Canvas)    │     │  Euclidean dist.   │     │  Heron's formula │
└──────────────┘     └───────────────────┘     └──────────────────┘
       │                                               │
       ▼                                               ▼
┌──────────────┐                              ┌──────────────────┐
│  Polygon     │◀─────────────────────────────│  Compare areas & │
│  Rendering   │       visual update          │  highlight larger│
└──────────────┘                              └──────────────────┘
```

1. The user clicks three points on the canvas to define each triangle.
2. `distance()` calculates Euclidean distances between each pair of vertices.
3. `area()` applies Heron's formula to derive the triangle's area from its three side lengths.
4. The application compares both areas, fills the larger triangle red, and renders area labels below each shape.

## Setup & Installation

### Prerequisites

- Python 3.6 or later

### Steps

```bash
# Clone the repository
git clone https://github.com/samie-mirghani/python-graphics.git
cd python-graphics

# Run the application
python "Project 4.pyw"
```

> **Note:** The project uses John Zelle's `graphics.py` module, which wraps Python's built-in `tkinter`. Ensure `tkinter` is installed with your Python distribution (it is included by default on most systems).

## Usage

1. Launch the program — a 600 × 600 pink canvas opens.
2. Click **three points** to draw the first triangle (filled cornflower blue).
3. Click **three more points** to draw the second triangle.
4. Click anywhere to **highlight the larger triangle in red** and display both areas.
5. Click once more to exit.

## Suggested Topics / Tags

`python` · `graphics` · `computational-geometry` · `herons-formula` · `tkinter` · `interactive` · `educational`

## License

This project is provided for educational purposes.

---

*Built by Shamsadean Mirghani*
