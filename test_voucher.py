import pytest
from app.voucher import validar_voucher

@pytest.mark.parametrize("valor", [
    50.00,     # limite inferior
    500.00,    # limite superior
    50.01,     # logo acima do limite inferior
    499.99,    # logo abaixo do limite superior
    275.50     # valor médio
])
def test_valor_valido(valor):
    assert validar_voucher(valor) is True

@pytest.mark.parametrize("valor", [
    49.99,     # logo abaixo do limite inferior
    0.00,      # extremo inferior
    500.01,    # logo acima do limite superior
    1000.00    # extremo superior
])
def test_valor_invalido(valor):
    assert validar_voucher(valor) is False
