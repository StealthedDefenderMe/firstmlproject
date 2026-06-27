#Here we're making the customer exception
import sys
from src.mlproject.logger import logging

def error_message_detail(error, error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename #Returns filename wherever exception occurs
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

# Creating a class of exception to inherit the exception
class CustomerException(Exception):
    # __init__ is a function that runs automatically when an object is created.
    def __init__(self, error_message, error_details:sys): #Initialisation constructor & sys to track error details
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details) #function which takes 2 parameters

    def __str__(self): #that tells Python: If someone prints my object, what text should be shown?"
        #When someone prints my exception, show the detailed error message instead of a weird object address.
        return self.error_message #Message coming form self.error returned here whenever we print it 