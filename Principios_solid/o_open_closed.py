"""
    OPEN-CLOSED:
        Software entities … should be open for extension 
        but closed for modification
"""
from abc import ABC, abstractmethod

# Abstract Class
class Logger(ABC):
    @abstractmethod
    def log(self, message, code):
        pass

""" 
    WITH THIS, WE MAKE AN ABSTRAC CLASS OPEN TOO YOUR
    EXTENSION BUT CANNOT BE MODIFIED.
"""

# Inherited Classes
class FileLogger(Logger):
    def log(self,message,code):
        with open('files/log.txt', 'w', newline='',encoding='utf-8') as file:
            file.write(f'{code}: {message} \n')

class DatabaseLogger(Logger):
    def log(self, message, code):
        # logic about generate logs in a Data Base
        print(f"{code}: {message} \n")

if __name__ == '__main__':
    loggers = [FileLogger(),DatabaseLogger()]
    
    for logger in loggers:
        logger.log("this is a log","info")
