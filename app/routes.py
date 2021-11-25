# https://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask
""" Specifies routing for the application"""
from flask import render_template, request, jsonify, redirect
from flask.helpers import url_for
from app import app
from app import database as db_helper

@app.route("/")
def homepage():
    """ returns rendered homepage (list of restaurants) """
    restaurant_list = db_helper.fetch_restaurants()
    return render_template("index.html", restaurants=restaurant_list)

@app.route("/advq1")
def advq1():
    """ returns rendered homepage (list of restaurants) """
    restaurant_list = db_helper.fetch_queried_restaurants_1()
    return render_template("advanced1.html", queried_restaurants_1=restaurant_list)

@app.route("/advq2")
def advq2():
    """ returns rendered homepage (list of restaurants) """
    dish_list = db_helper.fetch_queried_restaurants_2()
    return render_template("advanced2.html", queried_dishes_2=dish_list)

@app.route("/search", methods=['POST'])
def searchpage():
    """ returns rendered search page (list of restaurants) """
    data = request.form.get('search-query')
    restaurant_list = db_helper.search_restaurants_by_name(str(data))
    return render_template("index.html", restaurants=restaurant_list)

@app.route("/delete/<int:restaurant_id>", methods=['POST'])
def delete(restaurant_id):
    """ recieved post requests for restaurant delete """
    try:
        db_helper.remove_restaurant_by_id(restaurant_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return redirect(url_for("homepage"))

@app.route("/edit/<int:restaurant_id>", methods=['POST'])
def update(restaurant_id):
    """ recieved post requests for restaurant updates """
    data = request.form
    db_helper.update_restaurant_entry(restaurant_id, data['rest-name'], data['rest-zip'], data['rest-addr'])
    result = {'success': True, 'response': 'Status Updated'}
    return redirect(url_for("homepage"))

@app.route("/create/", methods=['POST'])
def create():
    """ recieves post requests to add new restaurant """
    data = request.form
    db_helper.insert_new_restaurant(data['rest-name'], data['rest-zip'], data['rest-addr'])
    result = {'success': True, 'response': 'Done'}
    return redirect(url_for("homepage"))

@app.route("/restaurant/<int:restaurant_id>")
def menupage(restaurant_id):
    """returns rendered menu page for a restaurant"""
    restaurant_info = db_helper.fetch_restaurant_info(restaurant_id)
    restaurant_info = restaurant_info[0]
    dish_list = db_helper.fetch_dishes(restaurant_id)
    return render_template("menu.html", dishes=dish_list, restaurant=restaurant_info)

@app.route("/restaurant/<int:restaurant_id>/edit/<int:dish_id>", methods=["POST"])
def update_dish(restaurant_id, dish_id):
    """updates target dish at target restaurant and refreshes page"""
    data = request.form
    db_helper.update_dish_entry(dish_id, restaurant_id, data['dish-name'], data['dish-price'])
    return redirect(url_for("menupage", restaurant_id=restaurant_id))

@app.route("/restaurant/<int:restaurant_id>/create", methods=["POST"])
def create_dish(restaurant_id):
    """creates dish at target restaurant and refreshes page"""
    data = request.form
    db_helper.insert_new_dish(data['dish-name'], data['dish-price'])
    return redirect(url_for("menupage", restaurant_id=restaurant_id))

@app.route("/restaurant/<int:restaurant_id>/delete/<int:dish_id>", methods=["POST"])
def delete_dish(restaurant_id, dish_id):
    """deletes dish at target restaurant and refreshes page"""
    try:
        db_helper.remove_dish_by_id(dish_id,restaurant_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return redirect(url_for("menupage", restaurant_id=restaurant_id))
