from app import application
from flask import render_template, request, redirect
import json, requests


@application.route("/", methods=["GET", "POST"])
def data():

    if request.method == "POST":

        search = request.form.get("search")

        req = requests.get(f"https://api.jikan.moe/v3/search/anime?q={search}")
        data.list = json.loads(req.content)
        return redirect("/search")
    return render_template("index.html")


@application.route("/search")
def search():
    resp = data.list
    return render_template("results.html", data=resp)


@application.route("/reccomend", methods=["GET", "POST"])
def reccomend():

    genre_dic = {
        "Action": 1,
        "Adventure": 2,
        "Cars": 3,
        "Comedy": 4,
        "Dementia": 5,
        "Demons": 6,
        "Mystery": 7,
        "Drama": 8,
        "Ecchi": 9,
        "Fantasy": 10,
        "Game": 11,
        "Hentai": 12,
        "Historical": 13,
        "Horror": 14,
        "Magic": 16,
        "Martial Arts": 17,
        "School": 23,
        "Sci Fi": 24,
        "Vampire": 32,
    }
    rating_dict = {
        "All": "g",
        "Children": "pg",
        "Teens 13 or older": "pg13",
        "17+ recommended": "r17",
        "Mild Nudity": "r",
        "Hentai": "rx",
    }
    if request.method == "POST":
        status = request.form.get("status")
        genre = request.form.get("genre")
        rated = request.form.get("rated")
        genre_dict = genre_dic[genre]
        rated_dict = rating_dict[rated]
        req = requests.get(
            f"https://api.jikan.moe/v3/search/anime?genre={genre_dict}&rated={rated_dict}&status={status}"
        )
        reccomend.list = json.loads(req.content)
        return redirect("/ani-list")
    return render_template("reccomend.html")


@application.route("/ani-list")
def anilist():

    resp = reccomend.list
    return render_template("list.html", data=resp)
