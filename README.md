# Python Demo

A Python package providing core mathematical operations.

## Operations Provided

- `add(a, b)`: Returns $a + b$
- `subtract(a, b)`: Returns $a - b$
- `multiply(a, b)`: Returns $a \times b$
- `divide(a, b)`: Returns $a / b$ (raises `ValueError` on division by zero)
- `power(base, exponent)`: Returns $base^{exponent}$
- `modulo(a, b)`: Returns $a \pmod b$

## Quickstart

```python
import math_operation as mo

print(mo.add(10, 5))       # 15
print(mo.subtract(10, 5))  # 5
print(mo.multiply(10, 5))  # 50
print(mo.divide(10, 2))    # 5.0
print(mo.power(2, 3))      # 8
print(mo.modulo(10, 3))    # 1
```
