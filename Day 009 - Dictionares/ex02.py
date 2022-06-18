# You are going to write a program that adds to a travel_log
# Write a function that will work with the following line of code to add the entry for Russia to the travel_log.
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_a_new_country(pais, visitas, cidades):
    dict = {'country': pais, 'visits': visitas, 'cities': cidades}
    travel_log.append(dict)

print(travel_log)

add_a_new_country('Russia', 2, ['Moscow', 'Saint Petesburg'])

print(f"You visited {travel_log[2]['country']} {travel_log[2]['visits']} times")
print(f"You've been to {travel_log[2]['cities'][0]} and {travel_log[2]['cities'][1]}")