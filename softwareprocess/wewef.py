import math
import datetime
import time
import softwareprocess.prod.dispatch as DP

def dispatch(values=None,dip=None):


    #Validate parm
    if(values == None):
        return {'error': 'parameter is missing'}

    if(not(isinstance(values,dict))):
        return {'error': 'parameter is not a dictionary'}

    if (not('op' in values)):
        values['error'] = 'no op is specified'
        return values



    # if(values['op'] !=None and values['op'] != 'adjust'):
    #     return {'error': 'op is not a legal operation'}


    # if(not(values['altitude'] ==  None)):
    #     values['error'] = 'altitude is not None'
    #     return values




    #Perform designated function
    if(values['op'] == 'adjust'):

        if (not('observation' in values)):
            values={}
            values['error'] = 'mandatory information is missing'
            return values

        o = values['observation']
        fulldate = {}


        fulldate = o.split('d')
        try:
            ominutes = float(fulldate[1])
        except:
            values['error'] = 'observation is invalid'
            return values


        try:
            odegree= int(fulldate[0])
        except:
            values['error'] = 'observation is invalid'
            return values


        if  not (int(fulldate[0]) >= 0 and int(fulldate[0]) < 90):
            values['error'] = 'observation is invalid'
            # __not in 0~90
            return values

        try:
            minutes= float(ominutes)
        except ValueError:
            values['error'] = 'observation is invalid'
            return values

        # if not (isinstance(ominutes,float)):
        #     values['error'] = 'observation is invalid'
        #     # __not float
        #     return values
        if not (ominutes >= 0.0 and ominutes < 60.0):
            values['error'] = 'observation is invalid'
            # __not 0~60
            return values

        if (int(fulldate[0])==0 and ominutes<0.1):
            values['error'] = 'observation is invalid'
            # __o is LT 0.0.1
            return values

        if (not('height' in values)):
            h = 0.0
        else:
            h = values['height']



        # if (values['height'].isalpha() == True ):
        #     values['error'] = 'height is not invalid'
        #     # __not num
        #     return values
        try:
            htest= float(h)
        except ValueError:
            values['error'] = 'height is invalid'
            return values


        # if (not isinstance(float(h),float)):
        #     values['error'] = 'height is not invalid'
        #     # __not num
        #     return values


        if (not float(h) >= 0):
            values['error'] = 'height is invalid'
            # __not >= 0
            return values

        if (not('temperature' in values)):
            t = 72
        else:
            t =values['temperature']

        try:
            temptest= int(t)
        except ValueError:
            values['error'] = 'temperature is invalid'
            return values

        # if not isinstance(float(t),float):
        #     values['error'] = 'temperature is invalid'
        #     # __not number
        #     return values
        if not (int(t) >= -20 and int(t) <= 120):
            values['error'] = 'temperature is invalid'
            # __not -20~120
            return values

        tc = 5 * (float(t) - 32) / 9






        if (not('pressure' in values)):
            p = 1010
        else:
            try:
                temptest= int(values['pressure'])
            except ValueError:
                values['error'] = 'pressure is invalid'
                return values
            except KeyError:
                values['error'] = 'pressure is invalid'
                return values

            p =int(values['pressure'])

        # try:
        #     temptest= float(values['pressure'])
        # except ValueError:
        #     values['error'] = 'pressure is invalid'
        #     return values
        # except KeyError:
        #     values['error'] = 'pressure is invalid'
        #     return values

        # if not (isinstance(float(p),float)):
        #     values['error'] = 'pressure is invalid'
        #     # __not str of number
        #     return values

        if not (p >= 100 and p <= 1100):
            print  values['pressure']
            values['error'] = 'pressure is invalid'
            # __not 100~1100
            return values

        if (not('horizon' in values)):
            hr = 'natural'
        else:
            hr = values['horizon']

        # if (len(hr.replace(' ',' '))>0):
        #     values['error'] = 'horizon is invalid'
        #     return values

        if(not(hr == 'artificial')):
            if(not(hr == 'natural')):

 # values['error'] = 'horizon is not invalid__not  artificial or natural'
                values['error'] = 'horizon is invalid'
                return values

        # if not (isinstance(hr,str)):
        #     values['error'] = 'horizon is invalid'
        #     # __not str
        #     return values


        if (hr == 'natural'):
            dip = (-0.97 * math.sqrt( float(h) )) / 60

        else:
            dip = 0

        refraction=( -0.00452*int(p))/(273+tc)/math.tan(math.radians(ominutes/60+int(fulldate[0])))
        altitude0 = ominutes/60+int(fulldate[0]) + dip + refraction
        # tempalt = {}
        # tempalt = str(altitude0).split('.')
        D2 = int(altitude0)
        M2 = (altitude0 - D2)*60
        altitudedig = str(D2) + 'd' + str(round(M2,1))
        print altitudedig


        try:
            temptest= int(D2)
        except ValueError:
            values['error'] = 'altitude is invalid'
            return values

        # if not (isinstance(D2,int)):
        #     # values['error'] = 'altitude-degree is not invalid__not int'
        #     values['error'] = 'altitude-degree is not invalid'
        #     return values

        if  not (D2 > -90 and D2 < 90):
            # values['error'] = 'altitude-degree is not invalid__not in -90~90'
            values['error'] = 'altitude is invalid'
            return values

        try:
            temptest= float(M2)
        except ValueError:
            values['error'] = 'altitude is invalid'
            return values

        # if not (isinstance(round(M2,1),float)):
        #     # values['error'] = 'altitude-min is not invalid__not float'
        #     values['error'] = 'altitude-min is not invalid'
        #     return values

        if (not (M2 >= 0 and round(M2,1) < 60)):
            # values['error'] = 'altitude-min is not invalid__not 0~60'
            values['error'] = 'altitude is invalid'
            return values

        if ('altitude' in values):
            # values['error'] = 'altitude-already exist'
            values['error'] = 'altitude is not invalid'
            return values

        values['altitude'] = altitudedig

        # print altitudedig
        # print values












        return values    #<-------------- replace this with your implementation
    elif(values['op'] == 'predict'):

        if (not('body' in values)):
            values['error'] = 'mandatory information is missing'
            return values


        obody= values['body']
        try:
            lowerbody=obody.lower()

        except:
            values['error'] = 'mandatory information is missing'
            return values

        if(lowerbody == 'alpheratz'):
            SHAStar = '357d41.7'
            Dec =lattitude = '29d10.9'

        elif(lowerbody == 'ankaa'):
            SHAStar = '353d14.1'
            Dec =lattitude = '-42d13.4'

        elif(lowerbody == 'schedar'):
            SHAStar = '349d38.4'
            Dec =lattitude = '56d37.7'

        elif(lowerbody == 'diphda'):
            SHAStar = '348d54.1'
            Dec =lattitude = '-17d54.1'

        elif(lowerbody == 'achernar'):
            SHAStar = '335d25.5'
            Dec =lattitude = '-57d09.7'

        elif(lowerbody == 'hamal'):
            SHAStar = '327d58.7'
            Dec =lattitude = '23d32.3'

        elif(lowerbody == 'polaris'):
            SHAStar = '316d41.3'
            Dec =lattitude = '89d20.1'

        elif(lowerbody == 'akamar'):
            SHAStar = '315d16.8'
            Dec =lattitude = '-40d14.8'

        elif(lowerbody == 'menkar'):
            SHAStar = '314d13.0'
            Dec =lattitude = '4d09.0'

        elif(lowerbody == 'mirfak'):
            SHAStar = '308d37.4'
            Dec =lattitude = '49d55.1'

        elif(lowerbody == 'aldebaran'):
            SHAStar = '290d47.1'
            Dec =lattitude = '16d32.3'

        elif(lowerbody == 'rigel'):
            SHAStar = '281d10.1'
            Dec =lattitude = '-8d11.3'

        elif(lowerbody == 'capella'):
            SHAStar = '280d31.4'
            Dec =lattitude = '46d00.7'

        elif(lowerbody == 'bellatrix'):
            SHAStar = '278d29.8'
            Dec =lattitude = '6d21.6'

        elif(lowerbody == 'elnath'):
            SHAStar = '278d10.1'
            Dec =lattitude = '28d37.1'

        elif(lowerbody == 'alnilam'):
            SHAStar = '275d44.3'
            Dec =lattitude = '-1d11.8'

        elif(lowerbody == 'betelgeuse'):
            SHAStar = '270d59.1'
            Dec =lattitude = '7d24.3'

        elif(lowerbody == 'canopus'):
            SHAStar = '263d54.8'
            Dec =lattitude = '-52d42.5'

        elif(lowerbody == 'sirius'):
            SHAStar = '258d31.7'
            Dec =lattitude = '-16d44.3'

        elif(lowerbody == 'adara'):
            SHAStar = '255d10.8'
            Dec =lattitude = '-28d59.9'

        elif(lowerbody == 'procyon'):
            SHAStar = '244d57.5'
            Dec =lattitude = '5d10.9'

        elif(lowerbody == 'pollux'):
            SHAStar = '243d25.2'
            Dec =lattitude = '27d59.0'

        elif(lowerbody == 'avior'):
            SHAStar = '234d16.6'
            Dec =lattitude = '-59d33.7'

        elif(lowerbody == 'suhail'):
            SHAStar = '222d50.7'
            Dec =lattitude = '-43d29.8'

        elif(lowerbody == 'miaplacidus'):
            SHAStar = '221d38.4'
            Dec =lattitude = '-69d46.9'

        elif(lowerbody == 'alphard'):
            SHAStar = '217d54.1'
            Dec =lattitude = '-8d43.8'

        elif(lowerbody == 'regulus'):
            SHAStar = '207d41.4'
            Dec =lattitude = '11d53.2'

        elif(lowerbody == 'dubhe'):
            SHAStar = '193d49.4'
            Dec =lattitude = '61d39.5'

        elif(lowerbody == 'denebola'):
            SHAStar = '182d31.8'
            Dec =lattitude = '14d28.9'

        elif(lowerbody == 'gienah'):
            SHAStar = '175d50.4'
            Dec =lattitude = '-17d37.7'

        elif(lowerbody == 'acrux'):
            SHAStar = '173d07.2'
            Dec =lattitude = '-63d10.9'

        elif(lowerbody == 'gacrux'):
            SHAStar = '171d58.8'
            Dec =lattitude = '-57d11.9'

        elif(lowerbody == 'alioth'):
            SHAStar = '166d19.4'
            Dec =lattitude = '55d52.1'

        elif(lowerbody == 'spica'):
            SHAStar = '158d29.5'
            Dec =lattitude = '-11d14.5'

        elif(lowerbody == 'alcaid'):
            SHAStar = '152d57.8'
            Dec =lattitude = '49d13.8'

        elif(lowerbody == 'hadar'):
            SHAStar = '148d45.5'
            Dec =lattitude = '-60d26.6'

        elif(lowerbody == 'menkent'):
            SHAStar = '148d05.6'
            Dec =lattitude = '-36d26.6'

        elif(lowerbody == 'arcturus'):
            SHAStar = '145d54.2'
            Dec =lattitude = '19d06.2'

        elif(lowerbody == 'rigil Kent.'):
            SHAStar = '139d49.6'
            Dec =lattitude = '-60d53.6'

        elif(lowerbody == 'zubenelg.'):
            SHAStar = '137d03.7'
            Dec =lattitude = '-16d06.3'

        elif(lowerbody == 'kochab'):
            SHAStar = '137d21.0'
            Dec =lattitude = '74d05.2'

        elif(lowerbody == 'alphecca'):
            SHAStar = '126d09.9'
            Dec =lattitude = '26d39.7'

        elif(lowerbody == 'antares'):
            SHAStar = '112d24.4'
            Dec =lattitude = '-26d27.8'

        elif(lowerbody == 'atria'):
            SHAStar = '107d25.2'
            Dec =lattitude = '-69d03.0'

        elif(lowerbody == 'sabik'):
            SHAStar = '102d10.9'
            Dec =lattitude = '-15d44.4'

        elif(lowerbody == 'shaula'):
            SHAStar = '96d20.0'
            Dec =lattitude = '-37d06.'

        elif(lowerbody == 'rasalhague'):
            SHAStar = '96d05.2'
            Dec =lattitude = '12d33.1'

        elif(lowerbody == 'etamin'):
            SHAStar = '90d45.9'
            Dec =lattitude = '51d29.3'

        elif(lowerbody == 'kaus aust.'):
            SHAStar = '83d41.9'
            Dec =lattitude = '-34d22.4'

        elif(lowerbody == 'vega'):
            SHAStar = '80d38.2'
            Dec =lattitude = '38d48.1'

        elif(lowerbody == 'nunki'):
            SHAStar = '75d56.6'
            Dec =lattitude = '-26d16.4'

        elif(lowerbody == 'altair'):
            SHAStar = '62d06.9'
            Dec =lattitude = '8d54.8'

        elif(lowerbody == 'peacock'):
            SHAStar = '53d17.2'
            Dec =lattitude = '-56d41.0'

        elif(lowerbody == 'deneb'):
            SHAStar = '49d30.7'
            Dec =lattitude = '45d20.5'

        elif(lowerbody == 'enif'):
            SHAStar = '33d45.7'
            Dec =lattitude = '9d57.0'

        elif(lowerbody == 'alnair'):
            SHAStar = '27d42.0'
            Dec =lattitude = '-46d53.1'

        elif(lowerbody == 'fomalhaut'):
            SHAStar = '15d22.4'
            Dec =lattitude = '-29d32.3'

        elif(lowerbody == 'scheat'):
            SHAStar = '13d51.8'
            Dec =lattitude = '28d10.3'

        elif(lowerbody == 'markab'):
            SHAStar = '13d36.7'
            Dec =lattitude = '15d17.6'




        else:
            values['error'] = 'star not in catalog'
            return values

        if (not('date' in values)):

            values['date'] = '2001-01-01'



        obsdate = values['date']

        try:
            if "-" in obsdate:
                fulldate = time.strptime(obsdate, "%Y-%m-%d")

        except:

            values['error'] = 'invalid time'
            return values

        #
        # try:
        #     fulldate = obsdate.split('-')
        #
        # except:
        #     values['error'] = 'invalid time'
        #     return values

        try:
            Obs_Year = int(fulldate[0])
        except:
            values['error'] = 'invalid time'
            return values

        try:
            obs_month = int(fulldate[1])
        except:
            values['error'] = 'DateMooth is invalid'
            return values

        try:
            obs_day = int(fulldate[2])
        except:
            values['error'] = 'obs_day is invalid'
            return values


        if  not (2001 <=Obs_Year):
            values['error'] = 'Obs_Year is invalid1'
            # __not in 0~90
            return values


        if  not (obs_month >= 1 and obs_month <= 12):
            values['error'] = 'Obs_Year is invalid2'
            # __not in 0~90
            return values

        bigmonth ={1,3,5,7,8,10,12}
        smallmonth = {4,6,9,11}

        if (obs_month in bigmonth):
            if  not (obs_day >= 1 and obs_day <= 31):
                values['error'] = 'obs_day is invalid'
            # __not in 0~90
                return values

        if (obs_month in smallmonth):
            if  not (obs_day >= 1 and obs_day <= 30):
                values['error'] = 'obs_day is invalid'
            # __not in 0~90
                return values

        if (Obs_Year % 4 == 0):
            if  not (obs_day >= 1 and obs_day <= 29):
                values['error'] = 'obs_day is invalid'
            # __not in 0~90
                return values
        if (Obs_Year % 4 != 0):
            if  not (obs_day >= 1 and obs_day <= 28):
                values['error'] = 'obs_day is invalid'
            # __not in 0~90
                return values


        if (not('time' in values)):

            values['time'] = '00:00:00'

        obstime = values['time']

        # if ":" not in obstime:
        #     values['error'] = 'invalid time'
        #     return values

        try:
            if ":" not in obstime:
                values['error'] = 'invalid time'
                return values

        except:

            values['error'] = 'invalid time'
            return values

        try:
            if ":" in obstime:
                obstimedictionary = time.strptime(obstime, "%H:%M:%S")

        except:

            values['error'] = 'invalid time'
            return values



        GHAAries20010101 = '100d42.6'
        differrence = Obs_Year - 2001
        GHAAriesDecreases='-0d14.31667'

        CumulativeProgresNum=differrence*(-14.31667/60.0)
        CPint=int(CumulativeProgresNum)
        CPSmallnum=round(((CumulativeProgresNum-CPint)*60.0),1)
        CumulativeProgresStr=str(CPint)+ 'd' + str(abs(CPSmallnum))

        # print CumulativeProgresStr

        LYNum= int((differrence+1)/4 -1)
        # print LYNum
        AmountOfDailyRoataAbs=float(0.983)
        # print AmountOfDailyRoataAbs
        TotalProgressionNum=AmountOfDailyRoataAbs * LYNum
        # print TotalProgressionNum
        TotalProgressionNumInt=int(TotalProgressionNum)
        TotalProgressionNumSmallNum=round((TotalProgressionNum-TotalProgressionNumInt)*60,1)
        TotalProgressionStr=str(TotalProgressionNumInt)+'D'+str(abs(TotalProgressionNumSmallNum))
        # print TotalProgressionStr


        GHAAries20010101Numlist = GHAAries20010101.split('d')
        # print GHAAries20010101Numlist
        GHAAries20010101Int=int(GHAAries20010101Numlist[0])
        GHAAries20010101SmallNum=round(float(GHAAries20010101Numlist[1])/60.0,1)

        GHAAries20010101Numliststr=str(GHAAries20010101Int)+ 'd'+ str(GHAAries20010101Numlist[1])
        # print GHAAries20010101Numliststr


        GHAAriesObsY0101Num=GHAAries20010101Int+float(GHAAries20010101Numlist[1])/60.0+round(CumulativeProgresNum,3)+TotalProgressionNumInt+TotalProgressionNumSmallNum/60.0
        GHAAriesObsY0101NumInt=int(GHAAriesObsY0101Num)
        GHAAriesObsY0101SmallNum=GHAAriesObsY0101Num-GHAAries20010101Int

        GHAAriesObsY0101NumStr=str(GHAAries20010101Int)+'d'+str(abs(round(GHAAriesObsY0101SmallNum*60,1)))



        # print GHAAries20010101Int
        # print float(GHAAries20010101Numlist[1])/60.0
        #
        #
        # print round(CumulativeProgresNum,3)
        #
        #
        # print TotalProgressionNumInt
        # print TotalProgressionNumSmallNum/60.0
        #
        # print GHAAriesObsY0101Num
        # print GHAAriesObsY0101NumStr


        # print values
        # print fulldate
        # print obstimedictionary
        # print fulldate[1]
        # print obstimedictionary[0]

        CalDate1=datetime.datetime(Obs_Year,01,01,00,00,00)
        # DateAndtime=fulldate
        # DateAndtime.expand(obstimedictionary)
        CalDate2=datetime.datetime(fulldate[0],fulldate[1],fulldate[2],obstimedictionary[3],obstimedictionary[4],obstimedictionary[5])

        # print CalDate1
        # print CalDate2

        NumberOfSecondsBetweenObsYear=(CalDate2-CalDate1).total_seconds()

        # print NumberOfSecondsBetweenObsYear

        AmountOfRotationNum=NumberOfSecondsBetweenObsYear/86164.1*360
        AmountOfRotationNumInt=int(AmountOfRotationNum)
        AmountOfRotationNumSmallNum=(AmountOfRotationNum-AmountOfRotationNumInt)*60
        AmountOfRotationNumStr=str(AmountOfRotationNumInt%360)+'d'+str(round(AmountOfRotationNumSmallNum,1))

        print AmountOfRotationNumStr
        GHAAriesObsYAndDAndHNumRad=GHAAriesObsY0101NumInt+GHAAriesObsY0101SmallNum+AmountOfRotationNumInt%360+AmountOfRotationNum-AmountOfRotationNumInt

        print GHAAriesObsY0101NumInt
        print GHAAriesObsY0101SmallNum
        print AmountOfRotationNumInt%360
        print AmountOfRotationNum-AmountOfRotationNumInt

        print GHAAriesObsYAndDAndHNumRad
        # C.  Calculate the star's GHA

        SHAStarNumList=SHAStar.split('d')

        GHAStarNum=GHAAriesObsYAndDAndHNumRad+float(SHAStarNumList[0])+float(SHAStarNumList[1])/60




        GHAStarNumInt=int(GHAStarNum)%360
        GHAStarSmallNum=round((GHAStarNum-int(GHAStarNum))*60,1)
        GHAStarStr=str(GHAStarNumInt)+'d'+str(GHAStarSmallNum)


        if ('long' in values):
            values['error'] = 'long in values'
            return values

        if ('lat' in values):
            values['error'] = 'lat in values'
            return values

        values['long']= GHAStarStr
        values['lat']= lattitude





        return values    #This calculation is stubbed out
    elif(values['op'] == 'correct'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'locate'):
        return values    #This calculation is stubbed out
    else:
        values = {}
        values['error'] = 'op is not a legal operation'
        return values




values = {'op': 'predict', 'body': 'Betelgeuse'}
data = DP.dispatch(values).get('long').split('d')
result = int(data[0]) + float(data[1])/60


# values={'observation': '10d00.0', 'height': '6.0','pressure': '1010', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '72'}
# print dispatch(values)
        # values={'observation': '10d00.0', 'height': '6.0', 'pressure': '1010', 'horizon': 'artificial', 'op': 'adjust', 'temperature': '72'}
# values={'observation': '45d15.2', 'height': '6', 'pressure': '1010', 'horizon': 'natural', 'op': 'adjust', 'temperature': '71'}
# print values['altitude']
print dispatch(values)
