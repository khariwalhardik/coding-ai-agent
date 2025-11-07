"""Calculation service: safely evaluate arithmetic expressions and keep a small history."""
from typing import List
import ast
import operator as op

from .model import Calculation


# supported operators map
_OPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
    ast.USub: op.neg,
}


class CalculatorService:
    def __init__(self, max_history: int = 50):
        self._history: List[Calculation] = []
        self.max_history = max_history

    def _eval_node(self, node):
        if isinstance(node, ast.Num):  # python <3.8
            return node.n
        if isinstance(node, ast.Constant):  # python 3.8+
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Unsupported constant")
        if isinstance(node, ast.BinOp):
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)
            op_func = _OPS.get(type(node.op))
            if op_func is None:
                raise ValueError(f"Unsupported operator: {type(node.op).__name__}")
            return op_func(left, right)
        if isinstance(node, ast.UnaryOp):
            operand = self._eval_node(node.operand)
            op_func = _OPS.get(type(node.op))
            if op_func is None:
                raise ValueError(f"Unsupported unary operator: {type(node.op).__name__}")
            return op_func(operand)
        raise ValueError(f"Unsupported expression: {type(node).__name__}")

    def evaluate(self, expression: str):
        """Safely evaluate a numeric expression and store it in history.

        Supports +, -, *, /, %, and ** with parentheses and numeric literals.
        """
        if not expression or not expression.strip():
            raise ValueError("Empty expression")

        try:
            tree = ast.parse(expression, mode="eval")
            result = self._eval_node(tree.body)
        except Exception as exc:
            raise ValueError(f"Invalid expression: {exc}") from exc

        # store history (keep it small)
        self._history.insert(0, Calculation(expression=expression, result=result))
        if len(self._history) > self.max_history:
            self._history.pop()
        return result

    def get_history(self):
        return list(self._history)
