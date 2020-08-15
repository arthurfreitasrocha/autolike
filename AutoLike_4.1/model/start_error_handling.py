

class ErrorHandling:

    def __init__(self, **kws):


        """
        this class verify if the information writted by the user is valid
        """

        " EMAIL "
        self.__login_entry = kws.get('login_entry')
        self.__password_entry = kws.get('password_entry')

        " OPTION ONE "
        self.__hashtag_entry = kws.get('hashtag_entry')
        self.__n_likes_entry = kws.get('n_likes_entry')

        "OPTION TWO "
        self.__users_selected = kws.get('users_selected')
        self.__kind_likes = kws.get('kind_likes')
        self.__send_entry = kws.get('send_entry')


    def startOptionTwoErrorHandling(self):

        " this method verify if the information what the user writted (in Option Two window) is valid "

        " INSTANCES THE VARIABLES WHICH WILL BE USED TO "
        users_selected = self.__users_selected
        kind_likes = self.__kind_likes
        send_entry = self.__send_entry
        validation = [False, False, False] #users_selected, kind_likes, send_entry

        " VALIDATES THE ENTRY AND THE KIND OF LIKES OPTION "
        if users_selected == '' or send_entry == '':
            
            if users_selected != '':
                validation[0] = True

            if kind_likes > 0 and kind_likes < 3:
                validation[1] = True

        else:

            if users_selected != '':
                validation[0] = True

            if kind_likes > 0 and kind_likes < 3:
                validation[1] = True

            if send_entry.isnumeric() == True:
                validation[2] = True

        return validation


    def startOptionOneErrorHandling(self):

        " this method verify if the information what the user writted (in Option One window) is valid "

        " INSTANCES THE VARIABLES WHICH WILL BE USED TO "
        hashtag_entry = self.__hashtag_entry
        n_likes_entry = self.__n_likes_entry
        validation = [False, False]

        " VERIFY IF THE INSTAGRAM HASHTAG AND THE NUMBER OF PHOTOS ARE VALID "
        if hashtag_entry == '' or n_likes_entry == '':

            return False

        else:
            
            " VALIDATES THE HASHTAG "
            if len(hashtag_entry) < 4:

                validation[0] = False

            else:

                if hashtag_entry[0] == '#':

                    validation[0] = True

            " VALIDATES THE Nº OF LIKES "
            if n_likes_entry.isnumeric() == False:

                validation[1] = False

            else:

                n_likes_entry = int(n_likes_entry)

                if n_likes_entry < 1:

                    validation[1] = False

                else:

                    validation[1] = True


            " RETURNS THE RESULT OF THE VALIDATION"
            if validation[0] == True and validation[1] == True:
                return True

            else:
                return False



    def startEmailErrorHandling(self):

        " this method verify if the information what the user writted (in Email window) is valid "

        " INSTANCES THE VARIABLES WHICH WILL BE USED TO "
        login_entry = self.__login_entry
        password_entry = self.__password_entry

        " VERIFY IF THE INSTAGRAM LOGIN AND PASSWORD IS VALID "
        if login_entry == '' or password_entry == '':

            return False

        else:

            " VALIDATES THE PASSWORD"
            n_password_characters = len(password_entry)

            if n_password_characters < 6:

                return False

            else:

                return True

