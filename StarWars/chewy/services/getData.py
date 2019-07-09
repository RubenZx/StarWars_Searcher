# Python tool to take the data from the Swapi
import requests

# The 5 next imports doesn't work, why?
# from ..models.people import People
# from ..models.planet import Planet
# from ..models.film import Film
# from ..models.species import Species
# from ..models.transport import Vehicle, Starship

response = requests.get("https://swapi.co/api/api")
while response.status_code != 200:
    response = requests.get("https://swapi.co/api/")
# API connection, and check if it is a succesful connection

urls = []
dic = response.json()
for key in dic:
    urls.append(dic[key])
# We take all the urls on the API that we are going to manage

for elem in urls:
    resp = requests.get(elem).json()
    next_page = resp["next"]
    # First of all I've to save the first page, bc it couldn't be more than 1 page
    while next_page != "null":
        # Now I have to iterate the rest of the pages
