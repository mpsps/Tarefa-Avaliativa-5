import pytest
from voucher import validar_voucher

@pytest.mark.parametrize("valor", [
    50.00,    
    500.00,    
    50.01,     
    499.99,    
    275.50     
])
def test_valor_valido(valor):
    assert validar_voucher(valor) is True

@pytest.mark.parametrize("valor", [
    49.99,     
    0.00,      
    500.01,    
    1000.00  
])
def test_valor_invalido(valor):
    assert validar_voucher(valor) is False
