import time



class PasswordTooShortError(Exception):
    pass
class MissingDigitError(Exception):
    pass
class SecurityPolicy:

    def __init__(self):
        self.failed_attempts ={}
        self.MAX_ATTEMPTS =5

    def record_failed_attempt(self,username):
        self.failed_attempts[username] = self.failed_attempts.get(username,0)+1
    def should_lockout(self,username):
        if self.failed_attempts.get(username,0)>=self.MAX_ATTEMPTS:
            time.sleep(180)
            return True

        else:
            return False
    def reset_attempts(self,username):
        self.failed_attempts[username]=0



    def is_password_strong(self,password):
        if len(password) <8:
            raise PasswordTooShortError("Password must be at least 8 character long.")
        if not any(c.isdigit() for c in password):
            raise MissingDigitError("Password must contain at least one number.")
        return True





