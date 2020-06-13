import unittest
from bacomovos import bacon_com_ovos


class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_levantar_assertion_de_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('33')

    def test_deve_retornar_bacon_com_ovos_se_a_entrada_for_multiplo_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com ovos'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida,
                                 msg=f'{entrada} não retornou "{saida}"')

    def test_deve_retornar_passarfome_se_a_entrada_nao_for_multiplo_3_e_5(self):
        entradas = (2, 4, 8, 14)
        saida = 'Passar fome'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida,
                                 msg=f'{entrada} não retornou "{saida}"')

    def test_deve_retornar_bacon_se_a_entrada_for_multiplo_3(self):
        entradas = (3, 6, 9, 12)
        saida = 'Bacon'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida,
                                 msg=f'{entrada} não retornou "{saida}"')

    def test_deve_retornar_bacon_se_a_entrada_for_multiplo_5(self):
        entradas = (5, 25, 35)
        saida = 'Ovos'
        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida,
                                 msg=f'{entrada} não retornou "{saida}"')


unittest.main(verbosity=2)
