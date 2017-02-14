from unittest import TestCase
import softwareprocess.Sample

class SampleTest(Teastcase):
    pass

# ______________
# ____acceptance tests
#   100 constructor
#   Desired level of confidence Boundary Value Analysis
#       Input/Ourput analysis:
#       input: n -> interger .GE. 2 and .LT 30. mandatory, unvalidated
#       Output:instance of Sample
#       Happy path analysis;
#           n: nominal value  4 expected result: instance of sample
#              low bound      2  expected result: instance of sample
#               high bound    29 expected result: instance of sample
#       San path analysis:
#           n: non-int n        4.2 expected result: exception
#           n: out of bounds n 1  expected result: exception
#               ditto           30 expected result: ditto
#           n: is missing       missing n       expected result: exception
#
#  Happy path
    def     test100_010_sholdCoustructInstance(self);
            self.assertIsInstance()S.Samle(4),S.Sample
    def test100_020_ShouldConstructInstanceWithLowBound(self):
        myS = S.Sample(2)
        self.assertIsInstance(myS.S.Sample)
        self.assertEauIs()

