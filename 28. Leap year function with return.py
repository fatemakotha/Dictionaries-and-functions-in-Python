def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        
        
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #if is_leap(2004) = True OR if is_leap(2023) = False
    if is_leap(year): 
        month_days[1] = 29 #month on the 1st index is set to 29
        print(month_days) #for 2004 it prints: [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = month_days[month - 1]
        return days
    else:
        print(month_days) #for 2022 it prints: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = month_days[month - 1] 
        return days #returns 28
        
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month) #days is set to the value of days_in_month
print(days)