

class ErrorHandlingOptionOne:

    def __init__(self, hashtag_entry, n_likes_entry):
        
        self.__hashtag_entry = hashtag_entry
        self.__n_likes_entry = n_likes_entry


    def startErrorHandling(self):

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


class ErrorHandlingOptionTwo:

    def __init__(self, users_selected, n_photos, checkbutton_value):
        
        self.__users_selected = users_selected
        self.__n_photos = n_photos
        self.__checkbutton_value = checkbutton_value


    def startErrorHandling(self, **kws):

        " this method verify if the information what the user writted (in Option Two window) is valid "

        " INSTANCES THE VARIABLES "
        users_selected = self.__users_selected
        n_photos = self.__n_photos
        checkbutton_value = self.__checkbutton_value


        if checkbutton_value == 0:

            validation = [False, False]


            " VALIDATES IF THE USER SELECTED AT LEAST ONE INSTAGRAM PROFILE "
            if users_selected != '':
                validation[0] = True
            
            else:
                validation[0] = False

            " VALIDATES THE ENTRY AND THE KIND OF LIKES OPTION "
            if n_photos != '' and n_photos.isnumeric() == True:
                validation[1] = True

            else:
                validation[1] = False


            if validation[0] == True and validation[1] == True:
                return True
            
            else:
                return False


        elif checkbutton_value == 1:

            " INSTANCES THE WRITTED TEXT "
            writted_text = kws.get('writted_text')

            validation = [False, False, False]


            " VALIDATES IF THE USER SELECTED AT LEAST ONE INSTAGRAM PROFILE "
            if users_selected != '':
                validation[0] = True
            
            else:
                validation[0] = False

            " VALIDATES THE ENTRY AND THE KIND OF LIKES OPTION "
            if n_photos != '' and n_photos.isnumeric() == True:
                validation[1] = True

            else:
                validation[1] = False

            " VALIDATES THE TEXT WRITTED BY THE USER "
            if writted_text != '' and writted_text != '\n':
                validation[2] = True
            
            else:
                validation[2] = False


            if validation[0] == True and validation[1] == True and validation[2] == True:
                return True
            
            else:
                return False


class ErrorHandlingOptionThree:

    def __init__(self, users_selected, writted_text):
        
        self.__users_selected = users_selected
        self.__writted_text = writted_text


    def startErrorHandling(self):

        " this method verify if the typed information is valid "

        " INSTANCES THE VARIABLES "
        users_selected = self.__users_selected
        writted_text = self.__writted_text
        validation = [False, False]


        " VALIDATES IF THE USER SELECTED AT LEAST ONE INSTAGRAM PROFILE "
        if users_selected != '':
            validation[0] = True
        
        else:
            validation[0] = False

        if writted_text == '' or writted_text == '\n':
            validation[1] = False

        else:
            validation[1] = True


        if validation[0] == True and validation[1] == True:
            return True
        
        else:
            return False


class ErrorHandlingEmail:

    def __init__(self, login_entry, password_entry):
        
        self.__login_entry = login_entry
        self.__password_entry = password_entry


    def startErrorHandling(self):

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

