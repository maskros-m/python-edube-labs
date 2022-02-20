class WeekDayError(Exception):
    pass
    

class Weeker:
    __weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    __dayvalues = [0, 1, 2, 3, 4, 5, 6]
        

    def __init__(self, day):
        self.__day = day
        if self.__day not in Weeker.__weekdays:
            raise WeekDayError

    def __str__(self):

        return self.__day

    def add_days(self, n):
        self.__i = Weeker.__weekdays.index(self.__day)
        self.__whichday = Weeker.__dayvalues[self.__i] + (n % 7)
        if self.__whichday == 7:
            self.__whichday = 0
        self.__day = Weeker.__weekdays[self.__whichday]

    def subtract_days(self, n):
        self.__ind = Weeker.__weekdays.index(self.__day)
        if n % 7 > self.__ind:
            self.__whichday = 7 - abs(Weeker.__dayvalues[self.__ind] - (n % 7))
        else:
            self.__whichday = Weeker.__dayvalues[self.__ind] - (n % 7)

        self.__day = Weeker.__weekdays[self.__whichday]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
