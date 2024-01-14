from flask import render_template, redirect, url_for, request, flash, abort
from islandApp import app, db, bcrypt
from flask import Flask, jsonify, render_template
from PIL import Image
from datetime import datetime as dt
from sqlalchemy import desc


from islandApp.dbconnect import *

current_year = dt.now().year

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(415)
def unsupported_media_type(e):
    return render_template('errors/415.html'), 415

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500


@app.route("/home/")
@app.route("/")
def islands():
    islands= getIslands()
    return render_template("index.html", islands=islands)





def activities(request):
    location = request.path_info.split('/')[-1]
    return render_template (request, 'activities.html', {'location': location.capitalize()})

def get_activities_for_island(island):
      return [
        {'name': 'Activity 1', 'description': 'Description 1'},
        {'name': 'Activity 2', 'description': 'Description 2'},
        {'name': 'Activity 3', 'description': 'Description 3'},
    ]

@app.route('/activities/<island>')
def activities(island):

    activities = get_activities_for_island(island)

    return render_template('activities.html', activities=activities,location=island.capitalize())




@app.route('/beaches/<island>')
def beaches(island):
    if island == 'spetses':
        beaches= getBeaches(1)
    elif island == 'hydra':
        beaches = getBeaches(2)
    elif island == 'poros':
        beaches = getBeaches(3)

    return render_template('beaches.html', island=island, beaches=beaches)

@app.route('/stay/<island>')
def stay(island):
    if island == 'spetses':
        stay = getStay(1)
    elif island == 'hydra':
        stay = getStay(2)
    elif island == 'poros':
        stay = getStay(3)
    return render_template('stay.html', island=island, stay = stay, location=island.capitalize())


@app.route('/food/<island>')
def food(island):
    if island == 'spetses':
        food = getFood(1)
    elif island == 'hydra':
        food = getFood(2)
    elif island == 'poros':
        food = getFood(3)
    return render_template('food.html', island=island, food=food)

@app.route('/event/<island>')
def event(island):
    if island == 'spetses':
        event = getEvent(1)
    elif island == 'hydra':
        event = getEvent(2)
    elif island == 'poros':
        event = getEvent(3)
    return render_template('event.html', island=island, event=event)


@app.route('/museum/<island>')
def museum(island):
    if island == 'spetses':
        museum = getMuseum(1)
    elif island == 'hydra':
        museum = getMuseum(2)
    elif island == 'poros':
        museum = getMuseum(3)
    return render_template('museum.html', island=island, museum=museum)



@app.route('/route/<island>')
def route(island):
    if island == 'spetses':
        route = getRoute(1)
        museum = getMuseum(1)
        beaches = getBeaches(1)
        stay = getStay(1)

    elif island == 'hydra':
        route = getRoute(2)
        museum = getMuseum(2)
        beaches = getBeaches(2)
        stay = getStay(2)

    elif island == 'poros':
        route = getRoute(3)
        museum = getMuseum(3)
        beaches = getBeaches(3)
        stay = getStay(3)

    return render_template('route.html', island=island, route=route,museum=museum,beaches=beaches, stay=stay)



@app.route('/buses/<int:startPlace>/<int:destinationPlace>/<island>')
def buses(startPlace, destinationPlace, island):

    if island == 'spetses':
        if startPlace < destinationPlace:
            connect = getConnect(startPlace, destinationPlace, 1)
            route = getRoute(1)
            if connect == []:
                route = getRoute(1)
        else:
            a=startPlace
            b=destinationPlace
            startPlace=b
            destinationPlace=a
            connect = getConnect(startPlace, destinationPlace, 1)
            route = getRoute(1)


    elif island == 'poros':
        if startPlace < destinationPlace:
            connect = getConnect(startPlace, destinationPlace, 3)
            route = getRoute(3)
            if connect == []:
                route = getRoute(3)

        else:
            a=startPlace
            b=destinationPlace
            startPlace=b
            destinationPlace=a
            connect = getConnect(startPlace, destinationPlace, 3)
            route = getRoute(3)


    return render_template('buses.html', island=island, startPlace=startPlace, destinationPlace=destinationPlace, route=route, connect=connect)


