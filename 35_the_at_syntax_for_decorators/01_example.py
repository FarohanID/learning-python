import functools

user = {"username": "jose", "access_level": "admin"} # admin / guest

def make_secure(func): # make_secure is the decorator function
    @functools.wraps(func)
    def secure_function():
        if user ["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}."
    return secure_function

@make_secure
def get_admin_password():
    return "admin:1234"

print(get_admin_password())