# https://stackoverflow.com/questions/11556958/sending-data-from-html-form-to-a-python-script-in-flask
""" Specifies routing for the application"""
from flask import render_template, request, jsonify
from app import app
from app import database as db_helper

@app.route("/restaurant/<int:RestaurantID>")
def menupage(restaurant_id):
    """returns rendered menu page for a restaurant"""
    dish_list = db_helper.fetch_menu(restaurant_id)
    return render_template("index.html", menu=dish_list)

@app.route("/")
def homepage():
    """ returns rendered homepage (list of restaurants) """
    restaurant_list = db_helper.fetch_restaurants()
    return render_template("index.html", restaurants=restaurant_list)

@app.route("/delete/<int:restaurant_id>", methods=['POST'])
def delete(restaurant_id):
    """ recieved post requests for restaurant delete """

    try:
        db_helper.remove_restaurant_by_id(restaurant_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)

@app.route("/edit/<int:restaurant_id>", methods=['POST'])
def update(restaurant_id):
    """ recieved post requests for restaurant updates """

    data = request.get_json()

    try:
        if "status" in data:
            db_helper.update_restaurant_entry(restaurant_id, data["status"])
            result = {'success': True, 'response': 'Status Updated'}
        elif "description" in data:
            db_helper.update_restaurant_entry(restaurant_id, data["description"])
            result = {'success': True, 'response': 'Task Updated'}
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/create/", methods=['POST'])
def create():
    """ recieves post requests to add new restaurant """
    data = request.form
    db_helper.insert_new_restaurant(data['rest-name'], data['rest-zip'], data['rest-addr'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)