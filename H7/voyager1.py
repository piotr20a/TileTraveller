days = int(input("Number of days after 9/25/09: "))

miles_from_the_sun = 16637000000                # variable that presents distance from the sun in MILES
km_from_the_sun = miles_from_the_sun * 1.609344 # viable that presents distance from the sun in KM
au_distance = 92955887.6                        # AU distance in AU/MILES
hours = days * 24                               # turn days into hours
speed_from_the_sun_in_miles = 38241             # speed in miles/h

# distance from the sun in miles

distance_in_miles = miles_from_the_sun + (speed_from_the_sun_in_miles * hours)
distance_in_miles = round(distance_in_miles)

# distance from the sun in km

distance_in_km = km_from_the_sun + (speed_from_the_sun_in_miles * 1.609344 * hours)
distance_in_km = round(distance_in_km)

# au from the sun

distance_in_au = (distance_in_miles / au_distance)
distance_in_au = round(distance_in_au)

print(f"Miles from the sun: {distance_in_miles}")
print(f"Kilometers from the sun: {distance_in_km}")
print(f"AU from the sun: {distance_in_au}")
