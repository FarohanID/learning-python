import functools

user = {"username": "jose", "access_level": "admin"} # admin / guest

def make_secure(func): # make_secure is the decorator function
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user ["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}."
    return secure_function

@make_secure
def get_password(panel):
    if panel == "admin":
        return "admin: 1234"
    elif panel == "billing":
        return "super_secure_password"

print(get_password("billing"))