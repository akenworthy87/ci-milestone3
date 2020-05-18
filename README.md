# CI-Milestone 3: Internet Film Database

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

For Mobile wireframes see [TBC]

##### Code Logic


------------------------------------------------------------------
------------------------------------------------------------------
------------------------------------------------------------------

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Authentication: If the site would be to grow in scope to expand its userbase to the public, or even a larger private group, an authentication system would be needed as some people are trolls and enjoy deleting/defacing the records 
- Actors pages: Originally I had intended to have a section for actor information, and had planned to link them to the movies pages and vice versa via a sub-object containing the Unique IDs and Name of the target, 
  this was easy to do on the backend and I did have a working proof of concept on the frontend, but I was unable to find an elegant way to implement the full feature on the frontend, so it has been cut.
- Reviews feature: This was removed for time constraints. I would also change the way I planned to implement, originally I was going to store the reviews in an array of objects on the movie db record,  
  which would've been a bit weird and not very scalable. Instead I would've opted for a seperate table of reviews, with a reference to the movie's unique id, as with a traditional relational database. 

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from The Internet Movie Database