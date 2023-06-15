from functools import wraps

def interger_validator(func):  # sourcery skip: raise-specific-error
    #@wraps
    def wrapper(*args, **kwargs):
        types = [isinstance(element, int) for element in args]
        if False in types:
            raise Exception("TIPOS DIFRENTES A INTEGERS")
        return func(*args,**kwargs)
    return wrapper