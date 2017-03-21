def dispatch(values=None):


    #Validate parm
    if(values == None):
        return {'error': 'parameter is missing'}
    if(not(isinstance(values,dict))):
        return {'error': 'parameter is not a dictionary'}
    if (not('op' in values)):
        values['error'] = 'no op  is specified'
        return values

    if(values['altitude'] is not None):
        values['error'] = 'altitude is not None'
    if(values['op'] == 'adjust','predict','correct' or'locate'):
        return {'error': 'op is not a legal operation'}


    if(values['observation'] >=90):
        values['error'] = 'observation is invalid'


    #Perform designated function
    if(values['op'] == 'adjust'):
        u = values['observation']
        list1 = None
        list1 == u.split('d')
        x = list1[1]
        y = list1[2]

        if not (isinstance(x,int)):
            values['error'] = 'degree is not invalid'
            return values
        if  not (x >= 0 and x < 90) :
                values['error'] = 'degree is not invalid'
                return values




            #and (y >= 0 and y < 60)  ):




        return values    #<-------------- replace this with your implementation
    elif(values['op'] == 'predict'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'correct'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'locate'):
        return values    #This calculation is stubbed out
    else:
        values['error'] = 'op is not a legal operation'
        return values

