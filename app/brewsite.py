from flask import Flask
from flask import render_template as rt
import requests, json, warnings # type: ignore
response = requests.get("https://api.openbrewerydb.org/v1/breweries")

data = json.loads(response.content)

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return rt("home.html", user = "Naruto Uzumaki")

@app.route("/breweries")
def breweries():
    return rt("breweries.html", content = data)

@app.route("/beer_type")
def beer_type():
    return rt("beer_types.html", user = "Naruto Uzumaki")

@app.route("/about")
def about():
    return rt("about.html", user = "Naruto Uzumaki")

if __name__ == "__main__":
    app.run(debug=True)