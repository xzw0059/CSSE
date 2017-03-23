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
        # print type(list1[0])
        # print type(x)
        # print x
        y = float(list1[1])
        # print type(list1[1])
        # print type(y)
        # print y
        print 123




        # print dip

        if not (isinstance(int(list1[0]),int)):
            # values['error'] = 'degree is not invalid__not int'
            values['error'] = 'observation is invalid'
            return values
        if  not (int(list1[0]) >= 0 and int(list1[0]) < 90):
            values['error'] = 'observation is invalid'
            # __not in 0~90
            return values
        if not (isinstance(y,float)):
            values['error'] = 'observation is invalid'
            # __not float
            return values
        if not (y >= 0 and y < 60):
            values['error'] = 'observation is invalid'
            # __not 0~60
            return values

        if (int(list1[0])==0 and y<0.1):
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
            values['error'] = 'height is not invalid'
            # __not num
            return values


        # if (not isinstance(float(h),float)):
        #     values['error'] = 'height is not invalid'
        #     # __not num
        #     return values


        if (not float(h) >= 0):
            values['error'] = 'height is not invalid'
            # __not >= 0
            return values

        if (not('temperature' in values)):
            t = 72
        else:
            t =values['temperature']
        if not isinstance(float(t),float):
            values['error'] = 'temperature is not invalid'
            # __not number
            return values
        if not (int(t) >= -20 and int(t) <= 120):
            values['error'] = 'temperature is not invalid'
            # __not -20~120
            return values

        tc = 5 * (float(t) - 32) / 9

        if (not('pressure' in values)):
            p = 1010
        else:
            p =float(values['pressure'])



        if not (isinstance(float(p),float)):
            values['error'] = 'pressure is not invalid'
            # __not str of number
            return values
        if not (p >= 100 and p <= 1100):
            print  values['pressure']
            values['error'] = 'pressure is not invalid'
            # __not 100~1100
            return values

        if (not('horizon' in values)):
            hr = 'natural'
        else:
            hr = values['horizon']

        if not (isinstance(hr,str)):
            values['error'] = 'horizon is not invalid'
            # __not str
            return values
        if(not(hr == 'artificial' or 'natural')):
            # values['error'] = 'horizon is not invalid__not  artificial or natural'
            values['error'] = 'horizon is not invalid'
            return values

        if (hr == 'natural'):
            dip = (-0.97 * math.sqrt( float(h) )) / 60

        else:
            dip = 0




        refraction=( -0.00452*int(p))/(273+tc)/math.tan(math.radians(y/60+int(list1[0])))
        altitude0 = y/60+int(list1[0]) + dip + refraction
        # tempalt = {}
        # tempalt = str(altitude0).split('.')
        D2 = int(altitude0)
        M2 = (altitude0 - D2)*60
        altitudedig = str(D2) + 'd' + str(round(M2,1))
        print altitudedig


        if not (isinstance(D2,int)):
            # values['error'] = 'altitude-degree is not invalid__not int'
            values['error'] = 'altitude-degree is not invalid'
            return values
        if  not (D2 > -90 and D2 < 90):
            # values['error'] = 'altitude-degree is not invalid__not in -90~90'
            values['error'] = 'altitude-degree is not invalid'
            return values

        if not (isinstance(round(M2,1),float)):
            # values['error'] = 'altitude-min is not invalid__not float'
            values['error'] = 'altitude-min is not invalid'
            return values
        if not (M2 >= 0 and round(M2,1) < 60):
            # values['error'] = 'altitude-min is not invalid__not 0~60'
            values['error'] = 'altitude is not invalid'
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
        return values    #This calculation is stubbed out
    elif(values['op'] == 'correct'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'locate'):
        return values    #This calculation is stubbed out
    else:
        values = {}
        values['error'] = 'op is not a legal operation'
        return values

