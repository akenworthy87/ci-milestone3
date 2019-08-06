import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'ifdb'
#Change this to an enviro-var
app.config["MONGO_URI"] = 'mongodb+srv://root:{}@ci-datacentricpy-e8zwz.mongodb.net/ifdb?retryWrites=true&w=majority'.format('r00tUser') 

mongo = PyMongo(app)

# Main Page
@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", movies=mongo.db.movies.find(), actors=mongo.db.actors.find())

# Movie Pages
@app.route('/movies')
def list_movies():
    return render_template("movies/movies.html", movies=mongo.db.movies.find())

@app.route('/view_movie/<movie_id>')
def view_movie(movie_id):
    movie_details = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    return render_template('movies/viewmovie.html', movie=movie_details)

#Actor Pages
@app.route('/actors')
def list_actors():
    return render_template("actors/actors.html", actors=mongo.db.actors.find())

@app.route('/view_actor/<actor_id>')
def view_actor(actor_id):
    actor_details = mongo.db.actors.find_one({"_id": ObjectId(actor_id)})
    return render_template('actors/viewactor.html', actor=actor_details)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
