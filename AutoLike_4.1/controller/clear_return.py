

class ClearReturn:

    """
    this class clear the return files
    """

    def __init__(self, name_file):
        
        self.name_file = name_file


    def startClearReturn(self):

        name_file = self.name_file

        file = open(name_file, 'w')
        file.write('')
        file.close()