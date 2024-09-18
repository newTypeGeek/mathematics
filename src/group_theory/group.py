import itertools

from typing import TypeVar, Generic

import loguru

T = TypeVar("T")


class Group(Generic[T]):
    def __init__(self, elements: set[T], operation: callable[T, T], **kwargs):
        self._elements = elements
        self._operation = operation
        self._identity = self._find_identity()
        self._check_group_definition()

    def _check_group_definition(self):
        assert self._is_associative(), "Operation is not associative"
        assert self._is_same_identity_for_all_elements(), "Identity is not the same for all elements"
        assert self._all_has_inverse(), "Not all elements have inverse"

    def _is_associative(self) -> bool:
        for a, b, c in itertools.product(self._elements, repeat=3):
            expr1 = self._operation(self._operation(a, b), c)
            expr2 = self._operation(a, self._operation(b, c))
            if expr1 != expr2:
                loguru.logger.error(
                    "Operation is not associative: {a}({b}{c})={expr1} != ({a}{b}){c}={expr2}",
                    a=a,
                    b=b,
                    c=c,
                    expr1=expr1,
                    expr2=expr2,
                )
                return False
        return True

    def _is_same_identity_for_all_elements(self) -> bool:
        if self._identity is None:
            return False
        for a in self._elements:
            right = self._operation(a, self._identity)
            left = self._operation(self._identity, a)
            if right != a or left != a:
                loguru.logger.error(
                    "Identity {e} is not the same for all elements: {a}e={right} != e{a}={left}",
                    e=self._identity,
                    a=a,
                    right=right,
                    left=left,
                )
                return False
        return True

    def _find_identity(self) -> T | None:
        for a, b in itertools.product(self._elements, repeat=2):
            if self._operation(a, b) == b and self._operation(b, a) == b:
                loguru.logger.debug("Found identity element e={e}", e=b)
                return b
        loguru.logger.error("No identity element found")
        return None

    def _all_has_inverse(self) -> bool:
        element_has_inverse = {a: False for a in self._elements}
        for a, b in itertools.product(self._elements, repeat=2):
            if self._is_inverse(a, b):
                element_has_inverse[a] = True
                element_has_inverse[b] = True

        all_has_inverse = all(element_has_inverse.values())
        if not all_has_inverse:
            loguru.logger.error(
                "Some elements do not have inverse: {elements}",
                elements=[a for a, has_inverse in element_has_inverse.items() if not has_inverse],
            )

        return all_has_inverse

    def _is_inverse(self, a: T, b: T) -> bool:
        return self._operation(a, b) == self._identity and self._operation(b, a) == self._identity
