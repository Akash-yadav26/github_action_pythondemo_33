"""Math operations module providing basic arithmetic and mathematical functions."""

def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of a and b.
    
    Raises:
        ValueError: If b is 0.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(base: float, exponent: float) -> float:
    """Return base raised to the power of exponent."""
    return base ** exponent


def modulo(a: int, b: int) -> int:
    """Return the remainder of a divided by b.
    
    Raises:
        ValueError: If b is 0.
    """
    if b == 0:
        raise ValueError("Cannot perform modulo by zero.")
    return a % b
