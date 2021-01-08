Day = [31,28,31,30,31,30,31,31,30,31,30,31]

month,day = input().split(" ")

sum = 0
date = 0

for i in range(0,int(month)-1) :
    sum = sum+Day[i]

sum = sum + int(day)
date = sum%7

if date == 1 :
    print("MON")
elif date == 2 :
    print("TUE")
elif date == 3 :
    print("WED")
elif date == 4 :
    print("THU")
elif date == 5 :
    print("FRI")
elif date == 6 :
    print("SAT")
elif date == 0 :
    print("SUN")
