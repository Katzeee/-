from time import strptime,mktime,localtime,strftime
def string2stamp(timeString):
    _timeTuple = strptime(timeString, "%Y%m%d")
    return int(mktime(_timeTuple))

def stamp2string(timeStamp):
    _timeTuple = localtime(float(timeStamp))
    return strftime("%Y%m%d", _timeTuple)

def FlattenList(_foldList):
    flatList = [item for sublist in _foldList for item in sublist]
    return flatList

