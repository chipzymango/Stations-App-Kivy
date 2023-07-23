import requests
import json
import time

def searchForStopPlace(userSearch):
    searchResults = requests.get('https://api.entur.io/geocoder/v1/autocomplete?text='+ userSearch +'') # assign the retrieved data to a variable
    searchResults = json.loads(searchResults.text) # parse text of the retrieved json string a python dict
    resultId = 1 # id to differenciate between each retrieved stop place
    
    print("\nThe following stop places were found: ")

    stopPlaces = [] # list to store data about each retrieved stop place

    for result in searchResults["features"]:
        # check if result place is registered in the national stop register (NSR) through the id property.
        if "NSR:StopPlace" in str(result["properties"]["id"]):
            stopPlaceData = {
                "stopPlaceName": result["properties"]["label"], 
                "stopPlaceLocation": result["properties"]["locality"], 
                "stopPlaceId": result["properties"]["id"]
                }        
            print(str(resultId) + ": " + str(stopPlaceData["stopPlaceName"]) +" | "+ str(stopPlaceData["stopPlaceLocation"]) +" | "+ str(stopPlaceData["stopPlaceId"])) # assign an id to each stop place which the user then picks
            resultId += 1
            stopPlaces.append(stopPlaceData)
    
        # if not, it will not be included in the list
        else:
            continue
        
    return stopPlaces