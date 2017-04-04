import math
import datetime
import time


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
            values={}
            values['error'] = 'mandatory information is missing'
            return values

        elif(values['body'] == 'Alpheratz'):
            SHAStar = '357d41.7'
            Dec =lattitude = '29d10.9'

        elif(values['body'] == 'Ankaa'):
            SHAStar = '353d14.1'
            Dec =lattitude = '-42d13.4'

        elif(values['body'] == 'Schedar'):
            SHAStar = '349d38.4'
            Dec =lattitude = '56d37.7'

        elif(values['body'] == 'Diphda'):
            SHAStar = '348d54.1'
            Dec =lattitude = '-17d54.1'

        elif(values['body'] == 'Achernar'):
            SHAStar = '335d25.5'
            Dec =lattitude = '-57d09.7'

        elif(values['body'] == 'Hamal'):
            SHAStar = '327d58.7'
            Dec =lattitude = '23d32.3'

        elif(values['body'] == 'Polaris'):
            SHAStar = '316d41.3'
            Dec =lattitude = '89d20.1'

        elif(values['body'] == 'Akamar'):
            SHAStar = '315d16.8'
            Dec =lattitude = '-40d14.8'

        elif(values['body'] == 'Menkar'):
            SHAStar = '314d13.0'
            Dec =lattitude = '4d09.0'

        elif(values['body'] == 'Mirfak'):
            SHAStar = '308d37.4'
            Dec =lattitude = '49d55.1'

        elif(values['body'] == 'Aldebaran'):
            SHAStar = '290d47.1'
            Dec =lattitude = '16d32.3'

        elif(values['body'] == 'Rigel'):
            SHAStar = '281d10.1'
            Dec =lattitude = '-8d11.3'

        elif(values['body'] == 'Capella'):
            SHAStar = '280d31.4'
            Dec =lattitude = '46d00.7'

        elif(values['body'] == 'Bellatrix'):
            SHAStar = '278d29.8'
            Dec =lattitude = '6d21.6'

        elif(values['body'] == 'Elnath'):
            SHAStar = '278d10.1'
            Dec =lattitude = '28d37.1'

        elif(values['body'] == 'Alnilam'):
            SHAStar = '275d44.3'
            Dec =lattitude = '-1d11.8'

        elif(values['body'] == 'Betelgeuse'):
            SHAStar = '270d59.1'
            Dec =lattitude = '7d24.3'

        elif(values['body'] == 'Canopus'):
            SHAStar = '263d54.8'
            Dec =lattitude = '-52d42.5'

        elif(values['body'] == 'Sirius'):
            SHAStar = '258d31.7'
            Dec =lattitude = '-16d44.3'

        elif(values['body'] == 'Adara'):
            SHAStar = '255d10.8'
            Dec =lattitude = '-28d59.9'

        elif(values['body'] == 'Procyon'):
            SHAStar = '244d57.5'
            Dec =lattitude = '5d10.9'

        elif(values['body'] == 'Pollux'):
            SHAStar = '243d25.2'
            Dec =lattitude = '27d59.0'

        elif(values['body'] == 'Avior'):
            SHAStar = '234d16.6'
            Dec =lattitude = '-59d33.7'

        elif(values['body'] == 'Suhail'):
            SHAStar = '222d50.7'
            Dec =lattitude = '-43d29.8'

        elif(values['body'] == 'Miaplacidus'):
            SHAStar = '221d38.4'
            Dec =lattitude = '-69d46.9'

        elif(values['body'] == 'Alphard'):
            SHAStar = '217d54.1'
            Dec =lattitude = '-8d43.8'

        elif(values['body'] == 'Regulus'):
            SHAStar = '207d41.4'
            Dec =lattitude = '11d53.2'

        elif(values['body'] == 'Dubhe'):
            SHAStar = '193d49.4'
            Dec =lattitude = '61d39.5'

        elif(values['body'] == 'Denebola'):
            SHAStar = '182d31.8'
            Dec =lattitude = '14d28.9'

        elif(values['body'] == 'Gienah'):
            SHAStar = '175d50.4'
            Dec =lattitude = '-17d37.7'

        elif(values['body'] == 'Acrux'):
            SHAStar = '173d07.2'
            Dec =lattitude = '-63d10.9'

        elif(values['body'] == 'Gacrux'):
            SHAStar = '171d58.8'
            Dec =lattitude = '-57d11.9'

        elif(values['body'] == 'Alioth'):
            SHAStar = '166d19.4'
            Dec =lattitude = '55d52.1'

        elif(values['body'] == 'Spica'):
            SHAStar = '158d29.5'
            Dec =lattitude = '-11d14.5'

        elif(values['body'] == 'Alcaid'):
            SHAStar = '152d57.8'
            Dec =lattitude = '49d13.8'

        elif(values['body'] == 'Hadar'):
            SHAStar = '148d45.5'
            Dec =lattitude = '-60d26.6'

        elif(values['body'] == 'Menkent'):
            SHAStar = '148d05.6'
            Dec =lattitude = '-36d26.6'

        elif(values['body'] == 'Arcturus'):
            SHAStar = '145d54.2'
            Dec =lattitude = '19d06.2'

        elif(values['body'] == 'Rigil Kent.'):
            SHAStar = '139d49.6'
            Dec =lattitude = '-60d53.6'

        elif(values['body'] == 'Zubenelg.'):
            SHAStar = '137d03.7'
            Dec =lattitude = '-16d06.3'

        elif(values['body'] == 'Kochab'):
            SHAStar = '137d21.0'
            Dec =lattitude = '74d05.2'

        elif(values['body'] == 'Alphecca'):
            SHAStar = '126d09.9'
            Dec =lattitude = '26d39.7'

        elif(values['body'] == 'Antares'):
            SHAStar = '112d24.4'
            Dec =lattitude = '-26d27.8'

        elif(values['body'] == 'Atria'):
            SHAStar = '107d25.2'
            Dec =lattitude = '-69d03.0'

        elif(values['body'] == 'Sabik'):
            SHAStar = '102d10.9'
            Dec =lattitude = '-15d44.4'

        elif(values['body'] == 'Shaula'):
            SHAStar = '96d20.0'
            Dec =lattitude = '-37d06.'

        elif(values['body'] == 'Rasalhague'):
            SHAStar = '96d05.2'
            Dec =lattitude = '12d33.1'

        elif(values['body'] == 'Etamin'):
            SHAStar = '90d45.9'
            Dec =lattitude = '51d29.3'

        elif(values['body'] == 'Kaus Aust.'):
            SHAStar = '83d41.9'
            Dec =lattitude = '-34d22.4'

        elif(values['body'] == 'Vega'):
            SHAStar = '80d38.2'
            Dec =lattitude = '38d48.1'

        elif(values['body'] == 'Nunki'):
            SHAStar = '75d56.6'
            Dec =lattitude = '-26d16.4'

        elif(values['body'] == 'Altair'):
            SHAStar = '62d06.9'
            Dec =lattitude = '8d54.8'

        elif(values['body'] == 'Peacock'):
            SHAStar = '53d17.2'
            Dec =lattitude = '-56d41.0'

        elif(values['body'] == 'Deneb'):
            SHAStar = '49d30.7'
            Dec =lattitude = '45d20.5'

        elif(values['body'] == 'Enif'):
            SHAStar = '33d45.7'
            Dec =lattitude = '9d57.0'

        elif(values['body'] == 'Alnair'):
            SHAStar = '27d42.0'
            Dec =lattitude = '-46d53.1'

        elif(values['body'] == 'Fomalhaut'):
            SHAStar = '15d22.4'
            Dec =lattitude = '-29d32.3'

        elif(values['body'] == 'Scheat'):
            SHAStar = '13d51.8'
            Dec =lattitude = '28d10.3'

        elif(values['body'] == 'Markab'):
            SHAStar = '13d36.7'
            Dec =lattitude = '15d17.6'




        else:
            values['error'] = 'mandatory information is missing'
            return values

        if (not('date' in values)):

            values['date'] = '2001-01-01'



        obsdate = values['date']

        try:
            if "-" in obsdate:
                fulldate = obsdate.strptime(obsdate, "%Y-%m-%d")

        except:

            values['error'] = 'fulltime is invalid'
            return values

        #
        # try:
        #     fulldate = date.split('-')
        #
        # except:
        #     values['error'] = 'fulldate is invalid'
        #     return values

        try:
            Obs_Year = int(fulldate[0])
        except:
            values['error'] = 'Obs_Year is invalid'
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


        if  not (Obs_Year >= 2001 and Obs_Year <= 2016):
            values['error'] = 'Obs_Year is invalid'
            # __not in 0~90
            return values


        if  not (obs_month >= 1 and Obs_Year <= 12):
            values['error'] = 'Obs_Year is invalid'
            # __not in 0~90
            return values

        bigmonth ={1,3,5,7,8,10,12}
        smallmonth = {4,6,9,11}

        if (obs_month in bigmonth):
            if  not (obs_day >= 1 and Obs_Year <= 31):
                values['error'] = 'Obs_Year is invalid'
            # __not in 0~90
                return values

        if (obs_month in smallmonth):
            if  not (obs_day >= 1 and Obs_Year <= 30):
                values['error'] = 'Obs_Year is invalid'
            # __not in 0~90
                return values

        if (Obs_Year % 4 == 0):
            if  not (obs_day >= 1 and Obs_Year <= 29):
                values['error'] = 'Obs_Year is invalid'
            # __not in 0~90
                return values
        if (Obs_Year % 4 != 0):
            if  not (obs_day >= 1 and Obs_Year <= 28):
                values['error'] = 'Obs_Year is invalid'
            # __not in 0~90
                return values


        if (not('time' in values)):

            values['time'] = '00:00:00'

        obstime = values['time']

        try:
            if ":" in obstime:
                obstimedictionary = time.strptime(obstime, "%H:%M:%S")

        except:

            values['error'] = 'fulldate is invalid'
            return values



        GHAAries20010101 = '100d42.6'
        differrence = Obs_Year - 2001
        GHAAriesDecreases='-0d14.31667'

        CumulativeProgresNum=differrence*(-14.31667/60)
        CPint=int(CumulativeProgresNum)
        CPSmallnum=(CumulativeProgresNum-CPint)*60
        CumulativeProgresStr=str(CPint)+ 'd' + str(round(CPSmallnum,1))

        LYNum= int((differrence+1)/4)

        AmountOfDailyRoataAbs=0.59/60
        TotalProgressionNum=AmountOfDailyRoataAbs * LYNum
        TotalProgressionNumInt=int(TotalProgressionNum)
        TotalProgressionNumSmallNum=(TotalProgressionNum-TotalProgressionNumInt)*60
        TotalProgressionStr=str(TotalProgressionNumInt)+'D'+str(TotalProgressionNumSmallNum)

        GHAAries20010101Numlist = GHAAries20010101.split('d')
        GHAAries20010101Int=GHAAries20010101Numlist[0]
        GHAAries20010101SmallNum=float(GHAAries20010101Numlist[1])/60



        GHAAriesObsY0101Num=GHAAries20010101Int+round(GHAAries20010101SmallNum,1)+CPint+round(CPSmallnum,1)+TotalProgressionNumInt+round(TotalProgressionNumSmallNum,1)
        GHAAriesObsY0101NumInt=int(GHAAriesObsY0101Num)
        GHAAriesObsY0101SmallNum=GHAAriesObsY0101Num-GHAAries20010101Int
        GHAAriesObsY0101NumStr=str(GHAAries20010101Int)+'d'+str(round(GHAAriesObsY0101SmallNum),1)

        CalDate1=datetime.datetime(Obs_Year,01,01,00,00,00)
        CalDate2=datetime.datetime(fulldate,obstimedictionary)

        NumberOfSecondsBetweenObsYear=(CalDate1-CalDate2).seconds
        AmountOfRotationNum=NumberOfSecondsBetweenObsYear/81164.1*360
        AmountOfRotationNumInt=int(AmountOfRotationNum)
        AmountOfRotationNumSmallNum=(AmountOfRotationNum-AmountOfRotationNumInt)*60
        AmountOfRotationNumStr=str(AmountOfRotationNumInt)+'d'+str(AmountOfRotationNumSmallNum)

        GHAAriesObsYAndDAndHNum=GHAAriesObsY0101Num+AmountOfRotationNum

        # C
        



        return values    #This calculation is stubbed out
    elif(values['op'] == 'correct'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'locate'):
        return values    #This calculation is stubbed out
    else:
        values = {}
        values['error'] = 'op is not a legal operation'
        return values

