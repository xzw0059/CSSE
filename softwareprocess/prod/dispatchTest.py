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

    def test6__200_010_inValidValues(self):
        values={'op':'correct', 'lat':'16aad32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        result={'op':'correct', 'lat':'16d32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3', 'correctedDistance':'3950', 'correctedAzimuth':'164d42.9'}
        self.assertTrue(DP.dispatch(values).has_key("error"), True)
    def test6__200_011_ValidValues(self):
        values={'op':'correct', 'lat':'16Dd32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3'}
        result={'op':'correct', 'lat':'16Dd32.3', 'long':'95d41.6', 'altitude':'13d42.3',  'assumedLat':'-53d38.4', 'assumedLong':' 74d35.3', 'correctedDistance':'3950', 'correctedAzimuth':'164d42.9'}
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
#     #     self.assertTrue(DP.dispatch(values).has_key("error"), True)
# import unittest
#
# import softwareprocess.dispatch as DP
#
# class MyTestCase(unittest.TestCase):
#     def setUp(self):
#         pass
#
#     def tearDown(self):
#         pass

        # -----------------------------------------------------------------------
        # ---- Acceptance Tests
        # 100 dispatch operation
        #   Happy path analysis:
        #        values:      mandatory
        #                     dictionary
        #                     Operations:   {'op':'adjust'}
        #                                   {'op':'predict'}
        #                                   {'op':'correct'}
        #                                   {'op':'locate'}
        #   Sad path analysis:
        #        values:
        #                     no op specified             values={}
        #                        -- return {'error':'no op  is specified'}
        #                     contain 'error' as a key      values={5d04.9', 'height': '6.0', 'pressure': '1010',
        #                                                           'horizon': 'artificial', 'temperature': '72'
        #                                                           'error':'no op is specified'}'
        #                        -- return values without error as a key and without its values
        #                     not-dictionary                values=42
        #                        -- return {'error':'parameter is not a dictionary'}
        #                     not legal operation           values={'op': 'unknown'}
        #                        -- return {'error':'op is not a legal operation'}
        #                     missing dictionary            dispatch()
        #                        -- return {'error':'dictionary is missing'}
        # Happy path

        # def test100_010ShouldReturnUnchangedValuesWithOperationCorrect(self):
        #     values = {'op': 'correct'}
        #     self.assertDictEqual(DP.dispatch(values), values)
        #
        # def test100_020ShouldReturnUnchangedValuesWithOperationLocate(self):
        #     values = {'op': 'locate'}
        #     self.assertDictEqual(DP.dispatch(values), values)
        #
        # # Sad path
        # def test100_910_ShouldReturnValuesWithErrorKeyWhenNoOpSpecified(self):
        #     values = {}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test100_920ShouldReturnValuesWithErrorWhenParameterIsNotADictionary(self):
        #     values = 42
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test100_930ShouldReturnValuesWithErrorWhenOpNotALegalOperation(self):
        #     values = {'op': 'unknown'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test100_940ShouldReturnValuesWithErrorWhenDictionaryMissing(self):
        #     self.assertEqual(DP.dispatch().has_key("error"), True)

        # -----------------------------------------------------------------------
        # ---- Acceptance Tests
        # 200 operation {'op': 'adjust'}
        #    Happy path analysis:
        #        observation: mandatory string in the form of xdy.y
        #                     x : is degree portion of the altitude
        #                         positive integer  where 0<=x<90
        #                         low bound x=0
        #                         high bound x=89
        #                     d : character that is used to separate degrees from minutes
        #                     y : minutes
        #                         positive floating point where 0.0<=y<60.0
        #                         low bound  y=0
        #                         high bound y=59.9
        #        height:      optional string
        #                     numerical value(in feet) where height>0
        #                     low bound      height=0
        #                     missing height height=0
        #        temperature: Temperature (in degrees F)
        #                     optional string
        #                     integer where -20<=temperature<=120
        #                     low bound      temperature = -20
        #                     high bound     temperature = 120
        #                     if missing     temperature = 72
        #        pressure:    Barometric pressure(in mbar) at the time observation
        #                     optional string
        #                     integer where 100<=pressure<=1100
        #                     low bound      pressure = 100
        #                     high bound     pressure = 1100
        #                     if missing     pressure = 1010
        #        horizon:     what the observed altitude is relative to
        #                     optional case-insensitive strings
        #                     horizon ="artificial" or horizon="natural
        #                     if missing     horizon = "natural"
        #
        #
        #   Calculation analysis:
        #       dip:
        #                   if the observation is relative to a natural horizon:
        #                       dip = ( -0.97 * sqrt( height ) ) / 60
        #                   else:
        #                       dip = 0
        #       refraction:
        #                   refraction=(-0.00452*pressure) / (273+convert_to_celsius(temperature))/tangent(altitude)
        #       altitude:
        #                   altitude = observation + dip + refraction
        #                   round altitude to the nearest 0.1 arc-minute
        #                   convert altitude to a string having the format xdyy.y where
        #                           x:   degree portion of the altitude
        #                                integer                 -90<x<90
        #                                low bound               x=-89
        #                                high bound              x=89
        #                           d:   character
        #                           y.y: positive floating point    0.0<=y<60.0
        #                                low bound             y=0.0
        #                                high bound            y=59.9
        #                                formatted with two digits to the left of the decimal point
        #                                               one digit to the right
        #
        #    Sad path analysis:
        #        values     : if values = {'op': 'adjust'}:
        #                             return {'error':'mandatory information is missing'}
        #        observation: not in the form of xdy.y        observation="abc"
        #                     missing observation
        #                     x:      non-int x               x="abc"
        #                             out-of-bounds x         x=-1; x=90
        #                             missing x
        #                             -- add values['error'] = diagnostic string to the dictionary
        #                                return values
        #                     y:      non-floating point y    y="abc"
        #                             out-of-bounds x         y=-1; y=60
        #                             missing y
        #                             -- add values['error'] = diagnostic string to the dictionary
        #                                return values
        #        height:      out-of-bounds height            height=-1
        #                     non-int height                  height="a"
        #                     -- add values['error'] = diagnostic string to the dictionary
        #                                return values
        #        temperature: non-int temperature             temperature="ab"
        #                     out-of-bounds temperature       temperature=-21; temperature=121
        #                     -- add values['error'] = diagnostic string to the dictionary
        #                                return values
        #        pressure:    non-int pressure                pressure="a"
        #                     out-of-bounds pressure          pressure=99; pressure 1101
        #                     -- add values['error'] = diagnostic string to the dictionary
        #                                return values
        #        altitude:    already exists in input dict    return values['error'] = diagnostic string
        #

        # sad path
        # def test200_910ShouldReturnErrorIfMandatoryInformationIsMissing(self):
        #     values = {'op': 'adjust'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test200_920ShouldReturnErrorWhenObservationIsIncorrectFormat(self):
        #     values = {'observation': 'abc', 'height': '6', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust',
        #               'temperature': '71'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test200_930ShouldReturnErrorWhenDegreeInObservationGreaterThan90(self):
        #     values = {'observation': '101d15.2', 'height': '6', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust',
        #               'temperature': '71'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test200_940ShouldReturnErrorWhenDegreeInObservationLessThan0(self):
        #         values = {'observation': '-12d15.2', 'height': '6', 'pressure': '1010', 'horizon': 'natural',
        #                   'op': 'adjust',
        #                   'temperature': '71'}
        #         self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test200_950ShouldReturnErrorWhenHeightNotNumericalValue(self):
        #     values = {'observation': '89d15.2', 'height': 'a', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust',
        #               'temperature': '71'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test200_960ShouldReturnErrorWhenHeightLessThan0(self):
        #     values = {'observation': '89d15.2', 'height': '-1', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust',
        #               'temperature': '71'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test200_970ShouldReturnErrorWhenTempNotANumericalValue(self):
        #     values = {'observation': '89d15.2', 'height': '10', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust',
        #               'temperature': 'ab'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test200_980ShouldReturnErrorWhenTempLTMinus20(self):
        #     values = {'observation': '89d15.2', 'height': '10', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust',
        #               'temperature': '-21'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test200_990ShouldReturnErrorWhenTempGEMinus120(self):
        #     values = {'observation': '89d15.2', 'height': '10', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust',
        #               'temperature': '121'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test200_1000ShouldReturnErrorWhenPressureNotANumericalValue(self):
        #     values = {'observation': '89d15.2', 'height': '10', 'pressure': 'aa', 'horizon': 'natural', 'op': 'adjust',
        #               'temperature': '72'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test200_1010ShouldReturnErrorWhenPressureLT100(self):
        #     values = {'observation': '89d15.2', 'height': '10', 'pressure': '90', 'horizon': 'natural', 'op': 'adjust',
        #               'temperature': '72'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test200_1020ShouldReturnErrorWhenPressureGT1100(self):
        #     values = {'observation': '89d15.2', 'height': '10', 'pressure': '1120', 'horizon': 'natural', 'op': 'adjust',
        #               'temperature': '72'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test200_1030ShouldReturnErrorWhenHorizonNotArtificalNorNatural(self):
        #     values = {'observation': '89d15.2', 'height': '10', 'pressure': '1010', 'horizon': 'abc', 'op': 'adjust',
        #               'temperature': '72'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test200_1040ShouldReturnErrorWhenHorizonNotString(self):
        #     values = {'observation': '89d15.2', 'height': '10', 'pressure': '1010', 'horizon': '45', 'op': 'adjust',
        #               'temperature': '72'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test200_1050ShouldReturnErrorWhenAltitudeInInputDictionary(self):
        #     values = {'observation': '89d15.2', 'height': '10', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust',
        #               'temperature': '72', 'altitude':'29d59.9'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #

        # Happy Path
        # def test200_110ShouldCalculateAltitude(self):
        #     values = {'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
        #     expectedDictionary = {'altitude':'29d59.9', 'observation': '30d1.5', 'height': '19.0', 'pressure': '1000', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '85'}
        #     self.assertDictEqual(DP.dispatch(values), expectedDictionary)
        #
        # def test200_120ShouldCalculateAltitudeWithDefaultValue(self):
        #     values = {'observation': '42d0.0',  'op': 'adjust'}
        #     expectedDictionary = {'altitude':'41d59.0', 'observation': '42d0.0',  'op': 'adjust'}
        #     self.assertDictEqual(DP.dispatch(values), expectedDictionary)
        #
        # def test200_130ShouldCalculateAltitudeWithExtraKey(self):
        #     values = {'observation': '42d0.0',  'op': 'adjust', 'extraKey':'ignore'}
        #     expectedDictionary = {'altitude':'41d59.0', 'observation': '42d0.0',  'op': 'adjust', 'extraKey':'ignore'}
        #     self.assertDictEqual(DP.dispatch(values), expectedDictionary)

        # -----------------------------------------------------------------------
        # ---- Acceptance Tests
        # 300 operation {'op': 'predict'}
        #    Happy path analysis:
        #    body: name of the celestial body that has been sighted.
        #          mandatory string
        #    date: date of the observation
        #          optional string in yyyy-mm-dd format
        #                               yyyy is GE 2001
        #          if missing "2001-01-01"
        #    time: time of the sighting
        #          optional string in hh:mm:ss format
        #          if missing "00:00:00"
        #
        #     Sad path analysis:
        #       values     : if values = {'op': 'predict'}:
        #                       return {'error':'mandatory information is missing'}
        #       body       : if missing
        #                       -- add values['error'] = diagnostic string to the dictionary
        #                                return values
        #                    if value['body'] not match with the name of the navigable stars
        #                       -- add values['error'] = diagnostic string to the dictionary
        #                                return values
        #       date       : not string
        #                    not in the form of yyyy-mm-dd
        #                    year in date is LE 2001
        #                       --add values['error'] = diagnostic string to the dictionary
        #                                return values
        #       time       : not string
        #                    not in the form of hh:mm:ss
        #                       -- add values['error'] = diagnostic string to the dictionary
        #                                return values

        # Happy Path
        #
        # def test300_100ShouldReturnTheCorrectStarLatitudeValue(self):
        #     values = {'op': 'predict', 'body': 'Betelgeuse'}
        #     self.assertEqual(DP.dispatch(values)['lat'], '7d24.3')
        #
        # def test300_110ShouldPredictTheLocationWithoutDateAndTime(self):
        #     values = {'op': 'predict', 'body': 'Betelgeuse'}
        #     data = DP.dispatch(values).get('long').split('d')
        #     result = int(data[0]) + float(data[1])/60
        #     self.assertAlmostEquals(result, 11.695, delta=1.695)
        #
        # def test300_120ShouldPredictTheLocation(self):
        #     values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42'}
        #     data = DP.dispatch(values).get('long').split('d')
        #     result = int(data[0]) + float(data[1]) / 60
        #     self.assertAlmostEqual(result, 75.8933333333, delta=0.895)
        #
        # def test300_130ShouldPredictTheLocation(self):
        #     values = {'op': 'predict', 'body': 'Altair', 'date': '2016-01-17', 'time': '03:15:42'}
        #     self.assertAlmostEqual(DP.dispatch(values)['lat'],"8d54.8")
        #
        # def test300_140ShouldPredictTheLocation(self):
        #     values = {'op': 'predict', 'body': 'Altair', 'date': '2016-01-17', 'time': '03:15:42'}
        #     data = DP.dispatch(values).get('long').split('d')
        #     result = int(data[0]) + float(data[1]) / 60
        #     self.assertAlmostEqual(result, 227.023333333, delta=2.023333333)

        # Sad path
        # def test300_900ShouldReturnErrorIfMandatoryInformationIsMissing(self):
        #     values = {'op': 'predict'}
        #     expectedDictionary = {'error':'mandatory information is missing', 'op': 'predict'}
        #     self.assertDictEqual(DP.dispatch(values), expectedDictionary)

        # def test300_910ShouldReturnIfBodyIsNumeric(self):
        #     values = {'op': 'predict', 'body': 42}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test300_920ShouldReturnIfBodyIsInvalid(self):
        #     values = {'op': 'predict', 'body': 'unknown'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test300_930ShouldReturnErrorWhenDateHasIncorrectFormat(self):
        #     values = {'op': 'predict', 'body': 'Betelgeuse', 'date': 'aa', 'time': '03:15:42'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test300_940ShouldReturnErrorIfDateIsNumeric(self):
        #     values = {'op': 'predict', 'body': 'Betelgeuse', 'date': 42, 'time': '03:15:42'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test300_950ShouldReturnErrorWhenYearInDateIsInvalid(self):
        #     values = {'op': 'predict', 'body': 'Betelgeuse', 'date': 'aa-09-17', 'time': '03:15:42'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test300_960ShouldReturnErrorWhenYearIsLT2001(self):
        #     values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2000-09-17', 'time': '03:15:42'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test300_970ShouldReturnErrorWhenFebruaryHasLeapDayWhenItIsNotInLeapYear(self):
        #     values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-29', 'time': '03:15:42'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test300_980ShouldReturnErrorWhenMonthInDateIsInvalid(self):
        #     values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2001-aa-17', 'time': '03:15:42'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test300_990ShouldReturnErrorWhenMonthInDateIsGT12(self):
        #     values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-35-13', 'time': '03:15:42'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test300_1000ShouldReturnErrorWhenDayInDateIsInvalid(self):
        #     values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-08-aa', 'time': '03:15:42'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test300_1010ShouldReturnErrorWhenDayInDateIsGT31(self):
        #     values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-08-99', 'time': '03:15:42'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test300_1020ShouldReturnErrorForMonthsThatDoesNotHave31Days(self):
        #     values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-04-31', 'time': '03:15:42'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test300_1030ShouldReturnErrorWhenFebruaryHasMoreThan29Days(self):
        #     values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-30', 'time': '03:15:42'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test300_1040ShouldReturnErrorIfTimeHasIncorrectFormat(self):
        #     values = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': 'aa'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test300_1050ShouldReturnErrorIfTimeIsNumeric(self):
        #     values = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': 19}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test300_1060ShouldReturnErrorIfHourInTimeIsInvalid(self):
        #     values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': 'aa:15:34'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test300_1070ShouldReturnErrorIfHourInTimeGT24(self):
        #     values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '25:15:02'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test300_1080ShouldReturnErrorIfMinuteInTimeIsInvalid(self):
        #     values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '25:aa:02'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test300_1090ShouldReturnErrorIfMinuteInTimeIsGT59(self):
        #     values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '03:61:02'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test300_1100ShouldReturnErrorIfSecondInTimeIsInvalid(self):
        #     values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '03:15:aa'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test300_1110ShouldReturnErrorIfSecondInTimeIsGT59(self):
        #     values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '03:15:99'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test300_1120ShouldReturnErrorIfLatitudeIsInInputDictionary(self):
        #     values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '02:15:02', 'lat':'7d24.3'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)
        #
        # def test300_1130ShouldReturnErrorIfLongitudeIsInInputDictionary(self):
        #     values = {'op': 'predict', 'body': 'Betelgeuse', 'date': '2017-02-10', 'time': '02:15:02', 'long':'75d53.6'}
        #     self.assertEqual(DP.dispatch(values).has_key("error"), True)

    # -----------------------------------------------------------------------
    # ---- Acceptance Tests
    # 400 operation {'op': 'correct'}
    #    Happy path analysis:
    #    lat:       lat is the latitude at which the star is predicted to be in the zenith position
    #               this should be obtained from  {'op': 'predict'}
    #               mandatory string in xdyy.y format
    #                                           where  x    is integral number of degrees
    #                                                       GT -90 and LT 90
    #                                                 yy.y  portion of degree to 1/10 of an arc-minute
    #                                                       GE 0 and LT 60.0
    #                                                  d   is literal character that seperates degree from minutes
    #
    #    long:      angle of the star sighting that has been adjusted for atmospheric conditions
    #               this should be obtained from {'op': 'adjust'}
    #               mandatory string in xdyy.y format
    #                                           where x     is integral number of degrees
    #                                                       GE 0 and LT 360
    #                                                       yy.y  portion of degree to 1/10 of an arc-minute
    #                                                       d     is literal character that seperates degree from minutes
    #
    #   altitude:   angle of the star sighting that has been adjusted for atmospheric conditions
    #               this should be obtained from {'op': 'adjust'}
    #               mandatory string in xdyy.y format
    #                                           where x     is integral number of degrees
    #                                                       GT 0 and LT 90
    #                                                 yy.y  portion of degree to 1/10 of an arc-minute
    #                                                       GE 0 and LT 60
    #                                                 d     is literal character that seperates degree from minutes
    #
    #   assumedLat: estimated latitude of the navigator
    #               mandatory string in xdyy.y format
    #                                           where x     is integral number of degrees
    #                                                       GT -90 and LT 90
    #                                                 yy.y  portion of degree to 1/10 of an arc-minute
    #                                                       GE 0 and LT 60
    #                                                 d     is literal character that seperates degree from minutes
    #
    #   assumedLong: estimated longitude of the navigator
    #                mandatory string in xdyy.y format
    #                                           where x     is integral number of degrees
    #                                                       GE 0 and LT 360
    #                                                 yy.y  portion of degree to 1/10 of an arc-minute
    #                                                       GE 0 and LT 60
    #                                                 d     is literal character that separates degree from minutes
    #
    #     Sad path analysis:
    #       values     : if values = {'op': 'correct'}:
    #                       return {'error':'mandatory information is missing'}
    #       lat       :  if missing
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #                    if integer
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #                    if not in the correct format
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #                    if x <=-90 or x>=90
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #                    if y <0 or y>=60
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #
    #       long       : if missing
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #                    if integer
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #                    if not in the correct format
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #                    if x < 0 or x>=360
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #
    #      altitude:     if missing
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #                    if integer
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #                    if not in the correct format
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #                    if x <= 0 or x>=90
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #                    if y <0 or y>=60
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #    assumedLat:     if missing
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #                    if integer
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #                    if not in the correct format
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #                    if x <= -90 or x>=90
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #                    if y < 0 or y >= 60
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #   assumedLong:     if missing
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #                    if integer
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #                    if not in the correct format
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #                    if x < 0 or x >= 360
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values
    #                    if y < 0 or y >= 60
    #                       -- add values['error'] = diagnostic string to the dictionary
    #                                return values

    # Sad path
    def test400_900_ShouldReturnErrorIfMandatoryInformationIsMissing(self):
        values = {'op': 'correct'}
        #expectedDictionary = {'error': 'mandatory information is missing', 'op': 'correct'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_910_ShouldReturnErrorIfLatIsMissing(self):
        values = {'op': 'correct', 'long': '95d41.6', 'altitude': '13d42.3', 'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_920_ShouldReturnErrorIfLongIsMissing(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'altitude': '13d42.3', 'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_930_ShouldReturnErrorIfAltitudeIsMissing(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_940_ShouldReturnErrorIfAssumedLatIsMissing(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_950_ShouldReturnErrorIfAssumedLongIsMissing(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d42.3', 'assumedLat': '-53d38.4'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_960_ShouldReturnErrorIfLatIsInteger(self):
        values = {'op': 'correct', 'lat': 123, 'long': '95d41.6', 'altitude': '13d42.3', 'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_970_ShouldReturnErrorIfLatHasInvalidFormat(self):
        values = {'op': 'correct', 'lat': "value%20", 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_980_ShouldReturnErrorIfLatDegreeHasInvalidFormat(self):
        values = {'op': 'correct', 'lat': '16.0d32.3', 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_990_ShouldReturnErrorIfLatDegreeLTMinus90(self):
        values = {'op': 'correct', 'lat': '-91d32.3', 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1000_ShouldReturnErrorIfLatDegreeGT90(self):
        values = {'op': 'correct', 'lat': '91d32.3', 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1010_ShouldReturnErrorIfLatMinuteHasInvalidFormat(self):
        values = {'op': 'correct', 'lat': '16d2', 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1020_ShouldReturnErrorIfLatMinLT0(self):
        values = {'op': 'correct', 'lat': '16d-32.3', 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1030_ShouldReturnErrorIfLatMinGT60(self):
        values = {'op': 'correct', 'lat': '16d62.3', 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1040_ShouldReturnErrorIfLongIsInteger(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': 123, 'altitude': '13d42.3', 'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1050_ShouldReturnErrorIfLongHasIncorrectFormat(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': 'incorrect', 'altitude': '13d42.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1060_ShouldReturnErrorIfLongDegreeHasInvalidFormat(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95.0d41.6', 'altitude': '13d42.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1070_ShouldReturnErrorIfLongDegreeLT0(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '-95d41.6', 'altitude': '13d42.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1080_ShouldReturnErrorIfLongDegreeGT360(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '365d41.6', 'altitude': '13d42.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1090_ShouldReturnErrorIfLongMinuteHasInvalidFormat(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d4', 'altitude': '13d42.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1100_ShouldReturnErrorIfAltIsInteger(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': 136, 'assumedLat': '-53d38.4',
                  'assumedLong': ' 74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1110_ShouldReturnErrorIfAltHasInvalidFormat(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': 'unknown', 'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1120_ShouldReturnErrorIfAltDegreeHasInvalidFormat(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13.2d42.3',
                  'assumedLat': '-53d38.4', 'assumedLong': ' 74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1130_ShouldReturnErrorIfAltDegreeLT0(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '-13d42.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1140_ShouldReturnErrorIfAltDegreeGT90(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '91d42.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1150_ShouldReturnErrorIfAltMinuteHasInvalidFormat(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d2',
                  'assumedLat': '-53d38.4',
                  'assumedLong': ' 74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1160_ShouldReturnErrorIfAltMinLT0(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d-42.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1170_ShouldReturnErrorIfAltMinGT60(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d92.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1180_ShouldReturnErrorIfAssumedLatIsInteger(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d42.3', 'assumedLat': 435,
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1190_ShouldReturnErrorIfAssumedLatHasInvalidFormat(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLat': 'value%20',
                  'assumedLong': ' 74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1200_ShouldReturnErrorIfAssumedLatDegreeHasInvalidFormat(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLat': '53.2d38.4', 'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1210_ShouldReturnErrorIfAssumedLatDegreeLTMinus90(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLat': '-93d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1220_ShouldReturnErrorIfAssumedLatDegreeGT90(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLat': '93d38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1230_ShouldReturnErrorIfAssumedLatMinuteHasInvalidFormat(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLat': '-53d8',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1240_ShouldReturnErrorIfAssumedLatMinLT0(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLat': '-53d-38.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1250_ShouldReturnErrorIfAssumedLatMinGT60(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLat': '-53d88.4',
                  'assumedLong': '74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1260_ShouldReturnErrorIfAssumedLongIsInteger(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': 435}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1270_ShouldReturnErrorIfAssumedLongHasInvalidFormat(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLat': '-53d38.4', 'assumedLong': 'aaa'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1280_ShouldReturnErrorIfAssumedLongDegreeHasInvalidFormat(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': ' 74.1d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1290_ShouldReturnErrorIfAssumedLongDegreeLT0(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': '-74d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1300_ShouldReturnErrorIfAssumedLongDegreeGT360(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': '374d35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1310_ShouldReturnErrorIfAssumedLongMinuteHasInvalidFormat(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': '74d5'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1320_ShouldReturnErrorIfAssumedLongMinLT0(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': '74d-35.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1330_ShouldReturnErrorIfAssumedLongMinGT60(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d42.3',
                  'assumedLat': '-53d38.4',
                  'assumedLong': '74d65.3'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1340_ShouldReturnErrorIfCorrectedDistanceIsInInputDictionary(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d42.3', 'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3', 'correctedDistance': '3950'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    def test400_1350_ShouldReturnErrorIfCorrectedAzimuthIsInInputDictionary(self):
        values = {'op': 'correct', 'lat': '16d32.3', 'long': '95d41.6', 'altitude': '13d42.3', 'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3', 'correctedAzimuth': '164d42.9'}
        self.assertEqual(DP.dispatch(values).has_key("error"), True)

    # Happy Path
    def test400_100_ShouldCalculateTheResultForStarAldeberanInCorrectOperation(self):
        valuesForAdjustOp = {'observation': '13d51.6', 'height': '33.0', 'pressure': '1010', 'horizon': 'natural',
                             'op': 'adjust', 'temperature': '72'}
        altitude = DP.dispatch(valuesForAdjustOp)['altitude']

        valuesForPredictOp = {'op': 'predict', 'body': 'Aldebaran', 'date': '2016-01-17', 'time': '03:15:42'}
        predict = DP.dispatch(valuesForPredictOp)
        long = predict['long']
        lat = predict['lat']

        values = {'op': 'correct', 'lat': lat, 'long': long, 'altitude': altitude, 'assumedLat': '-53d38.4',
                  'assumedLong': '74d35.3'}
        result = DP.dispatch(values)

        correctedDistance = result.get('correctedDistance')
        self.assertAlmostEquals(float(correctedDistance), 3950, delta=197.5)

        data = result.get('correctedAzimuth').split('d')
        correctedAzimuth = int(data[0]) + float(data[1]) / 60
        self.assertAlmostEqual(float(correctedAzimuth), 164.715, delta=8.235750000000001)

    def test400_110_ShouldCalculateTheResultForStarPolarisInCorrectOperation(self):
        valuesForAdjustOp = {'observation': '37d21.7', 'height': '10.0', 'pressure': '1010', 'horizon': 'artificial',
                             'op': 'adjust', 'temperature': '65'}
        altitude = DP.dispatch(valuesForAdjustOp)['altitude']

        valuesForPredictOp = {'op': 'predict', 'body': 'Polaris', 'date': '2017-03-15', 'time': '01:42:10'}
        predict = DP.dispatch(valuesForPredictOp)
        long = predict.get('long')
        lat = predict.get('lat')

        values = {'op': 'correct', 'lat': lat, 'long': long, 'altitude': altitude, 'assumedLat': '35d59.7',
                  'assumedLong': '74d35.3'}
        result = DP.dispatch(values)

        correctedDistance = result.get('correctedDistance')
        self.assertAlmostEqual(float(correctedDistance), 104, delta=5.2)

        data = result.get('correctedAzimuth').split('d')
        correctedAzimuth = int(data[0]) + float(data[1]) / 60
        self.assertAlmostEqual(correctedAzimuth, 0.61333333333, delta=0.0306666666665)
