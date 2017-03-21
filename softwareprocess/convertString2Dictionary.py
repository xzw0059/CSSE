import urllib
import re
def convertString2Dictionary(inputString = ""):
    wholdstr = inputString
    errorDict = {'error':'true'}
    wholdstr = urllib.unquote(wholdstr)
    if inputString == "":
        print errorDict
        return
    Dir = []
    ##
    wholdstr = wholdstr.split(' ')
    for i in wholdstr:
        pair = []
        if i != "":
            midstr1 = i
##cancle space
    wholdstr = wholdstr.split(',')

    for i in wholdstr:
        pair = []
        if i != " " or "":
            midstr1 = i
##cancle ,
        midstr1 = midstr1.split('=')
        if len(midstr1) != 2:
            print errorDict
        if type(midstr1[0]) != str and len(midstr1) < 2:
            print errorDict
        if len(midstr1) < 2:
            print errorDict
        for m in midstr1[0]:
            if type(m) != str or type(m)!= int:
                print errorDict
        for n in midstr1[1]:
            if type(m) != str or type(m)!= int:
                print errorDict
            ##
        pair.append(midstr1[0])
        pair.append(midstr1[1])
        Dir.append(pair)
    print Dir
