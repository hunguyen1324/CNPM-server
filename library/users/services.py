from library.extension import db
from library.library_ma import UserSchema
from flask import request, jsonify, json,session
from library.model import Users
from werkzeug.security import check_password_hash,generate_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt, unset_jwt_cookies
import bcrypt
users_schema = UserSchema(many=True)
user_schema = UserSchema()

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def register():
    data = request.json
    email = data['email']
    password = data['password']
    username = data['username']
    address = data['address']
    phone = data['phone']
    if not email or not password or not username: 
        return {'message': 'email, password, username are required'}, 400
    
    # Kiểm tra xem email đã tồn tại chưa
    user = Users.query.filter_by(email=email).first()
    if user: 
        return {'message': 'email already exists'}, 400
    
    # Mã hóa mật khẩu
    hashed_password = hash_password(password)

    # Tạo đối tượng user mới với mật khẩu đã mã hóa
    user = Users(email=email, username=username, password=hashed_password, address=address, phone=phone)

    # Lưu đối tượng user vào database
    db.session.add(user)
    db.session.commit()
    return {'message': 'user created successfully'}

def check_password(hashed_password, password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return {'message': 'email and password are required'}, 400

    user = Users.query.filter_by(email=email).first()

    if not user:
        return {'message': 'invalid email or password'}, 401
    if not check_password(user.password.encode('utf-8'), password):
        return {'message': 'invalid email or password'}, 401
    login_method = data.get('login_method', 'token')
    
    if login_method == 'token':
        # Tạo JWT token
        access_token = create_access_token(identity=user.id)
        return {'username': user.username ,'password':user.password,'id':user.id,'address':user.address,
                'phone':user.phone, 'access_token': access_token}, 200
    elif login_method == 'session':
        session['id'] = user.id
        session['username'] = user.username
        return {'message': user.username + '  Login success'}, 200
    else:
        return {'message': 'Invalid login method'}, 400


def logout():
    if 'username' in session and 'id' in session :
        username = session['username']
        session.pop('id',None)
        session.pop('username',None)
        return {'message' : username + 'logged out successfully'}
    return {'message' : 'you are not login'}




def add_user_service():
    data = request.json
    if(('email' in data) and ('username' in data) and('password' in data)):
        email = data['email']
        username = data['username']
        password = data['password']
        phone =data['phone']
        address=data['address']

        try :
            new_user = Users(email,username,password,phone,address)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"message" : "Add sucess!"}),200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message " : "Cannot add user"}),400
    else :
        return jsonify({"message" : "Request error"}),400    

def get_all_users_service():
    users = Users.query.all()
    if users:
        return users_schema.jsonify(users)
    else : 
        return jsonify({"message": "Not found users!"})

def get_user_by_id_service(id):
    user = Users.query.get(id)
    if user : 
        return user_schema.jsonify(user)
    else: 
        return jsonify({"message": "Not found user"}),


def update_user_by_id_service(id):
    user = Users.query.get(id)
    data = request.json
    if user:
        if data and "password" in data and "username" in data :
            try:
                user.username = data["username"]
                user.password = data["password"]
                user.phone =data["phone"]
                user.address=data["address"]
                db.session.commit()
                return "user Updated"
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Can not delete book!"}), 400
    else:
        return "Not found user"
def delete_User_data_by_id_service(id):
    price = Users.query.get(id)
    if price:
        try:
            db.session.delete(price)
            db.session.commit()
            return jsonify({"message": "User deleted successfully"})
        except Exception as e:
            db.session.rollback()
            return jsonify({"message": "Cannot delete User!", "error": str(e)}), 400
    else:
        return jsonify({"message": "Not found User!"}), 404