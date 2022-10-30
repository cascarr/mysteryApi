import unittest

from myst_view import Item, MysteryClass 
#from apiapp import views 



class MysteryClassTest(unittest.TestCase):

    def test_brie(self):
        items = [Item("Aged Brie", 45, 40)] # input
        chck_mysteryclass = MysteryClass(items) # checking with MysteryClass
        chck_mysteryclass.update() # MysteryClass method check
        self.assertEqual("Aged Brie", items[0].name) # output

    def test_backstage(self):
        items = [Item("Backstage passes to a concert", 20, 40)] # input
        chck_mysteryclass = MysteryClass(items) # checking with MysteryClass
        chck_mysteryclass.update() # MysteryClass method check
        self.assertEqual("Backstage passes to a concert", items[0].name) # output

    def test_sulfuras(self):
        items = [Item("Sulfuras", 29, 47)] # input
        chck_mysteryclass = MysteryClass(items) # checking with MysteryClass
        chck_mysteryclass.update() # MysteryClass method check
        self.assertEqual("Sulfuras", items[0].name) # output


if __name__ == "__main__":
    unittest.main()