import bcrypt
class PasswordHasher:

    def hash_password(self,password):
        encoded_password= password.encode()
        salt= bcrypt.gensalt()
        return bcrypt.hashpw(encoded_password,salt)


    def check_password(self,stored_password,password):
        try:
             return bcrypt.checkpw(password.encode(),stored_password.encode())
        except(TypeError,ValueError):
            return False





