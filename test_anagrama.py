def test_anagrama():
    palabra1 = sorted("dog")
    palabra2 = sorted("god")
    resultado = palabra1 == palabra2

    assert True == resultado, "si es un anagrama"
