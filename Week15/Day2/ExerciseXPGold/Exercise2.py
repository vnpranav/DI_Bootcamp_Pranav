time_earth = 1000000000
age_earth = time_earth / 31557600

ratios = {
   "earth": 1,
   "mercury" : 0.2408467,
   "venus" : 0.61519726,
   "mars" : 1.8808158,
   "jupiter" : 11.862615,
   "saturn" : 29.447498,
   "uranus" : 84.016846,
   "neptune" : 164.79132,
}

for planet in ratios.keys():
   print(f"Age on {planet.title()} : {age_earth/ratios[planet]}")