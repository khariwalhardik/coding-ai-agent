from dataclasses import dataclass
from typing import Any


@dataclass
class Calculation:
    """Simple data class to hold a calculation record."""
    expression: str
    result: Any
