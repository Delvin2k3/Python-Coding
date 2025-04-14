import datetime

current_year = datetime.datetime.today().year
birth_year = input('Birth year: ')
age = current_year - int(birth_year)
print (age)
