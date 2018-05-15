# Dependencies
from flask import Flask, jsonify, render_template, redirect
#import pymongo
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app)

@app.route("/")
def index():
    mars_info = db.mars.find_one()

    return render_template("index.html", mars_info=mars_info)

@app.route("/scrape")
def scrape():
    mars_info = db.mars
    mars_data = scrape_mars.Scrape()
    mars_info.update(
        {},
        mars_data,
        upsert = True
    )

    return redirect("http://localhost:5000/", code=302)

    
if __name__ == "__main__":
    app.run(debug=False)