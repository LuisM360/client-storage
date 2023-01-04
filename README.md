# Client Storage
A tkinter gui created in python to store client name, address, and amount. Once you submit the information it will be
added to a sqlite3 database for long term use.

## How It's Made:

**Tech used:** Python, Tkinter, Sqlite3

A Tkinter gui writen with classes to help organize the code. When opening the
application it will prompt you to enter the client information and then hit the
submit button. The application will then add it to a local sqlite database.

## Optimizations
I plan to connect the application to the cloud as right now it only has local storage.
As well as introducing the MVC pattern and making my application asynchronous.
