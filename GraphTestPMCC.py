import unittest
from ActualCode import xCoords, yCoords, linear_regression
import numpy as np
x = xCoords
y = yCoords

def PmCc(x, y):
    meanx = np.mean(x)
    meany = np.mean(y)

    numerator = np.sum((x - meanx) * (y - meany))
    denominator_x = np.sqrt(np.sum((x - meanx)**2))
    denominator_y = np.sqrt(np.sum((y - meany)**2))

    p = numerator / (denominator_x * denominator_y)

    return p

class TestFunction(unittest.TestCase):

    def test_addition_lower_one(self):
        result = PmCc(x, y)
        self.assertLessEqual(abs(result), 1)


    def test_addition_greater_point_one(self):
        result = PmCc(x, y)
        self.assertGreaterEqual(abs(result), 0.1)


if __name__ == '__main__':
    unittest.main()