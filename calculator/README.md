# Calculator (Mini-App)
A small calculator used by the Ai Agent and runnable on its own. It parses and evaluates simple mathematical operations with respect to precendence operators and prints a pretty result box. 


### Quick Start
- Example command:
```uv run calculator/main.py```

- Output
```
┌─────────────────────┐
│  2 * 3 - 8 / 2 + 5  │
│                     │
│  =                  │
│                     │
│  7                  │
└─────────────────────┘
```


## Project Structure
```
calculator/
├─ __pycache__/
├─ pkg/
│ ├─ __pycache__/
│ ├─ __init__.py/
│ ├─ calculator.py  # Parser / evaluator
│ └─ render.py      # Output box rendering
├─ main.py          # Entry point for CLI
└─ tests.py         # Unit tests
```
