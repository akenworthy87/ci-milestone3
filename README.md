# CI-Milestone 3: Internal Film Database

The purpose of this project will be to make a web accessible database of films; users will be able to view, add, and edit records of films, ~~and the same for actors~~.

The movie database will contain information about the movie such as name, age rating, genre, running time, the synopsis, and a list of staring actors. Users will also be able to post comments/reviews of the movie.

~~The actor database will feature their names, age, a brief background, and list the movies they star in.~~

A demonstration of this project is located here: [ak87-ci-milestone3.herokuapp.com](https://ak87-ci-milestone3.herokuapp.com/)
 
## UX
 
### Intended Audience

As an authentication system is out of scope for this project, the assumed target userbase would be for a private group that can trust its members to use the honour system.  
Perhaps it is a group of film enthusiasts that want to catalogue and share their opinions of movies they have watched to other members of their group?

### User Stories

###### User 1
> As a movie watcher, I want to be able to visit a page with a list of movies and I want to be able to search it, so I can a find a movie to read about

###### User 2
> As the above user, I want to then go to a page containing information about the movie, so I can be informed about the movie

###### ~~User 3~~
> ~~As a movie reviewer, I want to be able to add a review to a movie, so I give my opinion of the movie to other uses~~

###### ~~User 4~~
> ~~As an actor fan, I want to be able to go to a page with a list of actors and I want to be able to search it, so I can find an actor I like and read about them and see what other movies they are in~~

###### ~~User 5~~
> ~~As the above user, I want to then go to a page with the details of the actor I am interested in, so I can read about them and find what movies they were in~~

###### User 6
> As a contributor, I want to be able to add a new movie to the database

###### User 7
> As a contributor, I want to be able to edit the details of an existing movie, to correct mistakes or add new/missing information etc

###### ~~User 8~~
> ~~As a contributor, I want to be able to add a new actor to the database~~

###### ~~User 9~~
> ~~As a contributor, I want to be able to edit the details of an existing actor, to correct mistakes, or add new/missing information etc~~

###### ~~User 10~~
> ~~As a maintainer, I want to be able to delete reviews on movies, to remove inappropriate ones~~

###### User 11
> As a maintainer, I want to be able to delete unneeded movie records

###### ~~User 12~~
> ~~As a maintainer, I want to be able to delete unneeded actor records~~


### Designs

##### Data Requirements

###### Movies

- id - unique id
- movie_name - name of the movie
- art - link to cover art
- released - date movie released
- runtime - the runtime of the movie (in minutes)
- genre - movie genre (could be a reference id to a genres table?)
- plot - the synopsis of the movie (max: ~500 chars)
- rating - age rating (could be a reference id to a ratings table?)
- [actors] - an array of actor-ids from the actors collection
- [reviews] - an matrix of user reviews, the below information
    - review_id - index id of the review
    - submitter - who submitted the review (defaults to anonymous)
    - review - text of the review (max: ~500 chars)
    - score - score given
    - date - date submitted
- [meta] - meta data of the record
    - date_created - date record was submitted
    - date_edited - date record was amended


Example:

    {
      "_id": {
        "$oid": "5d44361c1c9d44000059417b"
      },
      "movie_name": "Robocop",
      "art": "http://t1.gstatic.com/images?q=tbn:ANd9GcQFgpXvtiPPxziaD8ElfgkJAz8V1bke1hElfwyB0lo28P533aj7",
      "released": {
        "$date": {
          "$numberLong": "536457600000"
        }
      },
      "runtime": {
        "$numberInt": "0"
      },
      "genre": "Police",
      "plot": "Part Man, Part Machine: All Cop",
      "rating": "18",
      "actors": [
        ""
      ],
      "reviews": {
        "review_id": {
          "$oid": "5d44379325e05e00005eb5c0"
        },
        "submitter": "Anonymous",
        "review": "Awesome!!",
        "score": {
          "$numberInt": "5"
        },
        "date": {
          "$date": {
            "$numberLong": "1546300800000"
          }
        }
      },
      "meta": {
        "date_created": {
          "$date": {
            "$numberLong": "536457600000"
          }
        },
        "date_edited": {
          "$date": {
            "$numberLong": "536457600000"
          }
        }
      }
    }

###### Actors

- id - unique id
- actor_name - name of the actor
- photo - headshot photo of the actor
- background - brief background of the actor (max: ~500 chars)
- [movies] - an array of movies actor is in
- [meta] - meta data of the record
    - date_created - date record was submitted
    - date_edited - date record was amended

##### Wireframes

For Desktop wireframes see [docs/wireframes/desktop.pdf](docs/wireframes/desktop.pdf)

For Mobile wireframes see [docs/wireframes/mobile.pdf](docs/wireframes/mobile.pdf)


## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Responsive Frontend - utilizes the Materialize framework to natively respond to different screen sizes, such as mobile and desktops.
- CRUD database - uses MongoDB to provide the database engine, which allows remote storing of records, and provides Create, Edit, Update, and Delete functionality.
- MVC/MVT Design - uses Flask and Jinja templates to generate rich content on the fly.

###### Pages: 
  - List Movies - a page which provides a list of movies in the database, includes a search function.  
    Satisfys User 1.
  - View Movies - a dynamically populated page to display the details of a movie record.  
    Satisfys User 2.
  - Create Movie - provides a form to create a movie record, a stub record can be created with as little as a name.  
    Satisfys User 6.
  - Edit Movie - provides a form to edit the details of a movie record.  
    Satisfys User 7.
  - Remove Movie - provides a system to delete movie records, includes a confirmation page.  
    Satisfys User 11.
  - Validation - requests to create or edit a movie record are passed through a validation function. This prevents users tampering with the form and inserting junk data, as well as checking that required fields have data present, and data sensitive fields have data in the right format. 


### Features Left to Implement
- Authentication: If the site would be to grow in scope to expand its userbase to the public, or even a larger private group, an authentication system would be needed as some people are trolls and enjoy deleting/defacing the records 
- Actors pages: Originally I had intended to have a section for actor information, and had planned to link them to the movies pages and vice versa via a sub-object containing the Unique IDs and Name of the target, this was easy to do on the backend and I did have a working proof of concept on the frontend, but I was unable to find an elegant way to implement the full feature on the frontend, so it has been cut.
- Reviews feature: This was removed for time constraints. I would also change the way I planned to implement, originally I was going to store the reviews in an array of objects on the movie db record, which would've been a bit weird and not very scalable. Instead I would've opted for a separate table of reviews, with a reference to the movie's unique id, as with a traditional relational database. 
- A pagination system will need to be added to the Movies List page once the DB expands above a certain number of records.
- Front End: the current frontend is a barebones proof of concept, I have only implemented the bare minimum CSS to make the site work as expected, one thing to possible adjust is the desktop view - it is a bit left side heavy.
- File uploading: a feature to allow users to upload images to the site to use for the movie art, instead of the current system of hotlinking to an external source.
- MongoDB Connection string: might be better to split this up so username, password, and db are stored as separate env vars and replace the parts of the connection string?
- Clean Requirements.txt: there's a lot of entries in here that pip3 picks up from AWS C9's environment which aren't actually required.

## Technologies Used

###### Languages

- [HTML5](https://www.w3.org/standards/webdesign/htmlcss)
	- Latest version of the Hyper Text Markup Language, used to write the markup language the browser interprets to display the webpage elements.
- [CSS 4](https://www.w3.org/standards/webdesign/htmlcss)
	- Used to create style sheets to adjust the styles of HTML elements.
- [JavaScript](https://developer.mozilla.org/en/JavaScript)
  - Used to provide interactive and dynamic content on the front end.
- [Python 3](https://www.python.org/)
  - Used to provide backend functionality such as database interaction and web app functions.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
  - Templating language for Python that allows Flask to use html templates and dynamically insert data.

###### Frameworks & Libraries

- [MaterializeCSS](https://materializecss.com/)
	- CSS framework that provides a collection of prebuilt styles responsive design, and nav bar features.
- [JQuery](https://jquery.com)
  - A JavaScript framework to simplify DOM manipulation. Required by Materialize.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
  - A Python drive micro-framework which provides web backend processing and uses Jinja html templates generate dynamic web content on the fly.

###### Platforms

- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
  - A NoSQL Database Engine. Used to provide external hosting of data in the 'Cloud'.
- [Github](https://github.com/)
	- Hosting service for Git Software Version Controlled repositories. 
	- Also provides GitHub Projects - a kanban board system I used to keep track of development tasks
- [Heroku](https://www.heroku.com/)
  - Cloud-based web hosting service for dynamic websites.

###### Tools

- [Paint.Net](https://www.getpaint.net/)
    - A drawing program. Used to create the site's Logo, Favicon, and placeholder movie art.
- [AWS Cloud9](https://aws.amazon.com/cloud9/)
	- Provides Linux workspaces which include an IDE for developing web based software, file hosting, git SVN, and basic web server services
- [Google Chrome](https://www.google.com/chrome/)
	- Web browser. Includes Dev Tools which provide information on how the elements are rendered, what style rules are applied, and allows editing of the HTML and CSS to see their effects live in the view pane. 

###### Validators

- [W3C Validator](https://validator.w3.org/)
	- Validates HTML markup files. Checks for errors in syntax such as unclosed tags or unneeded close tags.
- [W3C Jigsaw](https://jigsaw.w3.org/css-validator/)
	- Validates CSS files for syntax errors.
- [PEP8 Online](http://pep8online.com/)
  - Validates Python code for syntax errors and checks for compliance with PEP8 styling rules.


## Testing

Testing documentation is located in a separate [TESTING.md document](docs/TESTING.md) located in the docs folder.

## Deployment

#### MongoDB

First create the database to host the data:

1. Login to MongoDB Atlas and create a new cluster or use existing (consult MongoDB documentation for further instructions)
2. Clusters: Collections: Create a database with desired name, e.g. 'ifdb'
3. (Optional, recommended) Security: Database Access: Create a user with readwrite access to above database
4. Clusters: Connect: Connect your application
    - Driver: Python, Version: 3.11 or later
    - Copy connection string, change username, password, and dbname components to desired ones created above
5. Keep note of connection string for below

#### Heroku

To deploy to Heroku: 

1. Create a fork of the github repo
2. Login to Heroku and create a new app environment (consult Heroku documentation for further instructions)
3. Deploy: Deployment Method: GitHub. 
    - Select your connected user/organisation
    - Enter repo named in step one and search
    - Select branch to deploy in either Automatic Deploys or Manual Deploy
    - Press relevant deploy button
4. Settings: Config Vars: Reveal Config Vars - set the following:
    - IP: 0.0.0.0
    - PORT: 5000
    - APPDEBUG: false (or 'true' (nb:lowercase t) to enable debug mode (best not to))
    - MONGODB_URI: your MongoDB connection string
5. Open app and verify app is running okay

#### Local

To deploy Locally:

1. Create a fork of the github repo 
2. Clone repo to your local environment, e.g. git clone https://github.com/akenworthy87/ci-milestone3.git
3. Create the following environment variables (consult OS documentation for further information)
    - APPDEBUG: false (or 'true' (nb:lowercase t) to enable debug mode)
    - MONGODB_URI: your MongoDB connection string
4. Install requirements with 'pip3 install -r requirements.txt'
5. Run with 'python3 app.py'
6. (Optional) Link Local to Heroku
    - Login with 'heroku login'
    - Add git remote with 'heroku git:remote --app [app name]'
    - Push changes with 'git push heroku master'


#### My Deployment

For the deployment of my demo environment, development work was done through AWS cloud9 and uploaded to my git repo's master branch.  
Periodically I would merge the 'master' dev branch into the 'live' deploy branch.  
I had set Heroku to automatically deploy from the live branch, so once changes were merged to it Heroku would see this and deploy the changes automatically.  
The only difference between the live and dev environments was that the local dev environment's APPDEBUG ENV-VAR was set to true and the live Heroku environment had this set to false. Both connect to the same MongoDB database, though I could've separated these.


## Credits

### Content
- Various information, including plot synopsis, taken from IMDB.com. Used for educational purposes only

### Media
- The images of movie art used in this site were obtained from IMDB.com. Used for education purposes only

### Acknowledgements
- I received inspiration for this project from The Internet Movie Database.
