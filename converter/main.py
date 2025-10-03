import re
import sys
from pkg.conversions import _convert_units_temp
from pkg.render import box

_PATTERNS = [
    re.compile(r"^\s*convert\s+(?P<value>-?\d+(?:\.\d+)?)\s+(?P<from>\w+)\s+to\s+(?P<to>\w+)\s*$", re.I),
    re.compile(r"^\s*(?P<value>-?\d+(?:\.\d+)?)\s+(?P<from>\w+)\s+to\s+(?P<to>\w+)\s*$", re.I),
    re.compile(r"^\s*(?P<value>-?\d+(?:\.\d+)?)\s+(?P<from>\w+)\s+in\s+(?P<to>\w+)\s*$", re.I),
]
def parse_input(user_input: str):
    for pattern in _PATTERNS:
        match = pattern.match(user_input)
        if match:
            value = float(match.group("value"))
            from_units = match.group("from")
            to_units = match.group("to")
            return value, from_units, to_units
    raise ValueError("Invalid input format. Please use formats like 'convert 10 meters to feet' or '50 fahrenheit to celcius'.")

def main() -> int:
    if len(sys.argv) <= 1:
        print("Unit Converter App")
        print('Usage: python main.py "<conversion request>"')
        print('Example: python main.py "convert 10 meters to feet"')
        return 0

    user_input = " ".join(sys.argv[1:])
    try:
        value, from_units, to_units = parse_input(user_input)
        result = _convert_units_temp(value, from_units, to_units)
        output = f"{value} {from_units} is {result:.2f} {to_units}"
        print(box(output))
    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
