import sys,os

# we are customizing this func so that here it will give which file, which line and what error we are getting and we can debug easily 
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message



# creating exe as senson exe as this is sensor project and inheriting Exception class
class SensorException(Exception):

    # taking error msg and error details as arguments
    def __init__(self,error_message, error_detail:sys):
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message