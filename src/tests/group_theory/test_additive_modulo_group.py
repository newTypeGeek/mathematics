import pytest

from group_theory.additive_modulo_group import AdditiveModuloGroup


@pytest.fixture
def identity_sub_group_candidate() -> set[int]:
    return {0}


@pytest.fixture
def group_order_seven() -> AdditiveModuloGroup:
    return AdditiveModuloGroup(7)


@pytest.fixture
def seven_order_group_elements() -> set[int]:
    return {0, 1, 2, 3, 4, 5, 6}


@pytest.fixture
def seven_order_sub_group_candidates() -> list[set[int]]:
    return [
        {0},
        {1},
        {2},
        {3},
        {4},
        {5},
        {6},
        {0, 1},
        {0, 2},
        {0, 3},
        {0, 4},
        {0, 5},
        {0, 6},
        {1, 2},
        {1, 3},
        {1, 4},
        {1, 5},
        {1, 6},
        {2, 3},
        {2, 4},
        {2, 5},
        {2, 6},
        {3, 4},
        {3, 5},
        {3, 6},
        {4, 5},
        {4, 6},
        {5, 6},
        {0, 1, 2},
        {0, 1, 3},
        {0, 1, 4},
        {0, 1, 5},
        {0, 1, 6},
        {0, 2, 3},
        {0, 2, 4},
        {0, 2, 5},
        {0, 2, 6},
        {0, 3, 4},
        {0, 3, 5},
        {0, 3, 6},
        {0, 4, 5},
        {0, 4, 6},
        {0, 5, 6},
        {1, 2, 3},
        {1, 2, 4},
        {1, 2, 5},
        {1, 2, 6},
        {1, 3, 4},
        {1, 3, 5},
        {1, 3, 6},
        {1, 4, 5},
        {1, 4, 6},
        {1, 5, 6},
        {2, 3, 4},
        {2, 3, 5},
        {2, 3, 6},
        {2, 4, 5},
        {2, 4, 6},
        {2, 5, 6},
        {3, 4, 5},
        {3, 4, 6},
        {3, 5, 6},
        {4, 5, 6},
        {0, 1, 2, 3},
        {0, 1, 2, 4},
        {0, 1, 2, 5},
        {0, 1, 2, 6},
        {0, 1, 3, 4},
        {0, 1, 3, 5},
        {0, 1, 3, 6},
        {0, 1, 4, 5},
        {0, 1, 4, 6},
        {0, 1, 5, 6},
        {0, 2, 3, 4},
        {0, 2, 3, 5},
        {0, 2, 3, 6},
        {0, 2, 4, 5},
        {0, 2, 4, 6},
        {0, 2, 5, 6},
        {0, 3, 4, 5},
        {0, 3, 4, 6},
        {0, 3, 5, 6},
        {0, 4, 5, 6},
        {1, 2, 3, 4},
        {1, 2, 3, 5},
        {1, 2, 3, 6},
        {1, 2, 4, 5},
        {1, 2, 4, 6},
        {1, 2, 5, 6},
        {1, 3, 4, 5},
        {1, 3, 4, 6},
        {1, 3, 5, 6},
        {1, 4, 5, 6},
        {2, 3, 4, 5},
        {2, 3, 4, 6},
        {2, 3, 5, 6},
        {2, 4, 5, 6},
        {3, 4, 5, 6},
        {0, 1, 2, 3, 4},
        {0, 1, 2, 3, 5},
        {0, 1, 2, 3, 6},
        {0, 1, 2, 4, 5},
        {0, 1, 2, 4, 6},
        {0, 1, 2, 5, 6},
        {0, 1, 3, 4, 5},
        {0, 1, 3, 4, 6},
        {0, 1, 3, 5, 6},
        {0, 1, 4, 5, 6},
        {0, 2, 3, 4, 5},
        {0, 2, 3, 4, 6},
        {0, 2, 3, 5, 6},
        {0, 2, 4, 5, 6},
        {0, 3, 4, 5, 6},
        {1, 2, 3, 4, 5},
        {1, 2, 3, 4, 6},
        {1, 2, 3, 5, 6},
        {1, 2, 4, 5, 6},
        {1, 3, 4, 5, 6},
        {2, 3, 4, 5, 6},
        {0, 1, 2, 3, 4, 5},
        {0, 1, 2, 3, 4, 6},
        {0, 1, 2, 3, 5, 6},
        {0, 1, 2, 4, 5, 6},
        {0, 1, 3, 4, 5, 6},
        {0, 2, 3, 4, 5, 6},
        {1, 2, 3, 4, 5, 6},
        {0, 1, 2, 3, 4, 5, 6},
    ]


def test_itself_is_subgroup(group_order_seven, seven_order_group_elements):
    assert group_order_seven.is_subgroup(seven_order_group_elements)


def test_identity_is_subgroup(group_order_seven, identity_sub_group_candidate):
    assert group_order_seven.is_subgroup(identity_sub_group_candidate)


def test_only_two_candidates_are_subgroups(group_order_seven, seven_order_sub_group_candidates):
    subgroup_count = 0
    for candidate in seven_order_sub_group_candidates:
        subgroup_count += group_order_seven.is_subgroup(candidate)

    # this is due to Lagrange's Theorem
    assert subgroup_count == 2
    
def test_negative_order_raises_error():
    with pytest.raises(AssertionError):
        AdditiveModuloGroup(-1)

def test_zero_order_raises_error():
    with pytest.raises(AssertionError):
        AdditiveModuloGroup(0)