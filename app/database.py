"""Defines all the functions related to the database"""
from app import db

def fetch_restaurants() -> dict:
    """Reads all restaurants listed in the todo table

    Returns:
        A list of dictionaries
    """

    conn = db.connect()
    query_results = conn.execute("Select * from Restaurants;").fetchall()
    conn.close()
    restaurant_list = []
    for result in query_results:
        item = {
            "RestaurantID": result[0],
            "RestaurantName": result[1],
            "ZipCode": result[2],
            "Address": result[3]
        }
        restaurant_list.append(item)

    return restaurant_list

def fetch_menu(restaurant_id) -> dict:
    """ Reads all menu items for the input restaurant_id

    Returns:
        A list of dictionaries
    """
    conn = db.connect()
    query_results = conn.execute("Select * from Dishes where RestaurantID = " + restaurant_id + ";").fetchall()
    conn.close()
    menu_list = []
    for result in query_results:
        item = {
            "DishID": result[0],
            "RestaurantID": result[1],
            "DishName": result[2],
            "Price": result[3],
            "AvgRating": result[4]
        }
        menu_list.append(item)

    return menu_list

# def update_task_entry(task_id: int, text: str) -> None:
#     """Updates task description based on given `task_id`

#     Args:
#         task_id (int): Targeted task_id
#         text (str): Updated description

#     Returns:
#         None
#     """

#     conn = db.connect()
#     query = 'Update tasks set task = "{}" where id = {};'.format(text, task_id)
#     conn.execute(query)
#     conn.close()


# def update_status_entry(task_id: int, text: str) -> None:
#     """Updates task status based on given `task_id`

#     Args:
#         task_id (int): Targeted task_id
#         text (str): Updated status

#     Returns:
#         None
#     """

#     conn = db.connect()
#     query = 'Update tasks set status = "{}" where id = {};'.format(text, task_id)
#     conn.execute(query)
#     conn.close()


# def insert_new_task(text: str) ->  int:
#     """Insert new task to todo table.

#     Args:
#         text (str): Task description

#     Returns: The task ID for the inserted entry
#     """

#     conn = db.connect()
#     query = 'Insert Into tasks (task, status) VALUES ("{}", "{}");'.format(
#         text, "Todo")
#     conn.execute(query)
#     query_results = conn.execute("Select LAST_INSERT_ID();")
#     query_results = [x for x in query_results]
#     task_id = query_results[0][0]
#     conn.close()

#     return task_id


# def remove_task_by_id(task_id: int) -> None:
#     """ remove entries based on task ID """
#     conn = db.connect()
#     query = 'Delete From tasks where id={};'.format(task_id)
#     conn.execute(query)
#     conn.close()
