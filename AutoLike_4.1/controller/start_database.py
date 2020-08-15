

class StartDatabase:

    """
    this class start the database
    """
    def __init__(self):

        pass


    def readDatabase(self):

        keys = ['app_version', 'user_instagram']

        variables = {}
        variables['app_version'] = ''
        variables['user_instagram'] = ''
        
        i = 0
        while(i < len(keys)):

            directory = f'controller/system_files/{keys[i]}.txt'

            file = open(directory, 'r')
            variables[keys[i]] = file.read()
            file.close()

            i += 1

        return variables
