"""write a python program to find a 
leap year or not"""
def isLeapYear(year):
  if(year %4==0 and year %100!=0) or year %400==0:
    return True
  else:
    return False
year=int(input ("ENTER A YEAR : "))
if isLeapYear(year):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")