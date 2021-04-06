from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


@app.route("/")
def index():
    # connect to database and read data
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    # connect to database
    mars = mongo.db.mars
    # call the scrape all function
    data = scrape_mars.scrape_all()
    # update database
    mars.update({}, data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run()
