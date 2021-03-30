import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kassapaate_on_oikeanlainen(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        self.assertEqual((self.kassapaate.edulliset+self.kassapaate.maukkaat), 0)


    def test_kateisosto_toimii(self):
        
        #kun raha riittää
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100640)
        self.assertEqual(self.kassapaate.maukkaat, 1)

        #kun raha ei riitä
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100640)
        self.assertEqual(self.kassapaate.edulliset, 1)

        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100640)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    
    def test_korttiosto_toimii(self):
        
        #kun raha riittää
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(str(self.maksukortti), "saldo: 7.6")
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)
        self.assertEqual(str(self.maksukortti), "saldo: 3.6")
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
        self.assertEqual(self.kassapaate.edulliset, 2)

        #kun raha ei riitä
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)
        self.assertEqual(str(self.maksukortti), "saldo: 1.2")
        self.assertEqual(self.kassapaate.edulliset, 2)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)
        self.assertEqual(str(self.maksukortti), "saldo: 1.2")
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


    def test_kortille_voi_ladata_rahaa(self):

        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")



    