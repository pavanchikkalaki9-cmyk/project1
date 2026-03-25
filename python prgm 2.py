class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y
    def day(self):
        print("Day =", self.d)
    def month(self):
        print("Month =", self.m)
    def year(self):
        print("Year =", self.y)
    def monthName(self):
        months=["january","february","march","april","may","june","july","august","september","october","november","december","invalid"]
        if(1 <= self.m <= 12):
            print("Month Name=",months[self.m])
        else:
            print("Invalid month")
    def isLeapYear(self):
        if(self.y % 400 == 0) and (self.y % 100 == 0):
            print("LeapYear")
        elif(self.y % 4 == 0) and (self.y % 100 != 0):
            print("LeapYear")
        else:
            print("not Leap Year")
dd = int(input("enter the day:"))
mm = int(input("enter the month:"))
yy = int(input("enter the year:"))

d1 = Date(dd, mm, yy)
d1.day()
d1.month()
d1.year()
d1.monthName()
d1.isLeapYear()
