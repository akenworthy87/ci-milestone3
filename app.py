import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
import re

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get('MONGODB_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGODB_URI')

mongo = PyMongo(app)

# Main Page ####################################################################
'''
Returns a list of the last ten updated movie records
'''
@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", movies=mongo.db.movies.find().sort('meta.date_updated', -1).limit(10))


# Movie Pages ##################################################################
## Movies list
''' 
Returns a list of movie records, by name ASC 
'''
@app.route('/movies')
def list_movies():
    return render_template("movies/movies.html", movies=mongo.db.movies.find().sort('movie_name', 1))

'''
Takes input from search field
Converts to lowercase (all movie names are stored as lowercase in DB)
Finds results, including partial matches, and renders list template
'''
## Search Movies
@app.route('/movies/search', methods=['POST'])
def search_movies():
    query = request.form.get('msearch').lower()
    results = mongo.db.movies.find({"movie_name":{'$regex': query}}).sort('movie_name', 1)
    return render_template("movies/movies.html", movies=results)

## View Movie
'''
Retrieves movie records via movie_id and renders view template
'''
@app.route('/view_movie/<movie_id>')
def view_movie(movie_id):
    movie_details = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    return render_template('movies/viewmovie.html', movie=movie_details)


## Add movie functions
'''
Renders page for create movie record form
'''
@app.route('/add_movie')
def add_movie():
    return render_template('movies/createmovie.html', movie={})

'''
Gets form data from create movie page
Validates. If error, returns to create page with errors and repopulates form with submitted data
           If passes updates timestamps and inserts new record
Returns home
'''
@app.route('/insert_movie', methods=['POST'])
def insert_movie():
    moviesDB = mongo.db.movies
    movie_form, form_errors = validate_movie(request.form.to_dict())
    if form_errors:
        return render_template('movies/createmovie.html', movie=movie_form, errors=form_errors)
    # Update datetime stamps
    movie_form.update({'meta':{'date_updated':datetime.utcnow(),'date_created':datetime.utcnow()}})
    # Insert record
    moviesDB.insert_one(movie_form)
    return redirect(url_for('home'))

## Edit movie functions
''' 
Retrives movie record and passes to edit movie form 
'''
@app.route('/edit_movie/<movie_id>')
def edit_movie(movie_id):
    the_movie = mongo.db.movies.find_one({"_id": ObjectId(movie_id)})
    return render_template('movies/editmovie.html', movie=the_movie)

'''
Gets form data from edit movie page
Validates. If error, returns to edit page with errors and repopulates form with submitted data
           If passes updates timestamps and updates record
Returns view page for movie
'''
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
    return redirect(url_for('view_movie', movie_id=movie_id))

## Delete movie functions
'''
Gets movie name and id, renders confirmation page to ask for deletion confirmation
'''
@app.route('/remove_movie/<movie_id>')
def remove_movie(movie_id):
    the_movie = mongo.db.movies.find_one({"_id": ObjectId(movie_id)},{'movie_id':1,'movie_name':1})
    return render_template('movies/removemovie.html', movie=the_movie)

'''
When confirm button clicked, deletes record, returns to home
'''
@app.route('/delete_movie/<movie_id>')
def delete_movie(movie_id):
    mongo.db.movies.remove({'_id':ObjectId(movie_id)})
    return redirect(url_for('home'))

# Validation Functions #########################################################
'''
Takes the submitted form, checks required data is present
Does required transformations
Builds record in expected state for DB insertion/updating
This is done to prevent extra data being inserted by malicious users
'''
def validate_movie(movie_in):
    errors = []
    movie_out = {}
    # Validation
    if not movie_in['movie_name']:
        errors.append('A movie name is required')
    if movie_in['released'] and not re.match('^[0-9]+$', movie_in['released']):
        errors.append('Please enter only numbers for release year')
    if movie_in['runtime'] and not re.match('^[0-9]+$', movie_in['runtime']):
        errors.append('Please enter only numbers for runtime')
    
    if not errors:
        # Transformation
        movie_out.update({
            'movie_name':movie_in['movie_name'].lower(),
            'released':int(movie_in['released'] or 0),
            'runtime':int(movie_in['runtime'] or 0),
        })
        # Add rest of data
        movie_out.update({
            'art': movie_in['art'],
            'genre': movie_in['genre'],
            'rating': movie_in['rating'],
            'director': movie_in['director'],
            'plot': movie_in['plot'],
        })
    return movie_out, errors

# Misc #########################################################################
'''
Checks if Env-var APPDEBUG is set to true
If anything else, including 'True' (as this check is case sensitive), debug mode is set to false. 
This allows live environ to run in debug false without having to change dev environment settings. 
'''
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=os.environ.get('APPDEBUG') == 'true')
