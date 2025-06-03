from service.parol_generator import generate_random_password


def test_length():
    assert len(generate_random_password(10)) == 10

def test_type():
    assert isinstance(generate_random_password(10), str)

def test_if_parameter_is_string():
    assert (generate_random_password('f'), 'error, enter only numbers')

def test_if_parameter_is_double():
    assert (generate_random_password(0.5), 'error, enter only numbers')

def test_small_length_error():
    assert (generate_random_password(5), 'error, password length must be at least 8 characters')


def test_big_length_error():
    assert (generate_random_password(130), 'error, password length must be less than 128 characters')


def test_default_length():
    assert len(generate_random_password()) == 12