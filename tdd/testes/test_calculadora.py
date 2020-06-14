import unittest
from calculadora import somar


class TestCalculadora(unittest.TestCase):

    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(somar(5, 5), 10)

    def teste_soma_5_pos_mais_5_negativo_deve_retornar_0(self):
        self.assertEqual(somar(5, -5), 0)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (5, 10, 15),
            (2, 10, 12),
            (3, 7, 10),
            (15, 15, 30),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(somar(x, y), saida)

    def test_soma_x_nao_eh_float_deve_retornar_assertion_error(self):
        with self.assertRaises(AssertionError):
            somar('11', 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
