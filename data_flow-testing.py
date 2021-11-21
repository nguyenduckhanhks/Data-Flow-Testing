import unittest
def get_price(riceKg, distance):
    
    if riceKg <= 0 or riceKg >= 1000 or distance <= 0 or distance >= 50:
        return -1

    price = 0.0
    if riceKg > 0 and riceKg < 50:
        price = 18000 * riceKg
    elif riceKg >= 50 and riceKg < 100:
        price = 17000 * riceKg
    elif riceKg >= 100 and riceKg < 1000:
        price = 16000 * riceKg
    
    if distance < 10:
        price = price / 1.25
    
    return price

class TestMethods(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_price(10, 5), 144000)

    def test2(self):
        self.assertEqual(get_price(10, 20), 180000)

    def test3(self):
        self.assertEqual(get_price(60, 20), 1020000)

    def test4(self):
        self.assertEqual(get_price(200, 20), 3200000)

if __name__ == '__main__':
    unittest.main()