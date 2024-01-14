import sqlite3
from islandApp.models import *

db=sqlite3.connect('./islandApp/team19.db', check_same_thread=False)

def getIslands():
    islands = []

    cursor=db.cursor()
    cursor.execute('''SELECT * FROM Island''')
    data = cursor.fetchall()

    for _island in data:
        island = IslandObject()
        island.name = _island[0]
        island.size = _island[1]
        island.islandId = _island[2]
        island.image = _island[3]
        island.description = _island[4]
        islands.append(island)

    return islands

def getMuseum(islandId):
    museums = []

    cursor=db.cursor()
    cursor.execute('''SELECT * FROM Museum WHERE islandId=?''',(islandId,))
    data = cursor.fetchall()

    for _museum in data:
        museum = MuseumObject()
        museum.museumId = _museum[0]
        museum.workHours = _museum[1]
        museum.islandId = _museum[2]
        museum.nameMuseum = _museum[3]
        museum.image = _museum[4]
        museum.price = _museum[5]
        museum.placeID = _museum[6]
        museums.append(museum)

    return museums

def getBeaches(islandId):
    beaches = []

    cursor=db.cursor()
    cursor.execute('''SELECT * FROM Beach WHERE islandId=?''',(islandId,))
    data = cursor.fetchall()

    for _beach in data:
        beach = BeachObject()
        beach.beachId = _beach[0]
        beach.rating = _beach[1]
        beach.beachName = _beach[2]
        beach.islandId = _beach[3]
        beach.image = _beach[4]
        beach.placeID = _beach[5]
        beaches.append(beach)

    return beaches
def getStay(islandId):
    stays = []

    cursor=db.cursor()
    cursor.execute('''SELECT * FROM Stay WHERE islandId=?''',(islandId,))
    data = cursor.fetchall()

    for _stay in data:
        stay = StayObject()
        stay.stayId = _stay[0]
        stay.name = _stay[1]
        stay.website = _stay[2]
        stay.rating = _stay[3]
        stay.food = _stay[4]
        stay.pricePerNight = _stay[5]
        stay.islandId = _stay[6]
        stay.image = _stay[7]
        stay.placeID = _stay[8]
        stays.append(stay)

    return stays

def getFood(islandId):
    foods = []

    cursor=db.cursor()
    cursor.execute('''SELECT * FROM Food WHERE islandId=?''',(islandId,))
    data = cursor.fetchall()

    for _food in data:
        food = FoodObject()
        food.foodId = _food[0]
        food.rating = _food[1]
        food.name = _food[2]
        food.type = _food[3]
        food.pricePerPerson = _food[4]
        food.islandId = _food[5]
        food.image = _food[6]
        food.placeID = _food[7]
        foods.append(food)

    return foods
def getEvent(islandId):
    events = []

    cursor=db.cursor()
    cursor.execute('''SELECT * FROM Event WHERE islandId=?''',(islandId,))
    data = cursor.fetchall()

    for _event in data:
        event = EventObject()
        event.eventId = _event[0]
        event.type = _event[1]
        event.rating = _event[2]
        event.date = _event[3]
        event.nameEvent = _event[4]
        event.islandId = _event[5]
        event.image = _event[6]
        event.price = _event[7]
        event.placeID = _event[8]
        events.append(event)

    return events

def getRoute(islandId):
    routes = []

    cursor=db.cursor()
    cursor.execute('''SELECT * FROM Route WHERE islandId=?''',(islandId,))
    data = cursor.fetchall()

    for _route in data:
        route = RouteObject()
        route.routeId = _route[0]
        route.BusName = _route[1]
        route.placeID = _route[2]
        route.islandId = _route[3]
        route.image = _route[4]
        route.price = _route[5]
        route.schedule = _route[6]

        routes.append(route)

    return routes


def getConnect(startPlace, destinationPlace, islandId,):

    connects=[]

    query = '''
    SELECT Route.routeid, Route.BusName, Route.islandId, Route.image,Route.schedule,Route.price,
    Connection.startPlace,Connection.destinationPlace
    FROM Route
    JOIN Connection ON Route.routeId = Connection.routeId
    WHERE ? >= Connection.startPlace AND ? <= Connection.destinationPlace AND ? = Route.islandId
'''

    cursor = db.cursor()
    cursor.execute(query, (startPlace, destinationPlace, islandId))
    data = cursor.fetchall()

    for _connect in data:
        connect = ConnectObject()
        connect.routeId = _connect[0]
        connect.BusName = _connect[1]
        connect.islandId = _connect[2]
        connect.image=_connect[3]
        connect.schedule=_connect[4]
        connect.price=_connect[5]

        connects.append(connect)


    return connects

