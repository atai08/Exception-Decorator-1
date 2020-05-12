
def decorator():
    def wrapper(*args):
        try:
            return func(*args)
        except:
            raise Exception("No password to change!")
    return wrapper

@decorator()
class User():
    def _init_(self):
        pass

    def change_password(self):
        pass


u = User()
u.change_password()
