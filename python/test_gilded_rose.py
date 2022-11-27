# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_conjured_simple_item(self):

        conjured_simple_item = Item("Conjured Foo", 2, 11)
        items = [conjured_simple_item]
        gilded_rose = GildedRose(items)

        # day1
        gilded_rose.update_quality()
        self.assertEqual(9, conjured_simple_item.quality)
        self.assertEqual(1, conjured_simple_item.sell_in)

        # day2
        gilded_rose.update_quality()
        self.assertEqual(7, conjured_simple_item.quality)
        self.assertEqual(0, conjured_simple_item.sell_in)

        # day3
        gilded_rose.update_quality()
        self.assertEqual(3, conjured_simple_item.quality)
        self.assertEqual(-1, conjured_simple_item.sell_in)

        # day4
        gilded_rose.update_quality()
        self.assertEqual(0, conjured_simple_item.quality)
        self.assertEqual(-2, conjured_simple_item.sell_in)

    def test_simple_item(self):

        simple_item = Item("Foo", 2, 5)
        items = [simple_item]
        gilded_rose = GildedRose(items)

        # day1
        gilded_rose.update_quality()
        self.assertEqual(4, simple_item.quality)
        self.assertEqual(1, simple_item.sell_in)

        # day2
        gilded_rose.update_quality()
        self.assertEqual(3, simple_item.quality)
        self.assertEqual(0, simple_item.sell_in)

        # day3
        gilded_rose.update_quality()
        self.assertEqual(1, simple_item.quality)
        self.assertEqual(-1, simple_item.sell_in)

        # day4
        gilded_rose.update_quality()
        self.assertEqual(0, simple_item.quality)
        self.assertEqual(-2, simple_item.sell_in)

    def test_conjured_aged_brie(self):
        conjured_simple_item = Item("Conjured Aged Brie", 2, 5)
        items = [conjured_simple_item]
        gilded_rose = GildedRose(items)

        # day1 (+2 quality)
        gilded_rose.update_quality()
        self.assertEqual(7, conjured_simple_item.quality)
        self.assertEqual(1, conjured_simple_item.sell_in)

        # day2 (+2 quality)
        gilded_rose.update_quality()
        self.assertEqual(9, conjured_simple_item.quality)
        self.assertEqual(0, conjured_simple_item.sell_in)

        # day3 (+4 quality)
        gilded_rose.update_quality()
        self.assertEqual(13, conjured_simple_item.quality)
        self.assertEqual(-1, conjured_simple_item.sell_in)

    def test_aged_brie(self):
        simple_item = Item("Aged Brie", 2, 5)
        items = [simple_item]
        gilded_rose = GildedRose(items)

        # day1 (+1 quality)
        gilded_rose.update_quality()
        self.assertEqual(6, simple_item.quality)
        self.assertEqual(1, simple_item.sell_in)

        # day2 (+1 quality)
        gilded_rose.update_quality()
        self.assertEqual(7, simple_item.quality)
        self.assertEqual(0, simple_item.sell_in)

        # day3 (+2 quality)
        gilded_rose.update_quality()
        self.assertEqual(9, simple_item.quality)
        self.assertEqual(-1, simple_item.sell_in)

    def test_concert_pass(self):
        simple_item = Item("Backstage passes to a TAFKAL80ETC concert", 12, 5)
        items = [simple_item]
        gilded_rose = GildedRose(items)

        # day1 (+1 quality)
        gilded_rose.update_quality()
        self.assertEqual(6, simple_item.quality)
        self.assertEqual(11, simple_item.sell_in)

        # day2 (+2 quality)
        gilded_rose.update_quality()
        self.assertEqual(8, simple_item.quality)
        self.assertEqual(10, simple_item.sell_in)

        #day 3, 4, 5, 6
        gilded_rose.update_quality() # (+2 quality)
        gilded_rose.update_quality() # (+2 quality)
        gilded_rose.update_quality() # (+2 quality)
        gilded_rose.update_quality() # (+2 quality)

        self.assertEqual(16, simple_item.quality)
        self.assertEqual(6, simple_item.sell_in)

        # day 7 (+3 quality)
        gilded_rose.update_quality()
        self.assertEqual(19, simple_item.quality)
        self.assertEqual(5, simple_item.sell_in)

        # day 8, 9, 10, 11, 12
        gilded_rose.update_quality()  # (+3 quality)
        gilded_rose.update_quality()  # (+3 quality)
        gilded_rose.update_quality()  # (+3 quality)
        gilded_rose.update_quality()  # (+3 quality)
        gilded_rose.update_quality()  # (+3 quality)

        self.assertEqual(34, simple_item.quality)
        self.assertEqual(0, simple_item.sell_in)

        # day 13
        gilded_rose.update_quality()  # (0 == quality)

        self.assertEqual(0, simple_item.quality)
        self.assertEqual(-1, simple_item.sell_in)

        # day 14
        gilded_rose.update_quality()  # (0 == quality)

        self.assertEqual(0, simple_item.quality)
        self.assertEqual(-2, simple_item.sell_in)

    def test_conjured_concert_pass(self):
        simple_item = Item("Conjured Backstage passes to a TAFKAL80ETC concert", 12, 5)
        items = [simple_item]
        gilded_rose = GildedRose(items)

        # day1 (+2 quality)
        gilded_rose.update_quality()
        self.assertEqual(7, simple_item.quality)
        self.assertEqual(11, simple_item.sell_in)

        # day2 (+4 quality)
        gilded_rose.update_quality()
        self.assertEqual(11, simple_item.quality)
        self.assertEqual(10, simple_item.sell_in)

        #day 3, 4, 5, 6
        gilded_rose.update_quality() # (+4 quality)
        gilded_rose.update_quality() # (+4 quality)
        gilded_rose.update_quality() # (+4 quality)
        gilded_rose.update_quality() # (+4 quality)

        self.assertEqual(27, simple_item.quality)
        self.assertEqual(6, simple_item.sell_in)

        # day 7 (+6 quality)
        gilded_rose.update_quality()
        self.assertEqual(33, simple_item.quality)
        self.assertEqual(5, simple_item.sell_in)

        # day 8, 9, 10, 11, 12
        gilded_rose.update_quality()  # (+6 quality)
        gilded_rose.update_quality()  # (+6 quality)
        gilded_rose.update_quality()  # (+6 quality) capped to 50
        gilded_rose.update_quality()  # (+6 quality) capped to 50
        gilded_rose.update_quality()  # (+6 quality) capped to 50

        self.assertEqual(50, simple_item.quality)
        self.assertEqual(0, simple_item.sell_in)

        # day 13
        gilded_rose.update_quality()  # (0 == quality)

        self.assertEqual(0, simple_item.quality)
        self.assertEqual(-1, simple_item.sell_in)

        # day 14
        gilded_rose.update_quality()  # (0 == quality)

        self.assertEqual(0, simple_item.quality)
        self.assertEqual(-2, simple_item.sell_in)

    def test_sulfuras(self):
        simple_item = Item("Sulfuras, Hand of Ragnaros", 2, 80)
        items = [simple_item]
        gilded_rose = GildedRose(items)

        # day 1
        gilded_rose.update_quality()  # (still same quality)
        self.assertEqual(80, simple_item.quality)
        self.assertEqual(1, simple_item.sell_in)

        # day 2
        gilded_rose.update_quality()  # (still same quality)
        self.assertEqual(80, simple_item.quality)
        self.assertEqual(0, simple_item.sell_in)

        # day 3
        gilded_rose.update_quality()  # (still same quality)
        self.assertEqual(80, simple_item.quality)
        self.assertEqual(-1, simple_item.sell_in)

    def test_conjured_sulfuras(self):
        simple_item = Item("Conjured Sulfuras, Hand of Ragnaros", 2, 80)
        items = [simple_item]
        gilded_rose = GildedRose(items)

        # day 1
        gilded_rose.update_quality()  # (still same quality)
        self.assertEqual(80, simple_item.quality)
        self.assertEqual(1, simple_item.sell_in)

        # day 2
        gilded_rose.update_quality()  # (still same quality)
        self.assertEqual(80, simple_item.quality)
        self.assertEqual(0, simple_item.sell_in)

        # day 3
        gilded_rose.update_quality()  # (still same quality)
        self.assertEqual(80, simple_item.quality)
        self.assertEqual(-1, simple_item.sell_in)

    def test_item_quality_over_50(self):
        simple_item = Item("Aged Brie", 1, 45)
        items = [simple_item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(46, simple_item.quality)
        self.assertEqual(0, simple_item.sell_in)

        gilded_rose.update_quality()
        self.assertEqual(48, simple_item.quality)
        self.assertEqual(-1, simple_item.sell_in)

        gilded_rose.update_quality()
        self.assertEqual(50, simple_item.quality)
        self.assertEqual(-2, simple_item.sell_in)

        gilded_rose.update_quality()
        self.assertEqual(50, simple_item.quality)
        self.assertEqual(-3, simple_item.sell_in)

    def test_item_quality_below_0(self):
        simple_item = Item("Foo", 1, 2)
        items = [simple_item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(1, simple_item.quality)
        self.assertEqual(0, simple_item.sell_in)

        gilded_rose.update_quality()
        self.assertEqual(0, simple_item.quality)
        self.assertEqual(-1, simple_item.sell_in)

        gilded_rose.update_quality()
        self.assertEqual(0, simple_item.quality)
        self.assertEqual(-2, simple_item.sell_in)

        gilded_rose.update_quality()
        self.assertEqual(0, simple_item.quality)
        self.assertEqual(-3, simple_item.sell_in)



        
if __name__ == '__main__':
    unittest.main()
