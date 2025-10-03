# Calculator (Mini-App)
A small calculator used by the Ai Agent and runnable on its own. It parses and evaluates simple mathematical operations with respect to precendence operators and prints a pretty result box. 


### Quick Start
- Example command:
  
```uv run calculator/main.py "2 * 3 - 8 / 2 + 5"```

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

## Running tests
```
uv run python -m unittest calculator/tests.py -v
uv run python -m unittest calculator.tests

```
## Testing output
Verbose output:
```
test_addition (calculator.tests.TestCalculator.test_addition) ... ok
test_complex_expression (calculator.tests.TestCalculator.test_complex_expression) ... ok
test_division (calculator.tests.TestCalculator.test_division) ... ok
test_empty_expression (calculator.tests.TestCalculator.test_empty_expression) ... ok
test_invalid_operator (calculator.tests.TestCalculator.test_invalid_operator) ... ok
test_multiplication (calculator.tests.TestCalculator.test_multiplication) ... ok
test_nested_expression (calculator.tests.TestCalculator.test_nested_expression) ... ok
test_not_enough_operands (calculator.tests.TestCalculator.test_not_enough_operands) ... ok
test_precedence (calculator.tests.TestCalculator.test_precedence) ... ok
test_subtraction (calculator.tests.TestCalculator.test_subtraction) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK
```

Standard output:
```
Ran 10 tests in 0.000s

OK
```