def LeepYear(year):
    if year%4==0 and year!=100:
        print(year,"is leep year")
    elif year%400==0:
        print(year,"year is leep year")
    else:
        print(year,"year is not leep year")
year=int(input("Enter the year:"))
LeepYear(year)
