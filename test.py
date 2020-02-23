import ephem, datetime
date =datetime.date.today()
print(date)
planet_name=input()

# planet_obj = ephem.Sun()
planet_obj = getattr(ephem, planet_name)(date)
print(planet_name+' in', ephem.constellation(planet_obj)[1])