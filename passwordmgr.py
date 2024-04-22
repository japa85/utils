import pickle
import bcrypt

class PasswordDatabase:
    def __init__(self):
        
        self.data = dict()
    def register(self, user, password):
        if user in self.data:
          return False
        pwd_hash = self.hash_password(password)
        self.data[user] = pwd_hash
        return True
    def login(self, user, password):
        if user not in self.data:
          return False
        pwd_bytes = password.encode("utf-8")
        return bcrypt.checkpw(pwd_bytes, self.data[user])
    def hash_password(self, password):
        pwd_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(pwd_bytes, salt)
    






if __name__ == "__main__":
   
    db = PasswordDatabase()
    print("Registering users")
    print(db.register("john", "password"))
    print(db.register("Seth", "HelloWorld"))
    print(db.register("john", "myname"))
    print("Login")
    print(db.login("abc", "password"))
    print(db.login("john", "pwd"))
    print(db.login("john", "password"))

    file = open('passwordDb', 'wb')
    pickle.dump(db, file)

