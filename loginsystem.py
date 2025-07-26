from usermanager import UserManager
from passwordhasher import PasswordHasher
from securitypolicy import SecurityPolicy
import getpass


class LoginSystem:
    def __init__(self, system):
        self.system = system


hasher = PasswordHasher()
policy = SecurityPolicy()
manager = UserManager("usernames.json", hasher,policy)

print("\nWelcome To The Login Page\n")

while True:
    try:
        options = int(input('1.Register\n2.Login\n3.Quit\n:'))
    except ValueError:
        print('Invalid option, please pick a number between 1-3')
        continue
    if options ==1:
        user = input("Enter Your Username:").strip()
        passw = getpass.getpass("Enter Your Password(8 characters long with at least one digit):")

        if manager.register_user(user,passw):
            print("Account Successfully created")
        else:
            print("Username already exists")



    elif options==2:
        user = input("Enter Your Username:")
        passw = input("Enter Your Password:")
        if manager.validate_user(user,passw):
             print("Successfully logged in")
        else:
            print("Login failed. Check username and password")
    elif options==3:
        break
    else:
        print('Invalid option, please pick a number between 1-3')




