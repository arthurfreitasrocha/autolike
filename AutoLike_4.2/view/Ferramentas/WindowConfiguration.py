

class WindowConfiguration:

    """ 
    this class returns the window configuration 
    based in the arguments passed by the user

    ACCEPTED ARGUMENTS:

    window - the window of the widget

    width - the width of the widget

    height - the height of the widget

    width_distance - the width_distance of the widget

    height_distance - the height_distance of the widget

    """
    def __init__(self, window, width, height, **kws):
        
        " constructor "

        self.__window = window
        self.__top_window = kws.get('top_window')
        self.__width = width
        self.__height = height
        self.__width_distance = kws.get('width_distance')
        self.__height_distance = kws.get('height_distance')


    def fullWindowConfiguration(self):

        " this method is used to create the window master "

        " INSTANCES "
        window = self.__window
        width = self.__width
        height = self.__height
        width_distance = self.__width_distance
        height_distance = self.__height_distance

        " CREATE THE WINDOW GEOMETRY OF THE APPLICATION "
        
        " CATCH THE DIMENSION OF THE MONITOR " 
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        " CALCULATE THE RESPONSIVENESS "
        final_width_distance = int(screen_width/width_distance)
        final_height_distance = int(screen_height/height_distance)

        " FINALLY, THE 'window_geometry' VARIABLE IS CREATED "
        " THE 'window_geometry' VARIABLE IS USED TO INFORM "
        " THE USER OF THE FINAL WINDOW GEOMETRY "
        window_geometry = f'{width}x{height}+{final_width_distance}+{final_height_distance}'

        " RETURN A DICT CONTAINING THE FULL WINDOW CONFIGURATION "
        full_window_configuration = {}
        full_window_configuration['window_geometry'] = window_geometry

        return full_window_configuration