# CONTROLLER
from controller.file_manipulator import FileWriter

class ClearReturn:

    """
    this class clear the return files
    """

    def __init__(self, name_file):
        
        self.__name_file = name_file


    def startClearReturn(self):

        file_directory = self.__name_file
        file_content = ''

        file_writer = FileWriter(file_content, file_directory)
        file_writer.startFileWriter()