from library.extension import db
from library.library_ma import AdminSchema
from flask import request, jsonify, json,session
from library.model import Admin
from werkzeug.security import check_password_hash,generate_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt, unset_jwt_cookies

admins_schema = AdminSchema(many=True)
admin_schema = AdminSchema()



def register():
    data = request.json
    email = data['email']
    password = data['password']
    adminname = data['adminname']
    if not email or not password or not adminname: 
        return {'message' : 'email,password,adminname are required'},400
    
    admin = Admin.query.filter_by(email = email ).first()

    if admin : 
        return {'message' : 'email already exits'},400
    
  #  password_hash = generate_password_hash(password)
    admin = Admin(email=email,adminname = adminname,password=password)

    db.session.add(admin)
    db.session.commit()
    return{'message' : 'admin created successfully'}




# def login():
#     data = request.json
#     email = data.get('email')
#     password = data.get('password')
#     if not email or not password:
#         return {'message': 'email and password are required'}, 400

#     admin = Admin.query.filter_by(email=email).first()

#     if not admin:
#         return {'message': 'invalid email or password'}, 401

#     passhash = generate_password_hash(admin.password)
#     if not check_password_hash(passhash, password):
#         return {'message': 'invalid email or password'}, 401

#     session['id'] = admin.id
#     session['adminname'] = admin.adminname
#     # access_token = create_access_token(identity=admin.id)
#     return {'message': admin.adminname + '  Login success '}, 200

def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return {'message': 'email and password are required'}, 400

    admin = Admin.query.filter_by(email=email).first()

    if not admin:
        return {'message': 'invalid email or password'}, 401

    passhash = generate_password_hash(admin.password)
    if not check_password_hash(passhash, password):
        return {'message': 'invalid email or password'}, 401

    login_method = data.get('login_method', 'token')
    
    if login_method == 'token':
        # Tạo JWT token
        access_token = create_access_token(identity=admin.id)
        return {'adminname': admin.adminname ,'password':admin.password,'id':admin.id, 'access_token': access_token}, 200
    elif login_method == 'session':
        session['id'] = admin.id
        session['adminname'] = admin.adminname
        return {'adminname': admin.adminname + '  Login success'}, 200
    else:
        return {'message': 'Invalid login method'}, 400

def logout():
    if 'adminname' in session and 'id' in session :
        adminname = session['adminname']
        session.pop('id',None)
        session.pop('adminname',None)
        return {'message' : adminname + 'logged out successfully'}
    return {'message' : 'you are not login'}




def add_admin_service():
    data = request.json
    if(('email' in data) and ('adminname' in data) and('password' in data)):
        email = data['email']
        adminname = data['adminname']
        password = data['password']

        try :
            new_admin = Admin(email,adminname,password)
            db.session.add(new_admin)
            db.session.commit()
            return jsonify({"message" : "Add sucess!"}),200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message " : "Cannot add admin"}),400
    else :
        return jsonify({"message" : "Request error"}),400    

def get_all_admin_service():
    admin = Admin.query.all()
    if admin:
        return admins_schema.jsonify(admin)
    else : 
        return jsonify({"message": "Not found admins!"})

def get_admin_by_id_service(id):
    admin = Admin.query.get(id)
    if admin : 
        return admin_schema.jsonify(admin)
    else: 
        return jsonify({"message": "Not found admin"}),


def update_admin_by_id_service(id):
    admin = Admin.query.get(id)
    data = request.json
    if admin:
        if data and "password" in data and "adminname" in data :
            try:
                admin.adminname = data["adminname"]
                admin.password = data["password"]
                db.session.commit()
                return "admin Updated"
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Can not delete book!"}), 400
    else:
        return "Not found admin"