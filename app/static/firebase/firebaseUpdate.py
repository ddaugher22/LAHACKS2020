import pyrebase
import os
from os import path
import sys

#lahacks2020-1e92d

config = {
  "apiKey": "AIzaSyCmyN_FLXHNj73sNdY-uI0NfX9LIbu9C_Y",
  "authDomain": "lahacks2020-1e92d.firebaseapp.com",
  "databaseURL": "https://lahacks2020-1e92d.firebaseio.com",
  "storageBucket": "lahacks2020-1e92d.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()



def addSuggestionFile(category, filename):

    if not os.path.exists(filename):
        print("File %s filename does not exist"%filename)
        return

    file = open(filename, 'r')

    for suggestion in file.readlines():
        addSuggestion(category, suggestion.strip())

    file.close()

def addSuggestion(category, suggestion):
    global db
    db.child("categories").child(category).push(suggestion)
    
def Main():
    if (len(sys.argv)) < 3:
        print("Please provide category and text file")
        sys.exit()

    category, filename = sys.argv[1], sys.argv[2]

    addSuggestionFile(category, filename)

if __name__ == "__main__":
    Main()
    

    