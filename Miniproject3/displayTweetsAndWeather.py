import pyowm

owm = pyowm.OWM("a40051c6d53e900889105abcdc376832");

observation = owm.weather_at_place('London,uk')
w = observation.get_weather()
print(w)