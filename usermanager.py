import json

import bcrypt

import passwordhasher
import securitypolicy
from passwordhasher import PasswordHasher


class UserManager:
    def __init__(self,file,hasher):
        self.file = file
        self.hasher= hasher


    def register_user(self,username,password):
        try:

             with open(self.file,"r") as f:
                 data=json.load(f)
        except FileNotFoundError:
            data= {}
        if username in data:
                return False
        hashed_pw= self.hasher.hash_password(password)
        data[username] = hashed_pw.decode()

        with open(self.file,"w") as f:
            json.dump(data,f,indent=4)

        return True

    def validate_user(self,username,password):
        try:
            with open(self.file,"r") as f:
                data=json.load(f)
        except FileNotFoundError:
            data={}

        if securitypolicy.SecurityPolicy.should_lockout(username):
            return False

        if username not in data:
            return False
        stored_hash = data[username]

        return passwordhasher.check_password(password,stored_hash)
