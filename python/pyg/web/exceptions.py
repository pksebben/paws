import logging

class PawsException(Exception):
    pass

class AuthError(PawsException):
    pass
    
class PasswordError(AuthError):
    """might want to log # attempts here, but probably unnecessary"""
    pass

class UserNotFoundError(AuthError):
    pass

