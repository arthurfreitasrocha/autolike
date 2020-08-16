

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


class FileAppender:

    """
    append files
    """

    def __init__(self, file_content, file_directory):
        
        self.__file_content = file_content
        self.__file_directory = file_directory


    def startFileAppender(self):

        file_content = self.__file_content
        file_directory = self.__file_directory

        file = open(file_directory, 'a')
        file.write(file_content)
        file.close()
