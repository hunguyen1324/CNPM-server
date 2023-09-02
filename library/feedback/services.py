from library.extension import db
from library.library_ma import FeedbackSchema
from library.model import Feedback_data
from flask import request, jsonify, json

total_schema = FeedbackSchema()
feedbacks_schema = FeedbackSchema(many=True)

def add_feedback_data_service():
    data = request.json
    if (('phone_fb' in data)and('email_fb' in data)and('user_fb' in data)and('mess_fb' in data)):
        phone_fb = data['phone_fb']
        email_fb = data['email_fb']
        user_fb  = data['user_fb']
        mess_fb = data['mess_fb']

        try:
            new_feedback_data = Feedback_data(phone_fb,email_fb,user_fb,mess_fb)
            db.session.add(new_feedback_data)
            db.session.commit()
            return jsonify({"message": "Add success!"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"message": "Cannot add data", "error": str(e)}), 400
    else:
        return jsonify({"message": "Request error"}), 400
  

def get_all_feedback_data_service():
    totals_data = Feedback_data.query.all()
    if totals_data:
        return feedbacks_schema.jsonify(totals_data)
    else : 
        return jsonify({"message": "Not found sensors_data!"})
    
def update_feedback_data_by_id_service(id):
    price = Feedback_data.query.get(id)
    if price:
        data = request.json
        if( data and ("phone_fb" in data)and('email_fb' in data)and('user_fb' in data)and('mess_fb' in data)):
            try:
                price.phone_fb = data['phone_fb']
                price.email_fb = data['email_fb']
                price.user_fb  = data['user_fb']
                price.mess_fb = data['mess_fb']
                db.session.commit()
                return jsonify({"message": "Feedback updated successfully"})
            except Exception as e:
                db.session.rollback()
                return jsonify({"message": "Cannot update Feedback!", "error": str(e)}), 400
    else:
        return jsonify({"message": "Not found Feedback!"}), 404
    
def delete_feedback_data_by_id_service(id):
    price = Feedback_data.query.get(id)
    if price:
        try:
            db.session.delete(price)
            db.session.commit()
            return jsonify({"message": "Feedback deleted successfully"})
        except Exception as e:
            db.session.rollback()
            return jsonify({"message": "Cannot delete feedback!", "error": str(e)}), 400
    else:
        return jsonify({"message": "Not found feedback!"}), 404



