import pytest
from calculadora import sumar, dividir, restar, multiplicar

@pytest.mark.suma
def test_sumar_positivo():
    assert sumar(2, 3) == 5

@pytest.mark.suma
def test_sumar_negativo():
    assert sumar(-10,-10) == -20

##def test_dividir_por_cero():
##    with pytest.raises(ValueError):
##        dividir(1, 0)

@pytest.mark.parametrize("a,b,resultado",[
    (3,3,6),
    (5,15,20),
    (6,6,12)
],
ids=["caso1", "caso2","caso3"])

def test_sumar_casos_parametrize(a,b,resultado):
    assert sumar(a,b) == resultado