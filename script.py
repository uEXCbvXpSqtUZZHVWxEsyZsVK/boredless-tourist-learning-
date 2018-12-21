#list of destinations
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

#test traveler
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# identify each location based on its index 
def get_destination_index(destination):
  return destinations.index(destination)

# get traveler's destination as index
def get_traveler_location(traveler):
    return get_destination_index(traveler[1])

#test traveler's destination
test_destination_index = get_traveler_location(test_traveler)
print (test_destination_index)


