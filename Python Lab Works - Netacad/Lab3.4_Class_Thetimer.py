class Timer:
    def __init__(self, hr, min, sec):
        self.__hour = hr
        self.__minute = min
        self.__second = sec   

    def __str__(self):
        self.__phour = str(self.__hour)
        self.__pmin = str(self.__minute)
        self.__psec = str(self.__second)
        if self.__hour < 10:
            self.__phour = '0' + self.__phour
        if self.__minute < 10:
            self.__pmin = '0' + self.__pmin
        if self.__second < 10:
            self.__psec = '0' + self.__psec
        
        return f"{self.__phour}:{self.__pmin}:{self.__psec}"

    def next_second(self):
        if self.__second <= 58:
            self.__second += 1
        elif self.__second == 59:
            self.__second = 0
            if self.__minute <= 58:
                self.__minute += 1
            elif self.__minute == 59:
                self.__minute = 0
                if self.__hour < 23:
                    self.__hour += 1
                else:
                    self.__hour = 0

    def prev_second(self):
        if self.__second > 0:
            self.__second -= 1
        elif self.__second == 0:
            self.__second = 59
            if self.__minute > 0:
                self.__minute -= 1
            elif self.__minute == 0:
                self.__minute = 59
                if self.__hour > 0:
                    self.__hour -= 1
                else:
                    self.__hour = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
