import math
import sys


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
        list1 = {}


        list1 = o.split('d')
        try:
            ominutes = float(list1[1])
        except IndexError:
            values['error'] = 'observation is invalid'
            return values


        try:
            odegree= int(list1[0])
        except ValueError:
            values['error'] = 'observation is invalid'
            return values


        if  not (int(list1[0]) >= 0 and int(list1[0]) < 90):
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

        if (int(list1[0])==0 and ominutes<0.1):
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




        refraction=( -0.00452*int(p))/(273+tc)/math.tan(math.radians(ominutes/60+int(list1[0])))
        altitude0 = ominutes/60+int(list1[0]) + dip + refraction
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
            SHA = '357d41.7'
            Dec = '29d10.9'

        elif(values['body'] == 'Ankaa'):
            SHA = '353d14.1'
            Dec = '-42d13.4'

        elif(values['body'] == 'Schedar'):
            SHA = '349d38.4'
            Dec = '56d37.7'

        elif(values['body'] == 'Diphda'):
            SHA = '348d54.1'
            Dec = '-17d54.1'

        elif(values['body'] == 'Achernar'):
            SHA = '335d25.5'
            Dec = '-57d09.7'

        elif(values['body'] == 'Hamal'):
            SHA = '327d58.7'
            Dec = '23d32.3'

        elif(values['body'] == 'Polaris'):
            SHA = '316d41.3'
            Dec = '89d20.1'

        elif(values['body'] == 'Akamar'):
            SHA = '315d16.8'
            Dec = '-40d14.8'

        elif(values['body'] == 'Menkar'):
            SHA = '314d13.0'
            Dec = '4d09.0'

        elif(values['body'] == 'Mirfak'):
            SHA = '308d37.4'
            Dec = '49d55.1'

        elif(values['body'] == 'Aldebaran'):
            SHA = '290d47.1'
            Dec = '16d32.3'

        elif(values['body'] == 'Rigel'):
            SHA = '281d10.1'
            Dec = '-8d11.3'

        elif(values['body'] == 'Capella'):
            SHA = '280d31.4'
            Dec = '46d00.7'

        elif(values['body'] == 'Bellatrix'):
            SHA = '278d29.8'
            Dec = '6d21.6'

        elif(values['body'] == 'Elnath'):
            SHA = '278d10.1'
            Dec = '28d37.1'

        elif(values['body'] == 'Alnilam'):
            SHA = '275d44.3'
            Dec = '-1d11.8'

        elif(values['body'] == 'Betelgeuse'):
            SHA = '270d59.1'
            Dec = '7d24.3'

        elif(values['body'] == 'Canopus'):
            SHA = '263d54.8'
            Dec = '-52d42.5'

        elif(values['body'] == 'Sirius'):
            SHA = '258d31.7'
            Dec = '-16d44.3'

        elif(values['body'] == 'Adara'):
            SHA = '255d10.8'
            Dec = '-28d59.9'

        elif(values['body'] == 'Procyon'):
            SHA = '244d57.5'
            Dec = '5d10.9'

        elif(values['body'] == 'Pollux'):
            SHA = '243d25.2'
            Dec = '27d59.0'

        elif(values['body'] == 'Avior'):
            SHA = '234d16.6'
            Dec = '-59d33.7'

        elif(values['body'] == 'Suhail'):
            SHA = '222d50.7'
            Dec = '-43d29.8'

        elif(values['body'] == 'Miaplacidus'):
            SHA = '221d38.4'
            Dec = '-69d46.9'

        elif(values['body'] == 'Alphard'):
            SHA = '217d54.1'
            Dec = '-8d43.8'

        elif(values['body'] == 'Regulus'):
            SHA = '207d41.4'
            Dec = '11d53.2'

        elif(values['body'] == 'Dubhe'):
            SHA = '193d49.4'
            Dec = '61d39.5'

        elif(values['body'] == 'Denebola'):
            SHA = '182d31.8'
            Dec = '14d28.9'

        elif(values['body'] == 'Gienah'):
            SHA = '175d50.4'
            Dec = '-17d37.7'

        elif(values['body'] == 'Acrux'):
            SHA = '173d07.2'
            Dec = '-63d10.9'

        elif(values['body'] == 'Gacrux'):
            SHA = '171d58.8'
            Dec = '-57d11.9'

        elif(values['body'] == 'Alioth'):
            SHA = '166d19.4'
            Dec = '55d52.1'

        elif(values['body'] == 'Spica'):
            SHA = '158d29.5'
            Dec = '-11d14.5'

        elif(values['body'] == 'Alcaid'):
            SHA = '152d57.8'
            Dec = '49d13.8'

        elif(values['body'] == 'Hadar'):
            SHA = '148d45.5'
            Dec = '-60d26.6'

        elif(values['body'] == 'Menkent'):
            SHA = '148d05.6'
            Dec = '-36d26.6'

        elif(values['body'] == 'Arcturus'):
            SHA = '145d54.2'
            Dec = '19d06.2'

        elif(values['body'] == 'Rigil Kent.'):
            SHA = '139d49.6'
            Dec = '-60d53.6'

        elif(values['body'] == 'Zubenelg.'):
            SHA = '137d03.7'
            Dec = '-16d06.3'

        elif(values['body'] == 'Kochab'):
            SHA = '137d21.0'
            Dec = '74d05.2'

        elif(values['body'] == 'Alphecca'):
            SHA = '126d09.9'
            Dec = '26d39.7'

        elif(values['body'] == 'Antares'):
            SHA = '112d24.4'
            Dec = '-26d27.8'

        elif(values['body'] == 'Atria'):
            SHA = '107d25.2'
            Dec = '-69d03.0'

        elif(values['body'] == 'Sabik'):
            SHA = '102d10.9'
            Dec = '-15d44.4'

        elif(values['body'] == 'Shaula'):
            SHA = '96d20.0'
            Dec = '-37d06.'

        elif(values['body'] == 'Rasalhague'):
            SHA = '96d05.2'
            Dec = '12d33.1'

        elif(values['body'] == 'Etamin'):
            SHA = '90d45.9'
            Dec = '51d29.3'

        elif(values['body'] == 'Kaus Aust.'):
            SHA = '83d41.9'
            Dec = '-34d22.4'

        elif(values['body'] == 'Vega'):
            SHA = '80d38.2'
            Dec = '38d48.1'

        elif(values['body'] == 'Nunki'):
            SHA = '75d56.6'
            Dec = '-26d16.4'

        elif(values['body'] == 'Altair'):
            SHA = '62d06.9'
            Dec = '8d54.8'

        elif(values['body'] == 'Peacock'):
            SHA = '53d17.2'
            Dec = '-56d41.0'

        elif(values['body'] == 'Deneb'):
            SHA = '49d30.7'
            Dec = '45d20.5'

        elif(values['body'] == 'Enif'):
            SHA = '33d45.7'
            Dec = '9d57.0'

        elif(values['body'] == 'Alnair'):
            SHA = '27d42.0'
            Dec = '-46d53.1'

        elif(values['body'] == 'Fomalhaut'):
            SHA = '15d22.4'
            Dec = '-29d32.3'

        elif(values['body'] == 'Scheat'):
            SHA = '13d51.8'
            Dec = '28d10.3'

        elif(values['body'] == 'Markab'):
            SHA = '13d36.7'
            Dec = '15d17.6'


        else:
            values['error'] = 'mandatory information is missing'
            return values


        return values    #This calculation is stubbed out
    elif(values['op'] == 'correct'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'locate'):
        return values    #This calculation is stubbed out
    else:
        values = {}
        values['error'] = 'op is not a legal operation'
        return values

