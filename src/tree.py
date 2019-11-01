from dataclasses import dataclass
from typing import Any
from src.output import Secret, output


@dataclass
class Node(Secret):
    attribute: Any
    left: Any = None
    right: Any = None

    def pretty_print(self, leader=''):
        next_leader = leader + '|  '
        if self.left:
            print(f"{leader}if {self.attribute} == 0")
            self.left.pretty_print(next_leader)
        if self.right:
            print(f"{leader}if {self.attribute} == 1")
            self.right.pretty_print(next_leader)

    async def __output__(self):
        attribute = await output(self.attribute)
        left = await output(self.left) if self.left else self.left
        right = await output(self.right) if self.right else self.right
        return Node(attribute, left=left, right=right)
