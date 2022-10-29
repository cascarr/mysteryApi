import unittest

from myst_view import Item, MysteryClass 


class MysteryClassTest(unittest.TestCase):

    def test_brie(self):
        items = [Item("Aged Brie", 45, 40)] # input
        chck_mysteryclass = MysteryClass(items)
        chck_mysteryclass.update()
        self.assertEqual("Aged Brie", items[0].name)

    def test_backstage(self):
        items = [Item("Backstage passes to a concert", 20, 40)] # input
        chck_mysteryclass = MysteryClass(items)
        chck_mysteryclass.update()
        self.assertEqual("Backstage passes to a concert", items[0].name)


if __name__ == "__main__":
    unittest.main()