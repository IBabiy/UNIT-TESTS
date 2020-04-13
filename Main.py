import unittest
class Main():
    def __init__(self,x):

        while True:
            try:
                self.x = float(x)
                if (self.x <= 36.868 or self.x >= 2.557):
                    break
            except(ValueError, NameError,SyntaxError):
                print('Введіть число! Invalid value')

    def outputting(self,x):
        mas = []
        mas.append((self.x) ** 4 * 4.769 + (self.x) ** 3 * 4.159 + (self.x) ** 2 * 2.745 + (self.x) * 4.503)
        mas.append((self.x)**3*2-(self.x)**2*2.578+(self.x)*6.966)
        mas.append((self.x)**2*1.575+x*3.894)
        mas.append((self.x)*2.664)
        return mas

class MainTest(unittest.TestCase):

    def testnormal(self):
        main = Main(2)
        res = main.outputting(2)
        self.assertEqual(res,[129.562, 19.62, 14.088000000000001, 5.328])

    def testminus(self):
        main = Main(-3)
        res = main.outputting(-3)
        self.assertEqual(res, [285.19199999999995, -98.1, 2.4929999999999986, -7.992000000000001])

    def testnormal2(self):
        main = Main(11)
        res = main.outputting(11)
        self.assertEqual(res,[75740.236, 2426.688, 233.409, 29.304000000000002])

    def testminus2(self):
        main = Main(-5)
        res = main.outputting(-5)
        self.assertEqual(res, [285.19199999999995, -98.1, 2.4929999999999986, -7.992000000000001])

    def testminus3(self):
        main = Main(dw)
        res = main.outputting(dw)
        self.assertEqual(res, [285.19199999999995, -98.1, 2.4929999999999986, -7.992000000000001])

    def testminus4(self):
        main = Main(    3)
        res = main.outputting(  3)
        self.assertEqual(res, [536.796, 51.696, 25.857, 7.992000000000001])

    def testminus5(self):
        main = Main(3,1)
        res = main.outputting(3,1)
        self.assertEqual(res, [536.796, 51.696, 25.857, 7.992000000000001])

    def testminus6(self):
        main = Main(999)
        res = main.outputting(999)
        self.assertEqual(res, [9152464.151999999, 98034.45999999999, 2300.2529999999997, 98.56800000000001])

    def testminus7(self):
        main = Main(-10)
        res = main.outputting(-10)
        self.assertEqual(res, [2506.86, -349.28, 19.905, -13.32])

    def testminus8(self):
        main = Main(-15)
        res = main.outputting(-15)
        self.assertEqual(res, [43760.47, -2327.46, 118.56, -26.64])

    def testminus9(self):
        main = Main(37)
        res = main.outputting(37)
        self.assertEqual(res, [227944.08, -7434.54, 295.965, -39.96])

    def testminus10(self):
        main = Main(39)
        res = main.outputting(39)
        self.assertEqual(res, [9152464.151999999, 98034.45999999999, 2300.2529999999997, 98.56800000000001])

unittest.main()



