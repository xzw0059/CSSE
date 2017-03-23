import math

def dispatch(values=None,dip=None):


    #Validate parm
    if(values == None):
        return {'error': 'parameter is missing'}

    if(not(isinstance(values,dict))):
        return {'error': 'parameter is not a dictionary'}

    if (not('op' in values)):
        values['error'] = 'no op  is specified'
        return values



    # if(values['op'] !=None and values['op'] != 'adjust'):
    #     return {'error': 'op is not a legal operation'}


    # if(not(values['altitude'] ==  None)):
    #     values['error'] = 'altitude is not None'
    #     return values




    #Perform designated function
    if(values['op'] == 'adjust'):

        o = values['observation']
        list1 = {}
        list1 = o.split('d')
        # print type(list1[0])
        # print type(x)
        # print x
        y = float(list1[1])
        # print type(list1[1])
        # print type(y)
        # print y




        # print dip

        if not (isinstance(int(list1[0]),int)):
            values['error'] = 'degree is not invalid__not int'
            return values
        if  not (int(list1[0]) >= 0 and int(list1[0]) < 90):
                values['error'] = 'degree is not invalid__not in 0~90'
                return values
        if not (isinstance(y,float)):
            values['error'] = 'min is not invalid__not float'
            return values
        if not (y >= 0 and y < 60):
            values['error'] = 'min is not invalid__not 0~60'
            return values

        if (int(list1[0])==0 and y<0.1):
            values['error'] = 'o is not invalid__o is LT 0.0.1'
            return values

        if (not('height' in values)):
            h = 0.0
        else:
            h = values['height']

        if (not isinstance(float(h),float)):
            values['error'] = 'height is not invalid__not num'
            return values


        if (not float(h) >= 0):
            values['error'] = 'height is not invalid__not >= 0'
            return values

        if (not('temperature' in values)):
            t = 72
        else:
            t =values['temperature']
        if not isinstance(float(t),float):
            values['error'] = 'temperature is not invalid__not number'
            return values
        if not (int(t) >= -20 and int(t) <= 120):
            values['error'] = 'temperature is not invalid__not -20~120'
            return values

        tc = 5 * (float(t) - 32) / 9

        if (not('pressure' in values)):
            p = 1010
        else:
            p =float(values['pressure'])



        if not (isinstance(float(values['pressure']),float)):
            values['error'] = 'pressure is not invalid__not str of number'
            return values
        if not (p >= 100 and p <= 1100):
            print  values['pressure']
            values['error'] = 'pressure is not invalid__not 100~1100'
            return values


        if (values['horizon'] == None):
            values['horizon'] = 'natural'
            return values
        if not (isinstance(values['horizon'],str)):
            values['error'] = 'horizon is not invalid__not str'
            return values
        if(not(values['horizon'] == 'artificial' or 'natural')):
            values['error'] = 'horizon is not invalid__not  artificial or natural'
            return values

        if (values['horizon'] == 'natural'):
            dip = (-0.97 * math.sqrt( float(values['height']) )) / 60

        else:
            dip = 0
            return values



        refraction=( -0.00452*int(p))/(273+tc)/math.tan(math.radians(y/60+int(list1[0])))
        altitude0 = y/60+int(list1[0]) + dip + refraction
        # tempalt = {}
        # tempalt = str(altitude0).split('.')
        D2 = int(altitude0)
        M2 = (altitude0 - D2)*60
        altitudedig = str(D2) + 'd' + str(round(M2,1))
        # print type(altitudedig)


        if not (isinstance(D2,int)):
            values['error'] = 'altitude-degree is not invalid__not int'
            return values
        if  not (D2 > -90 and D2 < 90):
                values['error'] = 'altitude-degree is not invalid__not in -90~90'
                return values

        if not (isinstance(round(M2,1),float)):
            values['error'] = 'altitude-min is not invalid__not float'
            return values
        if not (M2 >= 0 and round(M2,1) < 60):
            values['error'] = 'altitude-min is not invalid__not 0~60'
            return values

        if ('altitude' in values):
            values['error'] = 'altitude-already exist'
            return values

        values['altitude'] = altitudedig

        # print altitudedig
        # print values












        return values    #<-------------- replace this with your implementation
    elif(values['op'] == 'predict'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'correct'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'locate'):
        return values    #This calculation is stubbed out
    else:
        values = {}
        values['error'] = 'op is not a legal operation'
        return values

