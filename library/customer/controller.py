from flask import Blueprint
from .services import (add_Customer_data_service,get_all_Customer_data_service,update_Customer_data_by_id_service,delete_Customer_data_by_id_service)

Customers_data = Blueprint("Customers_data",__name__)

@Customers_data.route("/customer_data/add",methods = ["POST"])
def add_sensor_data():
    return add_Customer_data_service()

@Customers_data.route("/customer_data/all",methods = ["GET"])
def get_all_sensors_data():
    return get_all_Customer_data_service()

@Customers_data.route("/customer_data/update/<int:id>", methods=['PUT'])
def update_price_by_id(id):
    return update_Customer_data_by_id_service(id)

@Customers_data.route("/customer_data/delete/<int:id>", methods=['DELETE'])
def delete_book_by_id(id):
    return delete_Customer_data_by_id_service(id)
