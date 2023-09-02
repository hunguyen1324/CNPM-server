from flask import Blueprint
from .services import (add_feedback_data_service,get_all_feedback_data_service,update_feedback_data_by_id_service,delete_feedback_data_by_id_service)

feedbacks_data = Blueprint("feedbacks_data",__name__)

@feedbacks_data.route("/feedback_data/add",methods = ["POST"])
def add_sensor_data():
    return add_feedback_data_service()

@feedbacks_data.route("/feedback_data/all",methods = ["GET"])
def get_all_sensors_data():
    return get_all_feedback_data_service()

@feedbacks_data.route("/feedback_data/update/<int:id>", methods=['PUT'])
def update_price_by_id(id):
    return update_feedback_data_by_id_service(id)

@feedbacks_data.route("/feedback_data/delete/<int:id>", methods=['DELETE'])
def delete_book_by_id(id):
    return delete_feedback_data_by_id_service(id)
