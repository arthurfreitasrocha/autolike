

class ClearUserPublications:

    def __init__(self, n_user_publications):

        " this class clear the number of publications what the instagram user has "

        self.__n_user_publications = n_user_publications


    def startClearUserPublications(self):

        " this method clear the number of publications what the instagram user has "

        " VARIABLE "
        n_user_publications = self.__n_user_publications

        " CLEAR THE NUMBER OF PUBLICATIONS WHAT THE INSTAGRAM USER HAS "
        clear_n_user_publications = ''
        for number in n_user_publications:

            if number != '.':
                clear_n_user_publications += number

        clear_n_user_publications = int(clear_n_user_publications)

        return clear_n_user_publications
