from dataclasses import dataclass
from typing import Any
from mpyc.runtime import mpc
from src.output import Secret, output
from functools import reduce
import operator


@dataclass
class ObliviousArray(Secret):
    values: [Any]
    included: [Any]

    def __init__(self, *values, included=None):
        self.values = values
        self.included = included

    def select(self, *include):
        if self.included == None:
            included = include
        else:
            included = mpc.schur_prod(list(self.included), include)
        return ObliviousArray(*self.values, included=included)

    def map(self, function):
        values = map(function, self.values)
        return ObliviousArray(*values, included=self.included)

    def reduce(self, neutral_element, operation):
        values = self.values
        included = self.included
        if included:
            values = [mpc.if_else(included[i], values[i], neutral_element)
                      for i in range(len(self.values))]
        return reduce(operation, values, neutral_element)

    def sum(self):
        return self.reduce(0, operator.add)

    def __getitem__(self, index):
        is_selected = [i == index for i in range(len(self.values))]
        return mpc.matrix_prod([is_selected], [self.values], True)[0][0]

    async def output(self):
        values = [await output(value) for value in self.values]
        if self.included:
            included = await output(self.included)
        else:
            included = [True] * len(self.values)
        return [values[i] for i in range(len(values)) if included[i]]
