# Dependencies
from flask import Flask, jsonify, render_template
import pymongo
import scrape_mars

app = Flask(__name__)

mongo = pymongo(app)

@app.route("/")
def index():
    mars_info = db.mars.find_one()

return render_template("index.html", mars_info=mars_info)






if __name__ == "__main__":
    app.run(debug=False)