# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import es_par

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_es_par(self):
        assert es_par(4) == True
        assert es_par(5) == False
        assert es_par(-7) == False
        assert es_par(-2) == True