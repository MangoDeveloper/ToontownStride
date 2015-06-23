from toontown.toonbase import ToontownGlobals, TTLocalizer
import calendar, datetime

Holidays = {
    ToontownGlobals.LAUGHING_MAN: {
        'startMonth': 6,
        'startDay': 22,
        'endMonth': 6,
        'endDay': 22,
        'startMessage': TTLocalizer.LaughingManHolidayStart,
        'ongoingMessage': TTLocalizer.LaughingManHolidayOngoing,
        'endMessage': TTLocalizer.LaughingManHolidayEnd
    },
    ToontownGlobals.GRAND_PRIX: {
        'weekDay': 0,
        'startMessage': TTLocalizer.CircuitRaceStart,
        'ongoingMessage': TTLocalizer.CircuitRaceOngoing,
        'endMessage': TTLocalizer.CircuitRaceEnd
    },
    ToontownGlobals.FISH_BINGO: {
        'weekDay': 2,
        'startMessage': TTLocalizer.FishBingoStart,
        'ongoingMessage': TTLocalizer.FishBingoOngoing,
        'endMessage': TTLocalizer.FishBingoEnd
    },
    ToontownGlobals.SILLY_SATURDAY: {
        'weekDay': 5,
        'startMessage': TTLocalizer.SillySaturdayStart,
        'ongoingMessage': TTLocalizer.SillySaturdayOngoing,
        'endMessage': TTLocalizer.SillySaturdayEnd
    },
    ToontownGlobals.BLACK_CAT_DAY: {
        'startDay': 13,
        'endDay': 13,
        'startMessage': TTLocalizer.BlackCatHolidayStart,
        'ongoingMessage': TTLocalizer.BlackCatHolidayStart,
        'endMessage': TTLocalizer.BlackCatHolidayEnd
    },
    ToontownGlobals.APRIL_TOONS_WEEK: {
        'startMonth': 4,
        'startDay': 1,
        'endMonth': 4,
        'endDay': 7,
        'startMessage': TTLocalizer.AprilToonsWeekStart,
        'ongoingMessage': TTLocalizer.AprilToonsWeekStart,
        'endMessage': TTLocalizer.AprilToonsWeekEnd
    },
    ToontownGlobals.IDES_OF_MARCH: {
        'startMonth': 3,
        'startDay': 14,
        'endMonth': 3,
        'endDay': 20,
        'startMessage': TTLocalizer.IdesOfMarchStart,
        'ongoingMessage': TTLocalizer.IdesOfMarchStart,
        'endMessage': TTLocalizer.IdesOfMarchEnd,
        'speedchatIndexes': [30450], # It's easy to be green!
        'effectMessage': TTLocalizer.GreenToonEffectMsg,
        'effectDelay': 10
    }
}

def getHoliday(id):
    return Holidays.get(id, {})

def getUnixTime(date):
    epoch = datetime.datetime.fromtimestamp(0)
    delta = date - epoch

    return delta.total_seconds()

def getEndDate(holiday):
    rightNow = datetime.datetime.now()
    endMonth = holiday['endMonth'] if 'endMonth' in holiday else rightNow.month
    endDay = holiday['endDay'] if 'endDay' in holiday else (rightNow.day if 'weekDay' in holiday else calendar.monthrange(rightNow.year, endMonth)[1])

    date = datetime.datetime(rightNow.year, endMonth, endDay)
    date += datetime.timedelta(days=1)

    return date