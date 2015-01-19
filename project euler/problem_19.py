NumberToDays = {i:j for i,j in zip([1,2,3,4,5,6,7],['Mon','Thues', 'Wed', 'Thurs', 'Fri', 'Satu', 'Sun'])}

class year:
    'year class used to count how many Sundays fell on Monday'
    def __init__(self, year, first_day):
        self.year = year
        self.first_day = first_day

    def JudgeEvenYear(self):
        flag1 = (self.year%4!=0)
        flag2 = ((self.year%100==0)and(self.year%400!=0))
        return not(flag1 or flag2)

    def CalFirDayNextY(self):
        if self.JudgeEvenYear():
            days = 366
        else:
            days = 365
#        print self.first_day, "after", days
        tmp = (self.first_day + days)%7
        if tmp == 0:
            return 7
        else:
            return tmp

    def NextMonthDay(self, month, first_day):
        if month in [1,3,5,7,8,10]:
            days = 31
        if month in [4,6,9,11]:
            days = 30
        if month == 2:
            if self.JudgeEvenYear():
                days = 29
            else:
                days = 28
        tmp = (first_day+days)%7
        if tmp == 0:
            return 7
        else:
            return tmp
        

    def CalSunFirMon(self):
        if self.first_day == 7:
            count = 1
        else:
            count = 0
        current_month_day = self.first_day
        for month in range(1,12):
            next_month_day = self.NextMonthDay(month, current_month_day)
            if next_month_day == 7:
#                print "year", self.year, "month", month, "is Saturday"
                count += 1
            current_month_day = next_month_day
            
        return count
        

first_year = year(1900, 1)
print first_year.CalSunFirMon()
print first_year.CalFirDayNextY()
print first_year.JudgeEvenYear()
result = 0
start_day = 1
for i in range(1900, 2001):
    year_to_cal = year(i, start_day)
    result += year_to_cal.CalSunFirMon()
#    print "year\t", i, "start day \t", start_day, "result", result
    start_day = year_to_cal.CalFirDayNextY()
print result-first_year.CalSunFirMon()

        
            
        