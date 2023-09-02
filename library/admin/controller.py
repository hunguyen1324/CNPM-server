from flask import Blueprint
from .services import (add_admin_service,get_all_admin_service,get_admin_by_id_service,update_admin_by_id_service,login,logout,register)

admin = Blueprint("admin",__name__)



@admin.route("/admin/login",methods = ['Post'])
def login_admin():
    return login()

@admin.route("/admin/logout", methods = ['GET'])
def logout_admin():
    return logout()

@admin.route("/admin/register",methods = ["POST"])
def add_admin():
    return register()

@admin.route("/admin/all",methods = ["GET"])
def get_all_admin():
    return get_all_admin_service()

@admin.route("/admin/<int:id>",methods = ["GET"])
def get_admin_by_email(id):
    return get_admin_by_id_service(id)

@admin.route("/admin/<int:id>",methods =["PUT"])
def update_admin_by_id(id):
    return update_admin_by_id_service(id)