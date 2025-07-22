import json

from passwordhasher import PasswordHasher
from securitypolicy import SecurityPolicy


class UserManager:
    def __init__(self,file,hasher,policy):
        self.file = file
        self.hasher = hasher
        self.policy = policy



    def register_user(self,username,password):
        data = self.load_data()
        if username in data:
            return False
        hashed_pw= self.hasher.hash_password(password)
        data[username] = hashed_pw.decode()
        self.save_data(data)
        return True




    def validate_user(self,username,password):
        data = self.load_data()
        if self.policy.should_lockout(username):
            return False

        if username in data:
             stored_hash = data[username]
        else:
            return False




        return self.hasher.check_password(password,stored_hash)

    def load_data(self):
       try:
            with open(self.file, "r") as f:
              data = json.load(f)
              return data

       except FileNotFoundError:
           return {}

    def save_data(self,data):
        try:
            with open(self.file,"w") as f:
                json.dump(data,f,indent=4)
                return True
        except Exception:
            return False



