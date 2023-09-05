from library.extension import db
from flask_jwt_extended import get_jwt_identity
class Users(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(50),nullable = False)
    username = db.Column(db.String(100),nullable = False)
    password = db.Column(db.String(20),nullable = False) 
    address= db.Column(db.String(50),nullable = False)
    phone= db.Column(db.String(50),nullable = False)

    def __init__(self, email,username, password,address,phone):
        self.email = email    
        self.username = username
        self.password = password
        self.address = address
        self.phone =phone
# thêm address,phone
class Admin(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(50),nullable = False)
    adminname = db.Column(db.String(100),nullable = False)
    password = db.Column(db.String(20),nullable = False) 

    def __init__(self, email,adminname, password):
        self.email = email    
        self.adminname = adminname
        self.password = password

class Total_price(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    men_price = db.Column(db.Integer,nullable = False)
    women_price = db.Column(db.Integer,nullable = False)
    men_product = db.Column(db.Integer,nullable = False)
    women_product = db.Column(db.Integer,nullable = False)
    label = db.Column(db.String(50),nullable = False)

    def __init__(self,men_price,women_price,men_product,women_product,label):
        self.men_price =men_price
        self.women_price =women_price
        self.men_product =men_product
        self.women_product =women_product
        self.label=label 

class Feedback_data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    phone_fb = db.Column(db.String(50),nullable = False)
    email_fb = db.Column(db.String(50),nullable = False)
    user_fb = db.Column(db.String(50),nullable = False)
    mess_fb = db.Column(db.String(500),nullable = False)

    def __init__(self,phone_fb,email_fb,user_fb,mess_fb):
        self.phone_fb =phone_fb
        self.email_fb =email_fb
        self.user_fb =user_fb
        self.mess_fb =mess_fb       

class Customer_data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    phone_ct= db.Column(db.String(50),nullable = False)
    email_ct= db.Column(db.String(50),nullable = False)
    user_ct= db.Column(db.String(50),nullable = False)
    mess_ct= db.Column(db.String(500),nullable = False)
    address_ct= db.Column(db.String(50),nullable = False)
    # bỏ pass_ct

    def __init__(self,phone_ct,email_ct,user_ct,mess_ct,address_ct):
        self.phone_ct=phone_ct
        self.email_ct=email_ct
        self.user_ct=user_ct
        self.mess_ct=mess_ct
        self.address_ct = address_ct

class Image_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), nullable=False)
    img_hover_url = db.Column(db.String(255), nullable=False)   
    image_name = db.Column(db.String(255), nullable=False)
    type_name = db.Column(db.String(255), nullable=False)
    price_value = db.Column(db.Integer, nullable=False)

    def __init__(self, image_url, price_value, image_name, type_name,img_hover_url):
        self.image_url = image_url
        self.img_hover_url = img_hover_url
        self.price_value = price_value
        self.image_name = image_name
        self.type_name = type_name

        


