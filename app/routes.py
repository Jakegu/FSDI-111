from flask import Flask # From the flask module import the Flask class


app = Flask(__name__)   # Creates an instance of the Flask class
                        
                        # Class terminology:
                        # A method is a function that belongs to class
                        # An attribute is a variable that belongs to a class

@app.get("/")           # Flask decorator that maps view functions to routes
def about_me():         # Our view function
    me = {              # Pyhton dictionary
        "first_name": "Jake",
        "last_name": "Gulotta",
        "hobbies": "Music",
        "is_active": True
    }
    return me           # Return statement (returned to caller)