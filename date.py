import datetime, time

timezone = time.strftime("%Z")

def getCurrentICDate():
    
    dayOfYear = int( time.strftime("%j"))
    icDay = -1
    icSeason = 'ERROR'
    icYear = datetime.datetime.now().year - 687

    if dayOfYear < 90:
        icSeason = 'Zephyr'
        icDay = dayOfYear
    elif dayOfYear < 180 and dayOfYear > 90:
        icSeason = 'Phoenix'
        icDay = dayOfYear - 90
    elif dayOfYear < 270 and dayOfYear > 180:
        icSeason = 'Scion'
        icDay = dayOfYear - 180
    elif dayOfYear > 270:
        icSeason = 'Colossus'
        icDay = dayOfYear - 270
    else:
        icSeason = 'ERROR'
        icDay = -1

    icDayString = str(icDay)
    
    if icDayString.endswith('1'):
        icDayString += 'st'
    elif icDayString.endswith('2'):
        icDayString += 'nd'
    elif icDayString.endswith('3'):
        icDayString += 'rd'
    
    return 'It is the ' + icDayString + ' of ' + icSeason + ', ' + str(icYear)
        
def getTimezone():
    return timezone