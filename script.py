# list of destinations
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

# test traveler
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# identify each location based on its index 
def get_destination_index(destination):
  return destinations.index(destination)

# get traveler's destination as index
def get_traveler_location(traveler):
    return get_destination_index(traveler[1])

# test traveler's destination
test_destination_index = get_traveler_location(test_traveler)
print (test_destination_index)

# list of attractions
attractions =  [[] for x in range(5)]
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions[destination_index].append(attraction)
  except ValueError:
    return

# test 
add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# Finding the Best Places to Go
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for possible_attraction in attractions_in_city:
    attraction_tags=possible_attraction[1]
    for interest in attraction_tags:
      if interest in interests:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest      
print (find_attractions("Los Angeles, USA", ['art']))  