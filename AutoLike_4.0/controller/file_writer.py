

class FileWriter:

    """
    write files
    """

    def __init__(self, file_content, file_directory):
        
        self.__file_content = file_content
        self.__file_directory = file_directory


    def startFileWriter(self):

        file_content = self.__file_content
        file_directory = self.__file_directory

        file = open(file_directory, 'w')
        file.write(file_content)
        file.close()
