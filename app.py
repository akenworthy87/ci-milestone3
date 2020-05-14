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
    # Returns a list of the last ten updated movie records
    return render_template("index.html", movies=mongo.db.movies.find().sort('meta.date_updated', -1).limit(10))


# Movie Pages ##################################################################
## Movies list
@app.route('/movies')
def list_movies():
    # Returns a list of movie records, by name ASC
    return render_template("movies/movies.html", movies=mongo.db.movies.find().sort('movie_name', 1))

## View Movie
@app.route('/view_movie/<movie_id>')
def view_movie(movie_id):
    movie_details = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    return render_template('movies/viewmovie.html', movie=movie_details)

## Add movie functions
@app.route('/add_movie')
def add_movie():
    return render_template('movies/createmovie.html', movie={})

@app.route('/insert_movie', methods=['POST'])
def insert_movie():
    moviesDB = mongo.db.movies
    movie_form, form_errors = validate_movie(request.form.to_dict())
    if form_errors:
        return render_template('movies/createmovie.html', movie=movie_form, errors=form_errors)
    # Update datetime stamps
    movie_form.update({'meta.date_updated':datetime.utcnow(),'meta.date_created':datetime.utcnow()})
    # Insert record
    moviesDB.insert_one(movie_form)
    return redirect(url_for('home'))

## Edit movie functions
@app.route('/edit_movie/<movie_id>')
def edit_movie(movie_id):
    the_movie = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    return render_template('movies/editmovie.html', movie=the_movie)

@app.route('/update_movie/<movie_id>', methods=['POST'])
def update_movie(movie_id):
    moviesDB = mongo.db.movies
    
    movie_form, form_errors = validate_movie(request.form.to_dict())
    if form_errors:
        return render_template('movies/editmovie.html', movie=movie_form, errors=form_errors)
    # Update datetime stamps
    movie_form.update({'meta.date_updated':datetime.utcnow()})
    
    moviesDB.update_one( {'_id': ObjectId(movie_id)},
                         {"$set":movie_form})
    # {"$set":{
    #     'movie_name': request.form.get('movie_name').lower(),
    #     'art': request.form.get('art'),
    #     'released': int(request.form.get('released') or 0),
    #     'genre': request.form.get('genre'),
    #     'runtime':int(request.form.get('runtime') or 0),
    #     'rating':request.form.get('rating'),
    #     'director':request.form.get('director'),
    #     'plot':request.form.get('plot'),
    #     'meta.date_updated':datetime.utcnow()
    # }})
    return redirect(url_for('view_movie', movie_id=movie_id))

## Delete movie functions
@app.route('/remove_movie/<movie_id>')
def remove_movie(movie_id):
    the_movie = mongo.db.movies.find_one({"_id": ObjectId(movie_id)},{'movie_id':1,'movie_name':1})
    return render_template('movies/removemovie.html', movie=the_movie)

@app.route('/delete_movie/<movie_id>')
def delete_movie(movie_id):
    mongo.db.movies.remove({'_id':ObjectId(movie_id)})
    return redirect(url_for('home'))

# Validation Functions #########################################################
'''
Takes the submitted form, checks required data is present
Does required transformations
Builds record in expected state for DB insertion/updating
'''
def validate_movie(movie_in):
    errors = []
    movie_out = {}
    # Validation - only req'ed is movie name
    if not movie_in['movie_name']:
        errors.append('A movie name is required')
    else:
        movie_out['movie_name'] = movie_in['movie_name'].lower()
    
    # Transformation
    movie_out.update({
        'released':int(movie_in['released'] or 0),
        'runtime':int(movie_in['runtime'] or 0),
    })
    
    # Add rest
    movie_out.update({
        'art': request.form.get('art'),
        'genre': request.form.get('genre'),
        'rating':request.form.get('rating'),
        'director':request.form.get('director'),
        'plot':request.form.get('plot'),
    })
    
    return movie_out, errors

# Misc #########################################################################
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=os.environ.get('APPDEBUG') == 'true')
