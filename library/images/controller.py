from flask import Blueprint, send_from_directory
from .services import (add_image_service,get_all_image_service,get_latest_images_service
,delete_image_service,update_image_service)
import os
images = Blueprint("images", __name__)

@images.route("/image/add", methods = ['POST'])
def add_image():
    return add_image_service()

@images.route("/image/all",methods = ['GET'])
def get_all_image():
    return get_all_image_service()

@images.route("/image/latest",methods = ['GET'])
def get_latest_image_controller():
    return get_latest_images_service()

@images.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static'), filename)

@images.route("/image/delete/<int:id>",methods =["DELETE"])
def delete_image_by_id(id):
    return delete_image_service(id)

@images.route("/image/update/<int:id>",methods =["PUT"])
def update_image_by_id(id):
    return update_image_service(id)