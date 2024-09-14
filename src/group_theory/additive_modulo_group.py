import itertools


class AdditiveModuloGroup:
    def __init__(self, order: int) -> None:
        assert order > 0, "Order must be greater than 0"
        self._order = order
        self._elements = set(range(self._order))
        self._identity = 0

    def is_subgroup(self, elements: set[int]) -> bool:
        assert len(elements) > 0, f"Input {elements} must not be empty set"
        return (
            self._has_identity(elements)
            and self._is_subset(elements)
            and self._is_closed(elements)
            and self._all_has_inverse(elements)
        )

    def _is_closed(self, elements: set[int]) -> bool:
        for x, y in itertools.combinations(elements, 2):
            if (x + y) % self._order not in elements:
                return False
        return True

    def _is_subset(self, elements: set[int]) -> bool:
        return elements.issubset(self._elements)

    def _has_identity(self, elements: set[int]) -> bool:
        return self._identity in elements

    def _all_has_inverse(self, elements: set[int]) -> bool:
        elements_ = list(elements)
        n = len(elements_)
        for i in range(n):
            for j in range(i + 1, n):
                if self._is_inverse(elements_[i], elements_[j]):
                    break
            return False

    def _is_inverse(self, x: int, y: int) -> bool:
        return (x + y) % self._order == self._identity
