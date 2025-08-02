import flask_login
from sqlalchemy.ext.hybrid import hybrid_property
from project.db import *

class User(DATABASE.Model, flask_login.UserMixin):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    name = DATABASE.Column(DATABASE.String)
    surname = DATABASE.Column(DATABASE.String)
    password = DATABASE.Column(DATABASE.String)
    email = DATABASE.Column(DATABASE.String)

class Profile(DATABASE.Model):
    # IMAGE_UPLOAD_PATH = 
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    _image = DATABASE.Column(DATABASE.String)

    @hybrid_property
    def image(self):
        return self._image
    
    @image.setter
    def image(self, file):
        
        file += "123321"
        self._image = file