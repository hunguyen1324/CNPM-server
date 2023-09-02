from library.extension import db
from library.library_ma import CustomerSchema
from library.model import Customer_data
from flask import request, jsonify, json

total_schema = CustomerSchema()
Customers_schema = CustomerSchema(many=True)

def add_Customer_data_service():
    data = request.json
    if (('phone_ct' in data)and('email_ct' in data)and('user_ct' in data)
        and('mess_ct' in data)and('address_ct' in data)):
        phone_ct = data['phone_ct']
        email_ct = data['email_ct']
        user_ct  = data['user_ct']
        mess_ct = data['mess_ct']
        address_ct=data['address_ct']

        try:
            new_Customer_data = Customer_data(phone_ct,email_ct,user_ct,mess_ct,address_ct)
            db.session.add(new_Customer_data)
            db.session.commit()
            return jsonify({"message": "Add success!"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"message": "Cannot add data", "error": str(e)}), 400
    else:
        return jsonify({"message": "Request error1"}), 400
  

def get_all_Customer_data_service():
    totals_data = Customer_data.query.all()
    if totals_data:
        return Customers_schema.jsonify(totals_data)
    else : 
        return jsonify({"message": "Not found sensors_data!"})
    
def update_Customer_data_by_id_service(id):
    price = Customer_data.query.get(id)
    if price:
        data = request.json
        if( data and ("phone_ct" in data)and('email_ct' in data)and('user_ct' in data)and
           ('mess_ct' in data)and('address_ct' in data)):
            try:
                price.phone_ct = data['phone_ct']
                price.email_ct = data['email_ct']
                price.user_ct  = data['user_ct']
                price.mess_ct = data['mess_ct']
                price.address_ct=data['address_ct']
                db.session.commit()
                return jsonify({"message": "Customer updated successfully"})
            except Exception as e:
                db.session.rollback()
                return jsonify({"message": "Cannot update Customer!", "error": str(e)}), 400
    else:
        return jsonify({"message": "Not found Customer!"}), 404
    
def delete_Customer_data_by_id_service(id):
    price = Customer_data.query.get(id)
    if price:
        try:
            db.session.delete(price)
            db.session.commit()
            return jsonify({"message": "Customer deleted successfully"})
        except Exception as e:
            db.session.rollback()
            return jsonify({"message": "Cannot delete Customer!", "error": str(e)}), 400
    else:
        return jsonify({"message": "Not found Customer!"}), 404



