import pytest

from group_theory.multiplicative_modulo_group import MultiplicativeModuloGroup


@pytest.fixture
def identity_sub_group_candidate() -> set[int]:
    return {1}


@pytest.fixture
def group_order_ten() -> MultiplicativeModuloGroup:
    return MultiplicativeModuloGroup(10)


@pytest.fixture
def ten_order_group_elements() -> set[int]:
    return {1, 3, 7, 9}


def test_correct_elements(group_order_ten, ten_order_group_elements) -> None:
    assert group_order_ten.elements == ten_order_group_elements


def test_itself_is_subgroup(group_order_ten) -> None:
    assert group_order_ten.is_subgroup(group_order_ten.elements)
