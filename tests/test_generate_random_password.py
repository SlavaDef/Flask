import pytest

from service.parol_generator import generate_random_password


def test_length():
    assert len(generate_random_password(10)) == 10

def test_type():
    assert isinstance(generate_random_password(10), str)


def test_value_error():
    with pytest.raises(ValueError) as error:
        generate_random_password('f')
    assert str(error.value) == "error, enter only numbers"
