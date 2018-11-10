def test_palin():
    texto = "ana"
    rvs_texto = reversed(texto)
    resultado = (list(texto)) == (list(rvs_texto))

    assert True == resultado, "si es un palindromo"
    assert False != resultado, "no es un palindromo"
