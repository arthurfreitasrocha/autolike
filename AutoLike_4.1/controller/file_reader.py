

class FileReader:

    """
    read files
    """

    def __init__(self, file_directory):
        
        self.__file_directory = file_directory


    def startFileReader(self):

        file_directory = self.__file_directory

        file = open(file_directory, 'r')
        file_content = file.read()
        file.close()

        return file_content
