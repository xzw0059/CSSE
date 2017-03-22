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
        list1 = None
        list1 == o.split('d')
        x = list1[1]
        print x
        y = list1[2]
        print y
        h = values['height']
        tf = values['temperature']
        tc = 5 * (tf - 32) / 9
        p = values['pressure']
        hr = values['horizon']
        print dip

        if not (isinstance(x,int)):
            values['error'] = 'degree is not invalid__not int'
            return values
        if  not (x >= 0 and x < 90):
                values['error'] = 'degree is not invalid__not in 0~90'
                return values
        if not (isinstance(y,float)):
            values['error'] = 'min is not invalid__not float'
            return values
        if not (y >= 0 and y < 60):
            values['error'] = 'min is not invalid__not 0~60'
            return values

        if (h == None):
            h = 0
            return values
        if (not h.isdigit()):
            values['error'] = 'height is not invalid__not num'
            return values
        if (not h >= 0):
            values['error'] = 'height is not invalid__not >= 0'
            return values


        if (tf == None):
            t = 72
            return values
        if not (isinstance(tf,int)):
            values['error'] = 'temperature is not invalid__not int'
            return values
        if not (tf >= -20 and tf <= 120):
            values['error'] = 'temperature is not invalid__not -20~120'
            return values


        if (p == None):
            p = 1010
            return values
        if not (isinstance(p,str)):
            values['error'] = 'pressure is not invalid__not str'
            return values
        if not (p >= 100 and p <= 1100):
            values['error'] = 'pressure is not invalid__not 100~1100'
            return values

        if (hr == None):
            hr = 'natural'
            return values
        if not (isinstance(hr,str)):
            values['error'] = 'horizon is not invalid__not str'
            return values
        if(not(hr == 'artificial' or 'natural')):
            values['error'] = 'horizon is not invalid__not  artificial or natural'
            return values

        if (hr == 'natural'):
            dip = (-0.97 * math.sqrt( h )) / 60

        else:
            dip = 0
            return values



        refraction=( -0.00452*int(p))/(273+tc)/math.tan(math.radians(y/60+x))
        altitude0 = y/60+x + dip + refraction
        # tempalt = {}
        # tempalt = str(altitude0).split('.')
        D2 = int(altitude0)
        M2 = (altitude0 - D2)*60
        altitudedig = {}
        altitudedig = {'altitude':D2 + 'D' + round(M2,1)}


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

        values.update = {'altitude':altitudedig}
        values = {}
        print altitudedig












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

