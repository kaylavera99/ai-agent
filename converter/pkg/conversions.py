# conversions.py

class ConversionResults:
    value: float
    from_units: str
    to_units: str

# temperature conversions
def _convert_temperature(value: float, from_units: str, to_units: str) -> float:
    f = from_units.lower()
    t = to_units.lower()
    if f == t:
        return value
    if f == "celsius" and t == "fahrenheit":
        return (value * 9/5) + 32
    if f == "fahrenheit" and t == "celsius":
        return (value - 32) * 5/9
    if f == "celsius" and t == "kelvin":
        return value + 273.15
    if f == "kelvin" and t == "celsius":
        return value - 273.15
    if f == "fahrenheit" and t == "kelvin":
        return (value - 32) * 5/9 + 273.15
    if f == "kelvin" and t == "fahrenheit":
        return (value - 273.15) * 9/5 + 32
    raise ValueError(f"Unsupported temperature conversion from {from_units} to {to_units}")
   
# weight and length conversions

_length_units = {
    "m": 1.0, "meter": 1.0, "meters": 1.0,
    "km": 1000.0, "kilometer": 1000.0, "kilometers": 1000.0,
    "cm": 0.01, "centimeter": 0.01, "centimeters": 0.01,
    "mm": 0.001, "millimeter": 0.001, "millimeters": 0.001,
    "mi": 1609.34, "mile": 1609.34, "miles": 1609.34,
    "yd": 0.9144, "yard": 0.9144, "yards": 0.9144,
    "ft": 0.3048, "foot": 0.3048, "feet": 0.3048,
    "in": 0.0254, "inch": 0.0254, "inches": 0.0254,
}

_weight_units = {
    "g": 1.0, "gram": 1.0, "grams": 1.0,
    "kg": 1000.0, "kilogram": 1000.0, "kilograms": 1000.0,
    "mg": 0.001, "milligram": 0.001, "milligrams": 0.001,
    "lb": 453.592, "pound": 453.592, "pounds": 453.592,
    "oz": 28.3495, "ounce": 28.3495, "ounces": 28.3495,
}
def _convert_units_tables(value: float, from_units: str, to_units: str, units_dict: dict) -> float:
    f = from_units.lower()
    t = to_units.lower()
    if f not in units_dict or t not in units_dict:
        raise ValueError(f"Unsupported conversion from {from_units} to {to_units}")
    value_in_base = value * units_dict[f]
    return value_in_base / units_dict[t]

def _convert_units_temp(value: float, from_units: str, to_units: str) -> ConversionResults:
    length_units = {"m", "meter", "meters", "km", "kilometer", "kilometers", "cm", "centimeter", "centimeters", "mm", "millimeter", "millimeters", "mi", "mile", "miles", "yd", "yard", "yards", "ft", "foot", "feet", "in", "inch", "inches"}
    weight_units = {"g", "gram", "grams", "kg", "kilogram", "kilograms", "mg", "milligram", "milligrams", "lb", "pound", "pounds", "oz", "ounce", "ounces"}
    f = from_units.lower()
    t = to_units.lower()
    if f in length_units and t in length_units:
        return _convert_units_tables(value, from_units, to_units, _length_units)
    elif f in weight_units and t in weight_units:
        return _convert_units_tables(value, from_units, to_units, _weight_units)
    elif (f in {"celsius", "fahrenheit", "kelvin"} and t in {"celsius", "fahrenheit", "kelvin"}):
        return _convert_temperature(value, from_units, to_units)
    else:
        raise ValueError(f"Unsupported conversion from {from_units} to {to_units}")
