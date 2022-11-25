# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("Conjured foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Conjured foo", items[0].name)
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

        items = [Item("Conjured foo", 5, 5)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual("Conjured foo", items[0].name)
        self.assertEqual(3, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

        gilded_rose.update_quality()

        self.assertEqual("Conjured foo", items[0].name)
        self.assertEqual(1, items[0].quality)
        self.assertEqual(3, items[0].sell_in)

        gilded_rose.update_quality()

        self.assertEqual("Conjured foo", items[0].name)
        self.assertEqual(0, items[0].quality)
        self.assertEqual(2, items[0].sell_in)



        
if __name__ == '__main__':
    unittest.main()
