#### Validation
- HTML
    - PASS
- CSS
    - PASS
- Python
    - PASS - some warnings about linelength remain but they're not excessively long (<120chr)

#### Functions
Test various CRUD functions of app in expected usage scenarios:

1. Home displays last ten updates movie records
    - PASS
2. Movies list displays list of movie records, ordered by Title
    1. Order is case sensitive
        - Made movie_names convert to lowercase before storing in DB
3. View movie displays all information correctly
    1. Plot didn't respect linebreaks stored in DB
        - Changed div to pre-wrap
4. Create allows creation of movie with full details, with only movie title
    1. Runtime and Release Year were storing as strings, despite being numbers on html form
        - Added code to convert above fields to Ints
    2. Throws error if Runtime or Release Year blank
        - Caused by Int() conversion, made to set value to 0 if null
5. Edit allows editing of movie records
    - PASS
6. Remove
    - Displays confirmation page
        - PASS
    - Cancel button takes back to movie view page
        - PASS
    - Confirm removes record from DB, returns to movie list
        - PASS
7. Responsive Design: On small screens Materalize.css will change to mobile view
    - Check Nav links work on both sizes of screen
        - PASS 
    - Check pages shift to mobile/desktop views as per wireframes
        - PASS - movie view is a little left heavy content wise on mobile, but not a critical issue 

#### Movie records validation
1. Create/Edit frontend should
    - Mark 'Movie Name as required
        - PASS
    - Release year - allow only numbers
        - PASS
    - Runtime - allow only numbers
        - PASS
2. To prevent form tampering (i.e. using browser devtools to remove 'required' tags and changing form-field data-type),  
   backend validation should validate the following:
    - Only approved fields are added to DB, extras are discarded
        - PASS
    - Movie Name is required, an error should be returned if missing
        - PASS
    - Release Year should return error if not only numbers
        - PASS
    - Runtime should return error if not only numbers
        - PASS
3. Backend validation should perform following transformations:
    - Convert Movie Name to lowercase
        - PASS
    - Convert Release Year to Int, or 0 if null
        - PASS
    - Convert Runtime to Int, or 0 if null
        - PASS

#### Deployment
Testing the Deployment instructions will be done via creating new Heroku and local environments, as an end user would. 

- Test what happens when MongoDB_URI string points to a database that doesn't exit
    - Mongo will create the non existent database and collection, which is handy
- Test what happens when environment variables are not set on deployment platform
    - App crashes and Heroku web displays error as expected 

#### Notes/Observations
- PyMongo handles embedded object values different for insert and update functions, 
    which is why the setting/updating meta.timestamps is done differently in the create and update movie functions.
    The Insert function does not support {'parent.child':value} syntax and will throw an error about the dot, so requires the movie_form dictionary to have the meta records appended in the {'parent':{'child':value}} syntax.  
    The Update function does not work correctly with the above, as updating the date_updated timestamp would cause the meta object to lose the date_created attribute. So for the Update function it's $Set attribute required the meta object's child to be update via the {'parent.child':value} syntax.

