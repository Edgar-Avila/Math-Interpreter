from dataclasses import dataclass
from typing import Any

@dataclass
class NumberNode:
    value: float

    def __repr__(self) -> str:
        return f'{self.value}'

@dataclass
class AddNode:
    left: Any
    right: Any

    def __repr__(self) -> str:
        return f'({self.left} + {self.right})'

@dataclass
class SubNode:
    left: Any
    right: Any

    def __repr__(self) -> str:
        return f'({self.left} - {self.right})'

@dataclass
class MultNode:
    left: Any
    right: Any

    def __repr__(self) -> str:
        return f'({self.left} * {self.right})'

@dataclass
class DivNode:
    left: Any
    right: Any

    def __repr__(self) -> str:
        return f'({self.left} / {self.right})'

@dataclass
class PlusNode:
    node: Any
    def __repr__(self) -> str:
        return f'(+{self.node})'

@dataclass
class MinusNode:
    node: Any
    def __repr__(self) -> str:
        return f'(-{self.node})'
