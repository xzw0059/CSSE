import unittest

import softwareprocess.prod.dispatch as DP

class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test6__000_010_ValidValues(self):
        values={'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        result={'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3', 'correctedDistance':'3950', 'correctedAzimuth':'164d42.9'}
        self.assertDictEqual(DP.dispatch(values),result)


    def test6__000_011_ValidValues(self):
        values={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4',  'assumedLat':'35d59.7', 'assumedLong':' 74d35.3'}
        result={'op':'correct', 'lat':'89d20.1', 'long':'154d5.4', 'altitude':'37d17.4',  'assumedLat':'35d59.7', 'assumedLong':' 74d35.3', 'correctedDistance':'104', 'correctedAzimuth':'0d36.8'}

        # self.assertAlmostEquals(int(values['correctedDistance']), 104, delta=1)
        self.assertDictEqual(DP.dispatch(values),result)
    # def test6__000_010_ValidValues(self):
    #     values={'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
    #     result={'extraKey':'ignore','op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3', 'correctedDistance':'3950', 'correctedAzimuth':'164d42.9'}
    #     self.assertDictEqual(DP.dispatch(values),result)
# 'extraKey':'ignore'
    # def test6__100_000_InValidValues(self):
    #     values={'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
    #     self.assertTrue(DP.dispatch(values).has_key("error"), True)
        # print DP.dispatch(values)
    def test6__200_012_inValidValues(self):
        values={'op':'correct', 'lat':'16-23.4', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        result={'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3', 'correctedDistance':'3950', 'correctedAzimuth':'164d42.9'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__200_013_inValidValues(self):
        values={'op':'correct', 'lat':32, 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        result={'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3', 'correctedDistance':'3950', 'correctedAzimuth':'164d42.9'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__000_014_ValidValues(self):
        values={'op':'correct', 'lat':'16D32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        result={'op':'correct', 'lat':'16D32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3', 'correctedDistance':'3950', 'correctedAzimuth':'164d42.9'}
        self.assertDictEqual(DP.dispatch(values),result)
    def test6__000_014_ValidValues(self):
        values={'op':'correct', 'lat':'16Dd32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        result={'op':'correct', 'lat':'16Dd32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3', 'correctedDistance':'3950', 'correctedAzimuth':'164d42.9'}
        self.assertDictEqual(DP.dispatch(values),result)
    def test6__200_010_inValidValues(self):
        values={'op':'correct', 'lat':'16aad32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        result={'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3', 'correctedDistance':'3950', 'correctedAzimuth':'164d42.9'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
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
