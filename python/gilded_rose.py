# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items


    def check_conjured(self, item):
        return "conjured" in item.name.lower()

    def update_aged_brie(self, item):
        if item.quality < 50:
            item.quality += 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1

    def update_concert_pass(self, item):
        if item.sell_in < 0:
            item.quality = 0
        elif item.quality < 50:
            item.quality += 1
            if item.sell_in <= 10 and item.quality < 50:
                item.quality += 1
                if item.sell_in <= 5 and item.quality < 50:
                    item.quality += 1

    def update_sulfuras(self, item):
        pass

    def update_simple_item(self, item):

        if item.quality > 0:
            item.quality -= 1
            if item.sell_in < 0 and item.quality > 0:
                item.quality -= 1

    def update_quality(self):

        for item in self.items:

            # update sell_in
            item.sell_in -= 1

            # check if item is conjured
            is_conjured = self.check_conjured(item)

            # update item quality value x1 if its normal, x2 if its conjured
            if 'Aged Brie' in item.name:
                self.update_aged_brie(item)
                if is_conjured:
                    self.update_aged_brie(item)
            elif 'Backstage passes to a TAFKAL80ETC concert' in item.name:
                self.update_concert_pass(item)
                if is_conjured:
                    self.update_concert_pass(item)
            elif 'Sulfuras, Hand of Ragnaros' in item.name:
                self.update_sulfuras(item)
                if is_conjured:
                    self.update_sulfuras(item)
            else:
                self.update_simple_item(item)
                if is_conjured:
                    self.update_simple_item(item)


        """
        
        Això depen de com interpretem quan actualitzar el valor del sell_in, si al
        final del dia pel dia següent (en aquest cas s'actualitzaria al final) o posar-lo al principi per
        res més obrir la tenda actualitzar-ho tot per aquell mateix dia.
        
        """



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
