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
# tempalt = math.modf(123.678)
# D2 = tempalt[1]
# M2 = tempalt[0]
# print D2
# print math.modf(123.678)
# print M2

u = math.modf(666.777)
print u
tempalt = 567,789
D2 = tempalt[1]
M2 = tempalt[0]
altitudedig = {str(D2) + 'D' + str(round(M2,1))}
# values = {'altitude':"altitudedig"}
# values = {}
print altitudedig
