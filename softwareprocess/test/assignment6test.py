from unittest import TestCase
import softwareprocess.prod.dispatch as dispatch
from softwareprocess import prod as cs2d
import softwareprocess.prod.dispatch as DP


class convertString2DictionaryTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.errorDict = {'error':'true'}

#class MyTest(unittest.TestCase):

    def test_100_000_ShouldBeDictionary(self):
        values=None
        self.assertDictEqual(dispatch.dispatch(values),{'error': 'parameter is missing'})

    def test_100_010_OpShouldBeNotNone(self):
        values={}
        self.assertDictEqual(dispatch.dispatch(values),{'error':'no op is specified'})


    def test_100_020_ValuesShouldNotViolatesTheParameterDescriptionAbove(self):
        values={'op': 'unknown'}
        self.assertDictEqual(dispatch.dispatch(values),{'error':'op is not a legal operation'})

    # def test_100_010_RightAdjust(self):
    #
    #      self.assertDictEqual(dispatch.dispatch({'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}), {'altitude':'29d59.9', 'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'})
    #
    # def test_100_030_ValuesShouldNotViolatesTheParameterDescriptionAbove(self):
    #     values={'observation': '15d04.9', 'height': '6.0', 'pressure': '1010', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '72'}
        # self.assertDictEqual(dispatch.dispatch(values),{dispatch.dispatch(values)})
        # print dispatch.dispatch(values)
        # print values

        # print dip.
    def test_100_040_RightValuesPdfEx1(self):
        values={'observation': '10d00.0', 'height': '6.0', 'pressure': '1010', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '72'}
        # result={'altitude':'9d54.7','temperature': '72', 'height': '6.0', 'pressure': '1010', 'horizon': 'artificial', 'observation': '10d00.0', 'op': 'adjust'}
        result={'altitude':'9d54.7','temperature': '72', 'height': '6.0', 'pressure': '1010', 'horizon': 'artificial', 'observation': '10d00.0', 'op': 'adjust'}
        self.assertDictEqual(dispatch.dispatch(values),result)



    def test_100_050_RightValuesPdfEx2(self):
        values={'observation': '45d15.2', 'height': '6', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
        result={'altitude':'45d11.9', 'observation': '45d15.2', 'height': '6', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
        self.assertDictEqual(dispatch.dispatch(values),result)
        # print values

    def test_100_060_RightValuesXls2t1(self):
        values={'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
        result={'altitude':'29d59.9', 'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
        self.assertDictEqual(dispatch.dispatch(values),result)
        # print values

    def test_100_070_RightValuesPdfEx2t3(self):
        values={'observation': '42d0.0',  'op': 'adjust'}
        result={'altitude':'41d59.0', 'observation': '42d0.0',  'op': 'adjust'}
        self.assertDictEqual(dispatch.dispatch(values),result)
        # print values

    def test_100_080_NoOpInValuesEcl4(self):
        values={'observation': '15d04.9', 'height': '6.0', 'pressure': '1010', 'horizon': 'artificial', 'temperature': '72'}
        result={'observation': '15d04.9', 'height': '6.0', 'pressure': '1010', 'horizon': 'artificial', 'temperature': '72','error':'no op is specified'}
        self.assertDictEqual(dispatch.dispatch(values),result)
        # print values

    def test_100_090_RightValuesXls2t3(self):
        values={'observation': '42d0.0',  'op': 'adjust'}
        result={'altitude':'41d59.0', 'observation': '42d0.0',  'op': 'adjust'}
        self.assertDictEqual(dispatch.dispatch(values),result)
        # print values

    def test_100_100_RightValuesXls2t5(self):
        values={'observation': '42d0.0',  'op': 'adjust', 'extraKey':'ignore'}
        result={'altitude':'41d59.0', 'observation': '42d0.0',  'op': 'adjust', 'extraKey':'ignore'}
        self.assertDictEqual(dispatch.dispatch(values),result)
        # print values

    def test_100_110_InCoValuesXls2t6(self):
        values={'op': 'adjust'}
        result={'error':'mandatory information is missing'}
        self.assertDictEqual(dispatch.dispatch(values),result)
        # print values

    def test_100_120_InCoValuesXls2t7(self):
        values={'observation': '101d15.2', 'height': '6', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
        result={'observation': '101d15.2', 'height': '6', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71', 'error':'observation is invalid'}
        # {'temperature': '71', 'height': '6', 'pressure': '1010', 'horizon': 'natural', 'error': 'degree is not invalid__not in 0~90', 'observation': '101d15.2', 'op': 'adjust'}
        self.assertDictEqual(dispatch.dispatch(values),result)
        # print values

    def test_100_130_InCoValuesXls2t8(self):
        values={'observation': '45d15.2', 'height': 'a', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
        result={'observation': '45d15.2', 'height': 'a', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71', 'error':'height is invalid'}
        self.assertDictEqual(dispatch.dispatch(values),result)

    def test_100_140_InCoValuesXls2t9(self):
        values={'observation': '45d15.2', 'height': '6', 'horizon': '   ', 'pressure': '1010', 'op': 'adjust', 'temperature': '71'}
        result={'observation': '45d15.2', 'height': '6', 'horizon': '   ', 'pressure': '1010', 'op': 'adjust', 'temperature': '71', 'error':'horizon is invalid'}
        self.assertDictEqual(dispatch.dispatch(values),result)

    def test_100_141_InCoValuesXls2t9(self):
        values={'observation': '45d15.2', 'height': '6', 'horizon': 'a', 'pressure': '1010', 'op': 'adjust', 'temperature': '71'}
        result={'observation': '45d15.2', 'height': '6', 'horizon': 'a', 'pressure': '1010', 'op': 'adjust', 'temperature': '71', 'error':'horizon is invalid'}

    def test_100_150_OnlyObsAndOp(self):
        values={'observation': '45d15.2', 'op': 'adjust'}
        result={'altitude': '45d14.3', 'observation': '45d15.2', 'op': 'adjust'}
        self.assertDictEqual(dispatch.dispatch(values),result)

    def test_200_010_ObservationIsInvalidCauseMmnuteTooBig(self):
        values={'observation': '45d95.2', 'height': '6', 'horizon': '   ', 'pressure': '1010', 'op': 'adjust', 'temperature': '71'}
        result={'observation': '45d95.2', 'height': '6', 'horizon': '   ', 'pressure': '1010', 'op': 'adjust', 'temperature': '71','error':'observation is invalid'}
        self.assertDictEqual(dispatch.dispatch(values),result)
        print values

    def test_200_020_ObservationIsInvalidCauseMmnuteTooLess(self):
        values={'observation': '00d00.0', 'height': '6', 'horizon': '   ', 'pressure': '1010', 'op': 'adjust', 'temperature': '71'}
        result={'observation': '00d00.0', 'height': '6', 'horizon': '   ', 'pressure': '1010', 'op': 'adjust', 'temperature': '71','error':'observation is invalid'}
        self.assertDictEqual(dispatch.dispatch(values),result)
        print values

    def test_200_030_InCoValuesObservationDegreeIsTooBig(self):
        values={'observation': '110d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
        result={'observation': '110d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85','error':'observation is invalid'}
        self.assertDictEqual(dispatch.dispatch(values),result)

    def test_200_040_InCoValuesPressureIsTooBig(self):
        values={'observation': '30d1.5', 'height': '19.0', 'pressure': '2000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
        result={'observation': '30d1.5', 'height': '19.0', 'pressure': '2000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85','error':'pressure is invalid'}
        self.assertDictEqual(dispatch.dispatch(values),result)

    def test_200_040_InCoValuesPressureIsTooSmall(self):
        values={'observation': '30d1.5', 'height': '19.0', 'pressure': '99', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
        result={'observation': '30d1.5', 'height': '19.0', 'pressure': '99', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85','error':'pressure is invalid'}
        self.assertDictEqual(dispatch.dispatch(values),result)

    def test_200_050_InCoValuesPressureIsInvalid(self):
        values={'observation': '30d1.5', 'height': '19.0', 'pressure': 'a', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
        result={'observation': '30d1.5', 'height': '19.0', 'pressure': 'a', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85','error':'pressure is invalid'}
        self.assertDictEqual(dispatch.dispatch(values),result)

    def test_200_060_InCoValuesHorizonIsCharacter(self):
        values={'observation': '45d15.2', 'height': '6', 'horizon': 'a', 'pressure': '1010', 'op': 'adjust', 'temperature': '71'}
        result={'observation': '45d15.2', 'height': '6', 'horizon': 'a', 'pressure': '1010', 'op': 'adjust', 'temperature': '71', 'error':'horizon is invalid'}


    def test5_100_010_ValidValues(self):
        values={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42'}
        result={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42', 'long':'75d53.6', 'lat':'7d24.3'}
        self.assertDictEqual(dispatch.dispatch(values),result)

    def test5_200_010_InvalidValues1(self):
        values={'op': 'predict'}
        result={'error':'mandatory information is missing', 'op': 'predict'}
        self.assertDictEqual(dispatch.dispatch(values),result)

    def test5_200_020_InvalidValues1(self):
        values={'op':'predict', 'body': 'unknown', 'date': '2016-01-17', 'time': '03:15:42'}
        result={'op':'predict', 'body': 'unknown', 'date': '2016-01-17', 'time': '03:15:42', 'error':'star not in catalog'}
        self.assertDictEqual(dispatch.dispatch(values),result)

    def test5_200_030_InvalidValues1(self):
        values={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-99-17', 'time': '03:15:42'}
        self.assertTrue(dispatch.dispatch(values).has_key("error"), True)


    def test5_200_030_InvalidValues2(self):
        values={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:99'}
        result={'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:99', 'error':'invalid time'}
        self.assertDictEqual(dispatch.dispatch(values),result)

    def test5_200_040_InValidValues(self):
        values={'op':'predict', 'body': 'Betelgeuse', 'date': '2016:01:17', 'time': '03:15:42'}
        result={'op':'predict', 'body': 'Betelgeuse', 'date': '2016:01:17', 'time': '03:15:42', 'error':'invalid time'}
        self.assertDictEqual(dispatch.dispatch(values),result)

    def test5_200_050_InValidValues(self):
        values={'op':'predict', 'body': 'Betelgeuse', 'date': '2016 01 17', 'time': '03:15:42'}
        result={'op':'predict', 'body': 'Betelgeuse', 'date': '2016 01 17', 'time': '03:15:42', 'error':'invalid time'}
        self.assertDictEqual(dispatch.dispatch(values),result)

    def test6_200_050_InValidValues(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        result={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3', 'correctedDistance':'-3950', 'correctedAzimuth':'164d43.1'}
        self.assertDictEqual(dispatch.dispatch(values),result)

    # def test_100_010_ShouldBeNotNone(self):
    #     values={}
    #     self.assertDictEqual(dispatch.dispatch(values), {'error':'no op  is specified'})
    # {'observation': '15d04.9', 'height': '6.0', 'pressure': '1010', 'horizon': 'artificial', 'temperature': '72'}



# Acceptance test analysis
#   input:  inputString -> percent-encoded UTF-8, optional,
#           contains key-value pairs,    (key = value)*
#                   key is ([a..z]|[A..A])([a..z]|[A..Z]|[0..9]|[.])*
#                   value is ([a..z]|[A..Z]|[0..9]|[.])+
#   output: dictionary -> {'key':'value', (,'key': 'value')*}
#                   invalid input:  {'error':'true'}
#
#   happy path analysis
#       inputString =   010 nominal percent-encoded UTF-8 string with one key-value pair
#                           given:  quote("key=value")
#                           expected:  {'key':'value'}
#                       020 nominal percent-encoded UTF-8 string with one key-value pair
#                           given:  quote("key1=value,key2=value")
#                           expected:  {'key1':'value','key2':'value'}
#                       030 nominal percent-encoded UTF-8 string with .GT. two key-value pairs
#                           given:  quote("key1=value,key2=value,key3=value")
#                           expected:  {'key1':'value','key2':'value'}
#                       040 nominal percent-encoded UTF-8 string with blanks
#                           given:  quote(" key1 = value , key2 = value ")
#                           expected:  {'key1':'value','key2':'value'}
#
#   sad path analysis
#       inputString:    900 missing string
#                       905 blanks
#                       910 percent-encoded UTF-8 string with multiple key-value pairs, not comma
#                       915 percent-encoded UTF-8 string with duplicate key
#                       920 percent-encoded UTF-8 string with an invalid key (invalid = key no alpha)
#                       925 percent-encoded UTF-8 string with an invalid key (invalid = key missing)
#                       930 percent-encoded UTF-8 string with an invalid key (invalid = key with blank)
#                       935 percent-encoded UTF-8 string with an invalid key (invalid = key with invalid char)
#                       940 percent-encoded UTF-8 string with invalid value (invalid = value missing)
#                       945 percent-encoded UTF-8 string with invalid value (invalid = value with blank)
#                       950 percent-encoded UTF-8 string with invalid value (invalid = value with invalid char)
#                       955 percent-encoded UTF-8 string with missing key and missing value
#                       960 percent-encoded UTF-8 string with comma separator alone
#                       965 percent-encoded UTF-8 string with valid and invalid

# Happy path tests
#     def test_100_010_ShouldConvertNominalStringWithOneKeyValuePair(self):
#         encodedString = urllib.quote("key=value")
#         expectedResult = {'key':'value'}
#         self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), expectedResult,
#                              "Major defect:  not able to parse one key-value pair")
#
#     def test_100_020_ShouldConvertNominalStringWithOneKeyValuePairs(self):
#         encodedString = urllib.quote("key1=value,key2=value")
#         expectedResult = {'key1':'value','key2':'value'}
#         self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), expectedResult,
#                              "Major defect:  not able to parse comma separated pairs")
#
#     def test_100_030_ShouldConvertNominalStringWithMultipleKeyValuePairs(self):
#         encodedString = urllib.quote("key1=value,key2=value,key3=value")
#         expectedResult = {'key1':'value','key2':'value','key3':'value'}
#         self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), expectedResult,
#                              "Major defect:  not able to parse multiple comma spearated pairs")
#
#     def test_100_030_ShouldConvertNominalStringWithBlanks(self):
#         encodedString = urllib.quote(" key1 = value , key2 = value ")
#         expectedResult = {'key1':'value','key2':'value'}
#         self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), expectedResult,
#                              "Major defect:  not able to parse appropriate white space")
#
# # Sad path tests
#     def test_100_900_ShouldReturnErrorNoInput(self):
#         self.assertDictEqual(cs2d.convertString2Dictionary(), self.errorDict,
#                              "Major defect:  does not return proper result on missing parm")
# #
#     def test_100_905_ShouldReturnErrorNullString(self):
#         self.assertDictEqual(cs2d.convertString2Dictionary(" "), self.errorDict,
#                              "Minor defect:  does not return proper result on blank parm")
#
#     def test_100_910_ShouldReturnErrorOnMissingComma(self):
#         encodedString = urllib.quote("key1=value1 key2=value2")
#         self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
#                              "Major defect:  does not return proper result on missing comma")
#
#     def test_100_915_ShouldReturnErrorOnDuplicateKey(self):
#         encodedString = urllib.quote("key=value,key=value")
#         self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
#                              "Major defect:  does not return proper result on duplicate key")
#
#     def test_100_920_ShouldReturnErrorOnBadKeyName(self):
#         encodedString = urllib.quote("1key=value")
#         self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
#                              "Major defect:  does not return proper result on invalid key")
#
#     def test_100_925_ShouldReturnErrorOnMissingKey(self):
#         encodedString = urllib.quote("=value")
#         self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
#                              "Major defect:  does not return proper result on missing key")
#
#     def test_100_930_ShouldReturnErrorOnMissingKeyWithBlank(self):
#         encodedString = urllib.quote("ke y=value")
#         self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
#                              "Major defect:  does not return proper result on key with embedded blanks")
#
#     def test_100_935_ShouldReturnErrorOnKeyWithInvalidChar(self):
#         encodedString = urllib.quote("my_key=value")
#         self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
#                              "Major defect:  does not return proper result on key with invalid characters")
#
#     def test_100_940_ShouldReturnErrorOnMissingValue(self):
#         encodedString = urllib.quote("key=")
#         self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
#                              "Major defect:  does not return proper result on missing value")
#
#     def test_100_945_ShouldReturnErrorOnValueWithBlank(self):
#         encodedString = urllib.quote("key=va lue")
#         self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
#                              "Major defect:  does not return proper result on value with embedded blanks")
#
#     def test_100_950_ShouldReturnErrorOnValueWithInvalidChar(self):
#         encodedString = urllib.quote("key=va_lue")
#         self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
#                              "Major defect:  does not return proper result on value with invalid characters")
#
#     def test_100_955_ShouldReturnErrorOnMissingKeyMissingValue(self):
#         encodedString = urllib.quote("=")
#         self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
#                              "Major defect:  does not return proper result on missing key and missing value")
#
#     def test_100_960_ShouldReturnErrorOnLoneComma(self):
#         encodedString = urllib.quote(",")
#         self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
#                              "Major defect:  does not return proper result on empty separator")
#
#     def test_100_960_ShouldReturnErrorOnValidInvalidKeyValuePair(self):
#         encodedString = urllib.quote("key1=value,key2=")
#         self.assertDictEqual(cs2d.convertString2Dictionary(encodedString), self.errorDict,
#                              "Major defect:  does not return proper result on mix of valid and invalid items")
    def test6__000_010_ValidValues(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        result={'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3', 'correctedDistance':'3950', 'correctedAzimuth':'164d42.9'}
        self.assertDictEqual(DP.dispatch(values),result)
    def test6__000_011_ValidValues(self):
        values={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4',  'assumedLat':'35d59.7', 'assumedLong':' 74d35.3'}
        result={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4',  'assumedLat':'35d59.7', 'assumedLong':' 74d35.3', 'correctedDistance':'104', 'correctedAzimuth':'0d36.8'}
        # self.assertAlmostEquals(int(values['correctedDistance']), 104, delta=1)
        # self.assertDictEqual(DP.dispatch(values),result)
    # def test6__000_010_ValidValues(self):
    #     values={'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
    #     result={'extraKey':'ignore','op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3', 'correctedDistance':'3950', 'correctedAzimuth':'164d42.9'}
    #     self.assertDictEqual(DP.dispatch(values),result)
# 'extraKey':'ignore'
    # def test6__100_000_InValidValues(self):
    #     values={'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
    #     self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_020_InValidValueshavenotlat(self):
        values={'op':'correct','long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__200_021_InValidValueshavenotvaludoflat(self):
        values={'op':'correct','lat':'','long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__200_022_InValidValueshavenotvaludoflatspace(self):
        values={'op':'correct','lat':' ','long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__200_0221_InValidValueshavenotvaludoflatdots(self):
        values={'op':'correct','lat':'....','long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__200_023_InValidValueslat0havedot(self):
        values={'op':'correct', 'lat':'16.0d32.3', 'long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_030_InValidValueslat0iscarcater(self):
        values={'op':'correct', 'lat':'aad32.3', 'long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_040_InValidValueslat0isnull(self):
        values={'op':'correct', 'lat':'d32.3', 'long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_050_InValidValueslat0isspace(self):
        values={'op':'correct', 'lat':' d32.3', 'long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_060_InValidValueslat0ismultyspaces(self):
        values={'op':'correct', 'lat':'    d32.3', 'long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_120_InValidValueslat1havenotdot(self):
        values={'op':'correct', 'lat':'16d32', 'long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)

    def test6__200_130_InValidValueslat1iscarcater(self):
        values={'op':'correct', 'lat':'16daa', 'long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_140_InValidValueslat1isnull(self):
        values={'op':'correct', 'lat':'16d', 'long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_150_InValidValueslat1isspace(self):
        values={'op':'correct', 'lat':'16d ', 'long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_160_InValidValueslat1ismultyspaces(self):
        values={'op':'correct', 'lat':'16d  ', 'long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)

# ====above is about lat
    def test6__200_120_InValidValueshavenotlong(self):
        values={'op':'correct', 'lat':'16d32.3', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__200_021_InValidValueshavenotvaludoflong(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__200_022_InValidValueshavenotvaludoflongspace(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':' ','altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__200_0221_InValidValueshavenotvaludoflongdots(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'.....6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__200_023_InValidValueslat0have2dot(self):
        values={'op':'correct',  'lat':'16d32.3', 'long':'95d41..6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_030_InValidValueslong0iscarcater(self):
        values={'op':'correct',  'lat':'16d32.3', 'long':'aad41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_040_InValidValueslong0isnull(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_050_InValidValueslong0isspace(self):
        values={'op':'correct', 'lat':' 16d32.3', 'long':'  41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_060_InValidValueslong0ismultyspaces(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'  d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_120_InValidValueslong1havenotdot(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95d41', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)

    def test6__200_130_InValidValueslong1iscarcater(self):
        values={'op':'correct', 'lat':'16daa', 'long':'95dss', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_140_InValidValueslong1isnull(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95d', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_150_InValidValueslong1isspace(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95d ', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_160_InValidValueslong1ismultyspaces(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95d   ', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
# ====above is about long

    def test6__200_210_InValidValueshavenotaltitude(self):
        values={'op':'correct','lat':'16d32.3','long':'95.41.6', 'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__200_211_InValidValueshavenotvaludofaltitude(self):
        values={'op':'correct','lat':'16d32.3','long':'95.41.6', 'altitude':'',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__200_212_InValidValueshavenotvaludofaltitudespace(self):
        values={'op':'correct','lat':'16d32.3','long':'95.41.6', 'altitude':' ',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__200_2121_InValidValueshavenotvaludofaltitudedots(self):
        values={'op':'correct','lat':'16d32.3','long':'95.41.6', 'altitude':'.....3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__200_223_InValidValuesaltitude0havedot(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13.0d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_230_InValidValuesaltitude0iscarcater(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'aad42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_240_InValidValuesaltitude0isnull(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_250_InValidValuesaltitude0isspace(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':' d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_260_InValidValuesaltitude0ismultyspaces(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_320_InValidValuesaltitude1havenotdot(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d42',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)

    def test6__200_330_InValidValuesaltitude1iscarcater(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13daa',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_340_InValidValuesaltitude1isnull(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_350_InValidValuesaltitude1isspace(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d ',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_360_InValidValuesaltitude1ismultyspaces(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d   ',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__200_361_InValidValuesaltitude1ismultyspaces(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'    13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
# ====above is about altitude

    def test6__200_410_InValidValueshavenotassumedLat(self):
        values={'op':'correct','lat':'16d32.3','long':'95.41.6', 'altitude':'13d42.3','assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__200_411_InValidValueshavenotvaludofassumedLat(self):
        values={'op':'correct','lat':'16d32.3','long':'95.41.6', 'altitude':'13d42.3','assumedLat':'', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__200_412_InValidValueshavenotvaludofassumedLatspace(self):
        values={'op':'correct','lat':'16d32.3','long':'95.41.6', 'altitude':'13d42.3 ',  'assumedLat':' ', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__200_4121_InValidValueshavenotvaludofassumedLatdots(self):
        values={'op':'correct','lat':'16d32.3','long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-.....4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__200_423_InValidValuesassumedLat0havedot(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53.0d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_430_InValidValuesassumedLat0iscarcater(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'aad42.3',  'assumedLat':'-aad38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_440_InValidValuesassumedLat0isnull(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'d42.3',  'assumedLat':'d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_450_InValidValuesassumedLat0isspace(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':' d42.3',  'assumedLat':' d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_460_InValidValuesassumedLat0ismultyspaces(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'  d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__201_320_InValidValuesassumedLat1havenotdot(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)

    def test6__201_330_InValidValuesassumedLat1iscarcater(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13daa',  'assumedLat':'-53daa', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__201_340_InValidValuesassumedLat1isnull(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d',  'assumedLat':'-53d', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__201_350_InValidValuesassumedLat1isspace(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d ',  'assumedLat':'-53d  ', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__201_360_InValidValuesassumedLat1ismultyspaces(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d   ',  'assumedLat':'-53d  ', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__201_361_InValidValuesassumedLat1ismultyspaces(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'    13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)

# ====above is about assumedLat
    def test6__220_410_InValidValueshavenotassumedLong(self):
        values={'op':'correct','lat':'16d32.3','long':'95.41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__220_411_InValidValueshavenotvaludofassumedLong(self):
        values={'op':'correct','lat':'16d32.3','long':'95.41.6', 'altitude':'13d42.3','assumedLat':'-53d38.4', 'assumedLong':''}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__220_412_InValidValueshavenotvaludofassumedLongspace(self):
        values={'op':'correct','lat':'16d32.3','long':'95.41.6', 'altitude':'13d42.3 ','assumedLat':'-53d38.4', 'assumedLong':' '}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__220_4121_InValidValueshavenotvaludofassumedLongdots(self):
        values={'op':'correct','lat':'16d32.3','long':'95.41.6', 'altitude':'13d42.3', 'assumedLat':'-53d38.4', 'assumedLong':' .....3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__220_4122_InValidValueshavenotvaludofassumedLongcaracters(self):
        values={'op':'correct','lat':'16d32.3','long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' sssdddd'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__220_423_InValidValuesassumedLong0havedot(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74.0d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__220_430_InValidValuesassumedLong0iscarcater(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'aad42.3',  'assumedLat':'-53d38.4', 'assumedLong':' aad35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__220_440_InValidValuesassumedLong0isnull(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'d42.3',  'assumedLat':'-53d38.4', 'assumedLong':'d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__220_450_InValidValuesassumedLong0isspace(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':' d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__220_460_InValidValuesassumedLong0ismultyspaces(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':'    d35.3'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__221_320_InValidValuesassumedLong1havenotdot(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)

    def test6__221_330_InValidValuesassumedLong1iscarcater(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13daa',   'assumedLat':'-53d38.4', 'assumedLong':' 74daa'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__221_340_InValidValuesassumedLong1isnull(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d',   'assumedLat':'-53d38.4', 'assumedLong':' 74d'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__221_350_InValidValuesassumedLong1isspace(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d ',   'assumedLat':'-53d38.4', 'assumedLong':' 74d '}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__221_360_InValidValuesassumedLong1ismultyspaces(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95.41.6', 'altitude':'13d   ',  'assumedLat':'-53d38.4', 'assumedLong':' 74d    '}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)

# ====above is about assumedLat
    def test6__331_000_InValidValuesassumedLong1ismultyspaces(self):
        values={}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__331_010_InValidValuesassumedLong1ismultyspaces(self):
        values=42
        self.assertTrue(DP.dispatch(values).has_key("error"), True)

    def test6__331_020_InValidValuesassumedLong1ismultyspaces(self):
        values={'op': 'unknown'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    #
    # def test6__331_030_InValidValuesassumedLong1ismultyspaces(self):
    #     DP.dispatch()
    #     self.assertTrue(DP.dispatch(values).has_key("error"), True)
