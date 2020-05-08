import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get('MONGODB_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGODB_URI')

mongo = PyMongo(app)

# Main Page ####################################################################
@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", movies=mongo.db.movies.find(), actors=mongo.db.actors.find())


# Movie Pages ##################################################################
## Movies list
@app.route('/movies')
def list_movies():
    return render_template("movies/movies.html", movies=mongo.db.movies.find())

## Add movie functions
@app.route('/add_movie')
def add_movie():
    return render_template('movies/createmovie.html')

@app.route('/insert_movie', methods=['POST'])
def insert_movie():
    moviesDB = mongo.db.movies
    movie = request.form.to_dict()
    movie.update({'meta':{'date_updated':datetime.utcnow(), 'date_created':datetime.utcnow()}})
    #validation goes here
    moviesDB.insert_one(movie)
    return redirect(url_for('list_movies'))

## Edit movie functions
@app.route('/edit_movie/<movie_id>')
def edit_movie(movie_id):
    the_movie = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    all_categories = mongo.db.categories.find()
    return render_template('movies/editmovie.html', movie=the_movie, categories=all_categories)

@app.route('/update_movie/<movie_id>', methods=['POST'])
def update_movie(movie_id):
    moviesDB = mongo.db.movies
    moviesDB.update_one( {'_id': ObjectId(movie_id)},
    {"$set":{
        'movie_name': request.form.get('movie_name'),
        'art': request.form.get('art'),
        'released': int(request.form.get('released')),
        'genre': request.form.get('genre'),
        'runtime':int(request.form.get('runtime')),
        'rating':request.form.get('rating'),
        'director':request.form.get('director'),
        'plot':request.form.get('plot'),
        'meta.date_updated':datetime.utcnow()
    }})
    return redirect(url_for('view_movie', movie_id=movie_id))

## View Movie
@app.route('/view_movie/<movie_id>')
def view_movie(movie_id):
    movie_details = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    return render_template('movies/viewmovie.html', movie=movie_details)


# Validation Functions #########################################################
def validate_movie(movie):
    return True

# Misc #########################################################################
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=os.environ.get('APPDEBUG') == 'true')
