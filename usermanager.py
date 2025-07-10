import json
class UserManager:
    def __init__(self,file):
        self.file = file


    def register_user(self,username,password,hasher):
        try:

             with open("usernames.json","r") as f:
                 data=json.load(f)
        except FileNotFoundError:
            data= {}
        if username in data:
                return False
        hashed_pw= hasher.hash_password(password)
        data[username] = hashed_pw.decode()

        with open(self.file,"w") as f:
            json.dump(data,f,indent=4)

        return True












