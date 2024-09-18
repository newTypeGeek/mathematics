import copy
import itertools

from number_theory.basic import gcd


class MultiplicativeModuloGroup:
    def __init__(self, order: int) -> None:
        assert order > 1, "Order must be greater than 1"
        self._order = order
        self._elements = self._generate_group_elements()
        self._identity = 1

    @property
    def order(self) -> int:
        return self._order

    @property
    def identity(self) -> int:
        return self._identity

    @property
    def elements(self) -> set[int]:
        return self._elements

    def is_subgroup(self, elements: set[int]) -> bool:
        assert len(elements) > 0, f"Input {elements} must not be empty set"
        return (
            self._has_identity(elements)
            and self._is_subset(elements)
            and self._is_closure(elements)
            and self._all_has_inverse(elements)
        )

    def _is_closure(self, elements: set[int]) -> bool:
        for x, y in itertools.combinations_with_replacement(elements, 2):
            if (x * y) % self._order not in elements:
                return False
        return True

    def _is_subset(self, elements: set[int]) -> bool:
        return elements.issubset(self._elements)

    def _has_identity(self, elements: set[int]) -> bool:
        return self._identity in elements

    def _all_has_inverse(self, elements: set[int]) -> bool:
        # identity is its own inverse, no checking is required
        elements_ = copy.deepcopy(elements)
        elements_.remove(self._identity)

        element_has_inverse = {i: False for i in elements_}

        for x, y in itertools.combinations_with_replacement(elements_, 2):
            if self._is_inverse(x, y):
                element_has_inverse[x] = True
                element_has_inverse[y] = True

        return all(element_has_inverse.values())

    def _is_inverse(self, x: int, y: int) -> bool:
        return (x * y) % self._order == self._identity

    def _generate_group_elements(self) -> set[int]:
        elements = set()
        for i in range(1, self._order):
            # only add elements that are coprime with the order
            if gcd(i, self._order) == 1:
                elements.add(i)
        return elements
