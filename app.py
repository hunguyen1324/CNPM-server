from flask import Flask
from library.extension import db
from flask_mysqldb import MySQL
#from library.model import Users,Sensor_data,Mobileapp_data,Log_data
from library.users.controller import users
from library.admin.controller import admin
from library.total_price.controller import totals_data
from library.feedback.controller import feedbacks_data
from library.customer.controller import Customers_data
from library.images.controller import images
# from library.sensor_data.controller import sensors_data
from flask_jwt_extended import JWTManager
from flask_cors import CORS
app =Flask(__name__) 


mysql = MySQL(app)
jwt = JWTManager(app)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/cnpm'
app.config['SECRET_KEY'] = 'my-secret-key'
app.config['JWT_SECRET_KEY'] = 'my-jwt-secret-key'
db.init_app(app)
with app.app_context():
    db.create_all()
    print("Created DB")

@app.route("/home", methods = ["GET"])
def create_app():
    return "APP created !"


if __name__ == "__main__":
    app.register_blueprint(images)
    app.register_blueprint(users)
    app.register_blueprint(admin)
    app.register_blueprint(totals_data)
    app.register_blueprint(feedbacks_data)
    app.register_blueprint(Customers_data)
    # app.register_blueprint(sensors_data)
    app.run(debug= True)