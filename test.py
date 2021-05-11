import unittest
from tp_crypto import *
class TestExo1(unittest.TestCase):

    def test_pgcd_rec(self):
        self.assertEqual(pgcd_rec(3, 2), 1)
        self.assertEqual(pgcd_rec(9, 3), 3)
        self.assertEqual(pgcd_rec(563, 9562), 1)

    def test_pgcd_iter(self):
        self.assertEqual(pgcd_iter(3, 2), 1)
        self.assertEqual(pgcd_iter(9548, 564), 4)
        self.assertEqual(pgcd_iter(1689, 564), 3)

    def test_euclide_ext(self):
        a, b = euclide_ext(3, 2)
        self.assertEqual(3*a+2*b, 1)
        a, b = euclide_ext(16583, 56)
        self.assertEqual(a*16583+b*56, 7)
        a, b = euclide_ext(563, 9562)
        self.assertEqual(a*563+b*9562, 1)

    def test_inverse_mod(self):
        a, N = 2, 5
        self.assertEqual((inverse_modulaire(a, N)*a)%N, 1)
        a, N = 2, 17
        self.assertEqual((inverse_modulaire(a, N)*a)%N, 1)
        a, N = 13, 29
        self.assertEqual((inverse_modulaire(a, N)*a)%N, 1)

    def test_expo_mod(self):
        e, b, N = 20, 6, 10
        c = expo_modulaire(e, b, N)
        self.assertEqual(c%N, (b**e)%N)

        e, b, N = 12, 23, 14
        c = expo_modulaire(e, b, N)
        self.assertEqual(c%N, (b**e)%N)

        e, b, N = 2, 43, 76
        c = expo_modulaire(e, b, N)
        self.assertEqual(c%N, (b**e)%N)
    
    def test_expo_mod_rapide(self):
        e, b, N = 2, 3, 4
        c = expo_modulaire_rapide(e, b, N)
        self.assertEqual(c%N, (b**e)%N)

        e, b, N = 12, 23, 14
        c = expo_modulaire_rapide(e, b, N)
        self.assertEqual(c%N, (b**e)%N)

        e, b, N = 2, 43, 76
        c = expo_modulaire_rapide(e, b, N)
        self.assertEqual(c%N, (b**e)%N)

    def test_Fermat(self):
        self.assertTrue(test_fermat(2, 170))
        self.assertTrue(test_fermat(7, 17))
        self.assertTrue(test_fermat(17, 17))
        self.assertTrue(test_fermat(5, 4))
        self.assertFalse(test_fermat(22, 4))
        self.assertFalse(test_fermat(70, 4))
        self.assertFalse(test_fermat(535, 4))
        self.assertFalse(test_fermat(16002, 4))

    def test_Rabin(self):
        self.assertTrue(test_rabin(2, 10))
        self.assertTrue(test_rabin(7, 10))
        self.assertTrue(test_rabin(17, 10))
        self.assertTrue(test_rabin(5, 10))
        self.assertFalse(test_rabin(22, 10))
        self.assertFalse(test_rabin(70, 10))
        self.assertFalse(test_rabin(535, 10))
        self.assertFalse(test_rabin(16002, 10))
    
    def test_encryption_decryption(self):
        n, e, d = gen_rsa(21)
        m = 1201
        self.assertEqual(dec_rsa(enc_rsa(m, e, n), d, n), m)
        m = 800
        self.assertEqual(dec_rsa(enc_rsa(m, e, n), d, n), m)
        m = 535
        self.assertEqual(dec_rsa(enc_rsa(m, e, n), d, n), m)

    #Question 12
    def test_example_12(self):
        msg_c, d, n = enc_example()
        s = "ceci est le message de la question 12"
        s_ret = verify_example(msg_c, d, n)
        #print(s_ret)
        self.assertEqual(s_ret, s)
        

if __name__ == '__main__':
    unittest.main()
