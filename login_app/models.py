import flask_login
from sqlalchemy.ext.hybrid import hybrid_property
from project.db import *
from project.settings import PROFILE_PATH
import os
import hashlib
from werkzeug.datastructures import FileStorage

class User(DATABASE.Model, flask_login.UserMixin):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    name = DATABASE.Column(DATABASE.String)
    surname = DATABASE.Column(DATABASE.String)
    password = DATABASE.Column(DATABASE.String)
    email = DATABASE.Column(DATABASE.String)

class Profile(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    _image = DATABASE.Column(DATABASE.String)

    @hybrid_property
    def image(self):
        profile_dir = os.path.basename(os.path.normpath(PROFILE_PATH))
        if isinstance(self._image, str):
            return os.path.join(profile_dir, self._image)
        return self._image
    
    @image.setter
    def image(self, file: FileStorage):
        random_salt = os.urandom(16)
        filename = file.filename.split(".")
        hash_name = hashlib.sha256(file.filename.encode() + random_salt)
        filename.insert(-1, hash_name.hexdigest())
        filename = ".".join(filename)
        file.save(os.path.join(PROFILE_PATH, filename))
        self._image = filename