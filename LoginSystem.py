from usermanager import UserManager
from passwordhasher import PasswordHasher
from securitypolicy import SecurityPolicy
#importlogger
hasher = PasswordHasher()
policy = SecurityPolicy()
manager = UserManager("usernames.json", hasher, policy)

print("Welcome To The Login Page")

while True:
    try:
        options = int(input('1.Register\n2.Login\n3.Quit\n:'))
    except ValueError:
        print('Invalid option, please pick a number between 1-3')
        continue
    if options ==1:
        user = input("Enter Your Username:")
        passw = input("Enter Your Password:")
        manager.register_user(user,passw)
    elif options==2:
        user = input("Enter Your Username:")
        passw = input("Enter Your Password:")
        manager.validate_user(user,passw)
    elif options==3:
        break
    else:
        print('Invalid option, please pick a number between 1-3')




