def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        leap = True

        if year % 100 != 0 and year % 400 != 0:
            leap = True

        if year % 100 == 0 and year % 400 != 0:
            leap = False

        if year % 100 == 0 and year % 400 == 0:
            leap = True
    else:
        if year % 100 != 0 and year % 400 != 0:
            leap = False
    
    return leap


#Main function
year = int(input())

if 1900 <= year <= 10**5:
    print(is_leap(year))