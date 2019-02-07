# dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import pymongo
import scrape_mars

# create flask app
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'
# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)
# Declare db and collection. Will create one if not already available.
db = client.info
collection = db.info
 
# Create root/index route to query mongoDB and pass mars data to HTML template to display data
@app.route('/')
def index():
    # Find one record of data from the mongo database
    info = db.info.find_one() 
    # Return template and data
    return render_template('index.html', info=info)

# Create route to trigger scrape function
@app.route('/scrape')
def scrape():
    info = scrape_mars.scrape()
    db.info.update({}, info, upsert=True)
    return redirect('/', code=302)

if __name__ == '__main__':
    app.run(debug=True)