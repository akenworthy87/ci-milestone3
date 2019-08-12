import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'ifdb'
app.config["MONGO_URI"] = 'mongodb+srv://root:{}@ci-datacentricpy-e8zwz.mongodb.net/ifdb?retryWrites=true&w=majority'.format(os.environ.get('MONGODB_PASS')) 

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
    #validation goes here
    movies = mongo.db.movies
    movies.insert_one(request.form.to_dict())
    return redirect(url_for('list_movies'))

## Edit movie functions
@app.route('/edit_movie/<movie_id>')
def edit_movie(movie_id):
    the_movie = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    all_categories = mongo.db.categories.find()
    return render_template('movies/editmovie.html', movie=the_movie, categories=all_categories)

@app.route('/update_movie/<movie_id>', methods=['POST'])
def update_movie(movie_id):
    movies = mongo.db.movies
    movies.update_one( {'_id': ObjectId(movie_id)},
    {"$set":{
        'movie_name': request.form.get('movie_name'),
        'art': request.form.get('art'),
        'released': request.form.get('released'),
        'genre': request.form.get('genre'),
        'runtime':request.form.get('runtime'),
        'rating':request.form.get('rating'),
        'plot':request.form.get('plot')
    }})
    return redirect(url_for('list_movies'))

## View Movie
@app.route('/view_movie/<movie_id>')
def view_movie(movie_id):
    movie_details = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    return render_template('movies/viewmovie.html', movie=movie_details)


# Actor Pages ##################################################################
@app.route('/actors')
def list_actors():
    return render_template("actors/actors.html", actors=mongo.db.actors.find())

## Add actor functions
@app.route('/add_actor')
def add_actor():
    return render_template('actors/createactor.html')

@app.route('/insert_actor', methods=['POST'])
def insert_actor():
    #validation goes here
    actors = mongo.db.actors
    actors.insert_one(request.form.to_dict())
    return redirect(url_for('list_actors'))

## Edit actor functions
@app.route('/edit_actor/<actor_id>')
def edit_actor(actor_id):
    the_actor = mongo.db.actors.find_one({"_id": ObjectId(actor_id)})
    all_categories = mongo.db.categories.find()
    return render_template('actors/editactor.html', actor=the_actor, categories=all_categories)

@app.route('/update_actor/<actor_id>', methods=['POST'])
def update_actor(actor_id):
    actors = mongo.db.actors
    actors.update( {'_id': ObjectId(actor_id)},
    {"$set":{
        'actor_name': request.form.get('actor_name'),
        'photo': request.form.get('photo'),
        'background': request.form.get('background')
    }})
    return redirect(url_for('list_actors'))

## View actor
@app.route('/view_actor/<actor_id>')
def view_actor(actor_id):
    actor_details = mongo.db.actors.find_one({"_id": ObjectId(actor_id)})
    return render_template('actors/viewactor.html', actor=actor_details)


# Misc #########################################################################
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
