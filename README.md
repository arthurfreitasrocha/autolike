# autolike

====== NEW UPDATE v4.1.0 ======

 What's new?
 - Now all the project uses the MVC software design pattern.
 - All the project now is translated to english.
 - Now all the project have comments in english, but some comments are out of date. Son I will update it.
 - Some buttons won externaly update
 - All the code is refactored with principles of Clean Code to improve the reading and understanding.
 - Consenquentely, the AutoLike now is more fast than before.
 
 
 - Button 'Switch Instagram Email' updated.
 - - Now when you click at 'Switch Instagram Email' button, you can show and hide your password clicking at the "eye".
 
 - Button 'Like photos of an specific Instagram profile' updated.
 - - Now you can comment the posts you have been liked. But just one post by profile. To use this option, click at 'Show/Hide Text' checkbutton, and will open a text widget what you can write your comment.
 
 - Button 'Send message in Direct' abandoned.
 - - I tried to implement this function but the Instagram don't have a option to send Messages to people what I not follow. So, I abandoned this function. The function is still avaible in menu but she don't do nothing.

 - Bug Fix
    
====== NEW UPDATE v4.1.0 =====

|

====== INTRODUCTION & HOW TO USE ======

A simple robot that can be like a number of photos in Instagram (and more)

Steps to run

- 01º Install Python
- 02º Install Selenium (A Python Library)
- 03º Have fun!

How to Install?

- First download Python entering in this link: https://www.python.org/downloads/.
- After download it, install Python. Don't forget to mark the "Add Python 3.x to PATH" checkbutton in the installation box (You need to mark it to all commands run ok in the CMD).
- After installing Python, you have to install Selenium. To do it open a CMD and write: pip install selenium. Please wait until the installation finish.
- After all this steps, you can start AutoLike. Enter in the AutoLike's folder and open the "__init__.py" file. This file will load all the requirements of AutoLike and start him.


How to Use?

To use AutoLike first you need to make login into Instagram. Do it clicking in 'Switch Instagram Email' button. After do it, select one option and have fun.

Options:
- 01 'Like photos using a hashtag'
- 02 'Curtir Fotos de um perfil Específico'
- 03 'Curtir Fotos e Enviar Mensagens no Direct'

01 - This function search the profiles based in the hashtag informed by the user. After, AutoLike access the Instagram publications which haves the hashtag and likes 'x' number of photos (you informs the number of photos). The name of the profiles was liked, will be saved in the DB (DataBase) to be used in the second option.
02 - This function work based on the DB acquired with option 01. The user selects 'n' users from the DB and informs what number of photos will be liked in each profile. Son, the AutoLike access profile by profile and likes a 'x' number of photos by the current profile (Test the option, you will understand better).
03 - Abandoned.

====== INTRODUCTION & HOW TO USE ======

|

====== THANKS & COPYRIGHT ======

Thanks to:
- Arthur Freitas Rocha to colaborat in the AutoLike's project

All the rights and contents is reserved to Arthur Freitas Rocha. Don't buy and don't sell. You are free to use the program just for personal use. If you are creating content using AutoLike, please credit Arthur Freitas Rocha during the content or in the description.

====== THANKS & COPYRIGHT ======
