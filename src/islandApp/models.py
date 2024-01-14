from islandApp import db



class IslandObject():
    name = ""
    size = 0
    islandId = 0
    image = ""
    description = ""




class BeachObject():
    beachId = 0
    rating = 0
    beachName = ""
    islandId = 0
    image = ""
    placeID = 0



class StayObject():
    stayId = 0
    name = ""
    website = ""
    rating = 0
    food = ""
    pricePerNight = 0
    islandId = 0
    image = ""
    placeID = 0


class FoodObject():
    foodId = 0
    rating = 0
    name = ""
    type = ""
    pricePerPerson = 0
    islandId = 0
    image = ""
    placeID = 0


class EventObject():
    eventId = 0
    type = ""
    rating = 0
    date = ""
    nameEvent = ""
    islandId = 0
    image = ""
    price = 0
    placeID = 0



class MuseumObject():
    museumId = 0
    workHours = ""
    nameMuseum = ""
    image = ""
    islandId = 0
    price = 0
    placeID = 0


class RouteObject():
    routeId = 0
    BusName = ""
    placeID = 0
    islandId = 0
    image = ""
    price = 0
    schedule = ""

class ConnectObject():
    routeId=0
    BusName=""
    islandId=0
    image=""
    schedule=""
    price =0

