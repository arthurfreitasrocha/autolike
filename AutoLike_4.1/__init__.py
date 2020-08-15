# MODEL
from model.bot_verify_instagram_user import VerifyInstagramUser

from model.start_autolike import StartAutoLike
from model.start_error_handling import ErrorHandling


# VIEW
from view.email import Email
from view.EmailFragments import *

from view.LogoFragment import LogoFragment

from view.main_menu import MainMenu
from view.MainMenuFragments import *

from view.Message import Message

from view.option_one import OptionOne
from view.OptionOneFragments import OptionOneFragments

from view.WindowConfiguration import WindowConfiguration


# CONTROLLER
from controller.clear_return import ClearReturn

from controller.file_reader import FileReader
from controller.file_writer import FileWriter

from controller.start_database import StartDatabase

from controller.user_information import *

from controller.verify_user import VerifyUser

start = StartAutoLike()
start.startInterface()