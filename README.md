# Stream Two Project - Gamers Galley

This is a web application I have created that gives users the ability to create, read, update, and delete games and game reviews.
I chose to use my own idea to demonstrate my capaibiites of HTML,CSS,JavaScript,Python+Flask, and MongoDB in cooperation with eachother.

The web application contains a home page that users will be greeted with, it allows the user to search for a game and expand the title to see the reviews for that game.
There's a register page that allows a user to create an account for this web application and a login page that allows the user to sign in which creates a session cookie.
When signed in the user is redirected to their profile page which currently just displays the profile name.
Once signed in the user will be able to add a review for any game that's currently in the database however, if a game is not in the database the user also has the option to add a game.
Equally once a review or game has been added to the backend database the web application gives the user the options to edit or delete existing records.
And lastly there's a function that gives the user the option to logout of their session cookie.
 
## UX

This web application is created for the user to have visibility of other users reviews on their favourite game titles.

As a user I would like to have the ability to be able to see other peoples reviews of my favourite game titles, with the added funtionality to search for games.
I would also appreciate having the added function to create my own account and login to leave my own reviews on games, equally I would like to have the option to logout.
If I make a mistake on my review or wish to change it later on I would also like to be able to edit or delete my review.
When a game I want to leave a review for isn't an available option I want to be able to add a game to the application, and similarly to the reviews I would like to edit and delete games too.

## Features

When I had the idea for this web application I wanted to create something that allowed users to manipulate and store data in a backend database using a user friendly frontend application,
I was inspired by this idea because gaming is one of my interests.

Firstly I created the page that allowed users to read game reviews directly from the database, but in order to display game reviews specific to the user that left them I had to create user
authentication and authorisation which will put the user into a session cookie that would be recognised by the database. The user has the option to register with Gamers Galley as well as
login, which creates a session cookie.

Once the user creates a session cookie it will give them the option to add a game review for any title available on the database, and once the review has been created the user has the option
to edit and remove their own game reviews.

If a game title isn't available for the user to leave a review on, they also have the option of creating, editing, and removing game titles.

When on the home page the user can also search for game titles, which when expanded will show all of the reviews created for the game.

Finally the user can logout of the session cookie, which returns them to the login page.
 
### Existing Features

- Feature 1 - User can search for game titles to quickly display any game reviews associated to it.
- Feature 2 - User can register to the web application which enters the user into a session cookie.
- Feature 3 - User can login to the web application which enters the user into a session cookie.
- Feature 4 - User can add a review directly to the database for any available game title, once created the user can only edit and delete their own reviews.
- Feature 5 - User can add a game directly to the database, and once created any user can edit and delete the games that are on the collection in MongoDB.
- Feature 6 - User can logout of the web application which exits the session cookie.

### Features Left to Implement

- Feature idea - I would like to add more functionality to the profile page, currently it will only display the profile that the user is logged in to but I would like to give
the option for the user to update their password and see the reviews that were created by that user.

## Technologies Used

- HTML

- CSS

- JavaScript

- Python+Flask

- MongoDB

- [Materialize](https://materializecss.com/)
    - The project uses **Materialize** to achieve the UX on the frontend of the application.

- [jQuery](https://jquery.com/)
    - The project uses jQuery for the following Materialize JavaScript components:
        1. Side navigational bar for smaller viewports
        2. Dropdown for the account settings within the side navigational bar
        3. Collapsible accordion on the main page
        4. Select dropdown on add and edit pages for game reviews and titles.
        5. Datepicker component on add and edit pages for game reviews and titles.

- [FontAwesome](https://fontawesome.com/)
    - The project uses **FontAwesome** to give icons that provide a good UX on the frontend of the application.

## Testing

1. Search Bar Success
    1. Navigate to the home page.
    2. Enter the game title you want to display.
    3. Click the search button to search.
    4. The search will successfully display game titles that match the words that have been entered in to the search

2. Search Bar Failure
    1. Navigate to the home page.
    2. Enter the game you want to search for.
    3. Click the search button to search.
    4. The search will display a flash message to say no results were found.

3. Search Bar Reset
    1. Navigate to the home page.
    2. Enter the game you want to search for.
    3. Click the search button to search.
    4. The search will either display results or display a flash message to say no results were found.
    5. Click the reset button to reset the search and display all results.

4. User Creation Success
    1. Navigate to the registration page.
    2. Enter a username and password that meets the requirements.
    3. The form will submit and create a session cookie for the user.
    4. The user will be redirected to the profile page and display a flash message to say registration was successful.
    5. The record is added to the backend database.

5. User Creation Failure
    1. Navigate to the registration page.
    2. Enter a username and password that meets the requirements.
    3. The form will submit but if the username already exists in the database display a flash message to say the username already exists.

6. Login Success
    1. Navigate to the login page.
    2. Enter a username and password that exists in the database.
    3. the user will be redirected to the profile page and display a flash message to welcome the user.

7. Login Failure
    1. Navigate to the login page.
    2. Enter a username and password that does not exist in the database.
    3. The user will be not be redirected, instead display a flash message to say incorrect username and/or password.

8. Add Review Success
    1. Navigate to the add review page.
    2. Fill in all of the form elements.
    3. Click the add review button to submit the form.
    4. The user will be redirected to the home page and display a flash message to say the review was successfully added.
    5. The record is added to the backend database.

9. Add Review Failure
    1. Navigate to the add review page.
    2. Do not fill in all of the form elements.
    3. The user will be prompted to fill in the form element in order to continue.

9. Edit Review
    1. Navigate to the home page.
    2. Click the edit button on a review left by your current user session.
    3. The user will be redirected to the edit review page with all of the form elements prefilled.
    4. Amend any of the form elements and click the edit review button, the user will not be redirected but display a flash message to say the review was successfully updated.
    5. Navigate back to the home page.
    6. The user will see the review has been successfully updated and it is updated in the backend database.

10. Cancel Edit Review
    1. Navigate to the home page.
    2. Click the edit button on a review left by your current user session.
    3. The user will be redirected to the edit review page with all of the form elements prefilled.
    4. Click the cancel button.
    5. The user will be redirected to the home page.

11. Delete Review
    1. Navigate to the home page.
    2. Click the remove button on a review left by your current user session.
    3. The user will be displayed a flash message to say the review was successfully deleted.
    4. The record is removed from the backend database.

12. Add Game Success
    1. Navigate to the manage games page.
    2. Click the add game button.
    3. The user will be redirected to the add game page.
    4. Fill in all of the form elements.
    5. Click the add game button to submit the form.
    6. The user will be redirected to the manage games page and display a flash message to say the game was successfully added.
    5. The record is added to the backend database.

13. Add Game Failure
    1. Navigate to the manage games page.
    2. Click the add game button.
    3. Do not fill in all of the form elements.
    4. The user will be prompted to fill in the form element in order to continue.

14. Edit Game
    1. Navigate to the manage games page.
    2. Click the edit button on a game.
    3. The user will be redirected to the edit game page with all of the form elements prefilled.
    4. Amend any of the form elements and click the edit review button, the user will be redirected to the manage games page and display a flash message to say the game was successfully updated.
    5. The record has updated in the backend database.

15. Cancel Edit Game
    1. Navigate to the manage games page.
    2. Click the edit button on a game.
    3. The user will be redirected to the edit game page with all of the form elements prefilled.
    4. Click the cancel button.
    5. The user will be redirected to the manage games page.

16. Delete Game
    1. Navigate to the manage games page.
    2. Click the remove button on a game.
    3. The user will be displayed a flash message to say the game was successfully deleted.
    4. The record is removed from the backend database.

17. User Logout
    1. Navigate to the log out option in the navigational bar.
    2. Click the log out link.
    3. The user will be redirected to the login page and display a flash message to say you have been logged out.

## Deployment
This site is hosted using GitHub pages and Heroku, I have deployed the site directly from the master branch. Now it has been deployed this site will update automatically following any new commits to the master.

To run locally, you can clone this repository directly into the editor of your choice by pasting git clone https://github.com/Boofy360/gamers-galley into your terminal. 
To cut ties with this GitHub repository, type git remote rm origin into the terminal.

## Credits

### Content

- The content is written by the users in the community.

### Media

- The background vector I used for every page was created by [freepik.com](www.freepik.com) free graphic resources.

### Acknowledgements

- The tutor support team were there for assistance in troubleshooting any bugs that I came across and was not able to resolve by researching myself.
- I reference [W3Schools](https://www.w3schools.com/) as the online library that I used for basic troubleshooting.
- The CSS code has been validated using the [CSS W3C Markup Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input)
- The HTML code has been validated using the [HTML W3C Markup Validation Service](https://validator.w3.org/#validate_by_input)
- The Python code has been validated using the [PEP8 Online Checker](http://pep8online.com/)
- I acknowledge the code for the python application came from the video lessons for the Data Centric Development mini project [Putting it all together](https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/9e2f12f5584e48acb3c29e9b0d7cc4fe/054c3813e82e4195b5a4d8cd8a99ebaa/?activate_block_id=block-v1%3ACodeInstitute%2BDCP101%2B2017_T3%2Btype%40sequential%2Bblock%40054c3813e82e4195b5a4d8cd8a99ebaa)