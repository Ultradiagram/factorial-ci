import pytest
from factorial import factorial


def test_factorial_caso_correcto():
    assert factorial(5) == 120


def test_factorial_caso_limite():
    assert factorial(0) == 1


def test_factorial_error_numero_negativo():
    with pytest.raises(ValueError):
        factorial(-3)


def test_factorial_error_tipo_incorrecto():
    with pytest.raises(TypeError):
        factorial("5")