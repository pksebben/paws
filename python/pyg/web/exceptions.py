import logging

class PawsException(Exception):
    pass

class AuthError(PawsException):
    pass
    
class PasswordError(AuthError):
    pass

class UserNotFoundError(AuthError):
    pass
