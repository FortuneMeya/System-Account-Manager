import json
import logging
from json import JSONDecodeError


class UserManager:
    def __init__(self,file,hasher,policy):
        self.file = file
        self.hasher = hasher
        self.policy = policy



    def register_user(self,username,password):
        data = self.load_data()
        if username in data:
            return False
        self.policy.is_password_strong(password)
        hashed_pw= self.hasher.hash_password(password)
        data[username] = hashed_pw.decode()
        self.save_data(data)
        logging.info(f"User registered: {username}")
        return True




    def validate_user(self, username, password):
        data = self.load_data()
        if self.policy.should_lockout(username):
            logging.warning(f"User locked out: {username}")
            return False
        if username not in data:
            return False
        stored_hash = data[username]
        if not self.hasher.check_password(password, stored_hash):
            self.policy.record_failed_attempt(username)
            logging.warning(f"Failed login attempt for user: {username}")
            return False
        self.policy.reset_attempts(username)
        logging.info(f"User logged in: {username}")
        return True

    def load_data(self):
       try:
            with open(self.file, "r") as f:
              data = json.load(f)
              return data

       except FileNotFoundError:
           return {}
       except JSONDecodeError:
           return {}

    def save_data(self,data):
        try:
            with open(self.file,"w") as f:
                json.dump(data,f,indent=4)
                return True
        except Exception:
            return False



