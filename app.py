# Import Dependencies
from flask import Flask
# Create App
app = Flask(__name__)
#Create flask routes
@app.route('/')
def hello_world(): 
    return 'Hello world'