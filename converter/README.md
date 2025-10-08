# Conversion Tool (Mini-App)
A small, light-weight conversion tool that converts temperatures, mass and distance with a simple CLI. 


### Quick Start
- Converting length:
```
python converter/main.py "Convert 10 m to feet"
uv run converter/main.py "Convert 8 feet to yards"
```
- Converting temperature:
```
python converter/main.py "10 Fahrenheit to Celsius"
uv run converter/main.py "300 K to F"
```

- Converting mass:
```
python converter/main.py "133 kg to ounces"
uv run converter/main.py "0.421 lbs to oz"
```
- Phrasing variations:
```
python converter/main.py "convert 133 mm to feet"
uv run converter/main.py "32 F to C"

```

- Output
```
┌──────────────────────┐
│ 10.0 m is 32.81 feet │
└──────────────────────┘
```

### Supported units
Input is normalized despite case and accepts common abbreviations
- Length: m, km, cm, mm, mi, yd, in (including plurals and non-abbreviations)
- Mass: g, kg, mg, lb, oz (including plurals and non-abbreviations)
- Temperature: Celsius, Fahrenheit, Kelvin (C / F / K)

## Project Structure
```
converter/
├─ __pycache__/
├─ pkg/
│ ├─ __pycache__/
│ ├─ __init__.py/
│ ├─ conversions.py  # Conversion logic
│ └─ render.py       # Output box rendering
├─ main.py           # Entry point for CLI
└─ tests.py          # Unit tests
```

## Running tests
### Using Python directly (Recommended)
```
python -m unittest converter/tests.py -v
python -m unittest converter.tests

```
### Using uv
```
uv run python -m unittest converter/tests.py -v
uv run python -m unittest converter.tests

```
## Testing output
Verbose output:
```
test_celsius_to_fahrenheit (converter.tests.TestConversionResults.test_celsius_to_fahrenheit) ... ok
test_cm_to_inch (converter.tests.TestConversionResults.test_cm_to_inch) ... ok
test_fahrenheit_to_celsius (converter.tests.TestConversionResults.test_fahrenheit_to_celsius) ... ok
test_fahrenheit_to_kelvin (converter.tests.TestConversionResults.test_fahrenheit_to_kelvin) ... ok
test_feet_to_mm (converter.tests.TestConversionResults.test_feet_to_mm) ... ok
test_gram_to_oz (converter.tests.TestConversionResults.test_gram_to_oz) ... ok
test_kelvin_to_cesius (converter.tests.TestConversionResults.test_kelvin_to_cesius) ... ok
test_kg_to_oz (converter.tests.TestConversionResults.test_kg_to_oz) ... ok
test_km_to_mile (converter.tests.TestConversionResults.test_km_to_mile) ... ok
test_lb_to_kg (converter.tests.TestConversionResults.test_lb_to_kg) ... ok
test_meter_to_km (converter.tests.TestConversionResults.test_meter_to_km) ... ok
test_mile_to_yard (converter.tests.TestConversionResults.test_mile_to_yard) ... ok
test_oz_to_mg (converter.tests.TestConversionResults.test_oz_to_mg) ... ok

----------------------------------------------------------------------
Ran 13 tests in 0.000s

OK
```

Standard output:
```
Ran 13 tests in 0.000s

OK
```