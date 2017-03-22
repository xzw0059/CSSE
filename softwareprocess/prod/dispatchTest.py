import unittest
import softwareprocess.prod.dispatch as dispatch
import math
#
# class MyTestCase(unittest.TestCase):
#     def setUp(self):
#         pass
#     def tearDown(self):
#         pass
#
#     def test100_ShouldReturnErrorWhenNoValues(self):
#         values = {}
#         self.assertDictEqual(dispatch.dispatch(values),{'error':'no op  is specified'})
#
#
# if __name__ == '__main__':
#     unittest.main()
# print math.tan(90d30)
tempalt = math.modf(123.678)
D2 = tempalt[1]
# M2 = tempalt[2]
print D2
print math.modf(123.678)
