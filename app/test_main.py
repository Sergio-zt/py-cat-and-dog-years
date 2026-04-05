from app.main import get_human_age


def test_check_if_14_cat_dog_yers_return_0() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_check_if_15_cat_dog_yers_return_1() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_check_if_23_cat_dog_yers_return_1() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_check_if_24_cat_dog_yers_return_2() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_check_if_27_28_cat_dog_yers_return_2() -> None:
    assert get_human_age(27, 28) == [2, 2]


def test_check_if_28_29_cat_dog_yers_return_2() -> None:
    assert get_human_age(28, 29) == [3, 3]
