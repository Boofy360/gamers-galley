import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_game_reviews")
def get_game_reviews():
    # get game and reviews from db
    reviews = list(mongo.db.reviews.find())
    games = list(mongo.db.games.find())
    return render_template("reviews.html", reviews=reviews, games=games)


@app.route('/select', methods=["GET", "POST"])
def search():
    # search games
    query = request.form.get("query")
    games = list(mongo.db.games.find({"$text": {"$search": query}}))
    return render_template("reviews.html", games=games)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"],
                request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    # add review to db
    if request.method == "POST":
        review = {
            "game_title": request.form.get("game_title"),
            "headline": request.form.get("headline"),
            "review": request.form.get("review"),
            "rating": request.form.get("rating"),
            "date": request.form.get("date"),
            "created_by": session["user"]
        }
        mongo.db.reviews.insert_one(review)
        flash("Review Successfully Added")
        return redirect(url_for("get_game_reviews"))

    games = mongo.db.games.find().sort("game_title", 1)
    return render_template("add_review.html", games=games)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    # update review in db
    if request.method == "POST":
        submit = {
            "game_title": request.form.get("game_title"),
            "headline": request.form.get("headline"),
            "review": request.form.get("review"),
            "rating": request.form.get("rating"),
            "date": request.form.get("date"),
            "created_by": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, submit)
        flash("Review Successfully Updated")

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    games = mongo.db.games.find().sort("game_title", 1)
    return render_template("edit_review.html", review=review, games=games)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    # delete review in db
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("get_game_reviews"))


@app.route('/get_game_titles')
def get_game_titles():
    # get games from db
    games = list(mongo.db.games.find().sort("game_title", 1))
    return render_template("games.html", games=games)


@app.route("/add_game_title", methods=["GET", "POST"])
def add_game_title():
    # add game to db
    if request.method == "POST":
        game = {
            "game_title": request.form.get("game_title"),
            "release_date": request.form.get("release_date"),
            "age_rating": request.form.get("age_rating"),
            "available_platforms": request.form.get("available_platforms")
        }
        mongo.db.games.insert_one(game)
        flash("New Game Added")
        return redirect(url_for("get_game_titles"))

    return render_template("add_game.html")


@app.route("/edit_game/<game_id>", methods=["GET", "POST"])
def edit_game(game_id):
    # edit game in db
    if request.method == "POST":
        submit = {
            "game_title": request.form.get("game_title"),
            "release_date": request.form.get("release_date"),
            "age_rating": request.form.get("age_rating"),
            "available_platforms": request.form.get("available_platforms")
        }
        mongo.db.games.update({"_id": ObjectId(game_id)}, submit)
        flash("Game Successfully Updated")
        return redirect(url_for("get_game_titles"))

    game = mongo.db.games.find_one({"_id": ObjectId(game_id)})
    return render_template("edit_game.html", game=game)


@app.route("/delete_game/<game_id>")
def delete_game(game_id):
    # delete game in db
    mongo.db.games.remove({"_id": ObjectId(game_id)})
    flash("Game Successfully Deleted")
    return redirect(url_for("get_game_titles"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT")),
            debug=False)
